from flask import Flask, render_template, request, jsonify
from app.ai_helper import SecurityAIHelper
from app.prompts import SecurityPrompts
from config import Config
import os
import logging
from logging.handlers import RotatingFileHandler

# Setup logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Create logs directory if it doesn't exist
if not os.path.exists('logs'):
    os.makedirs('logs')

# Create file handler
file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=10)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
))
file_handler.setLevel(logging.INFO)
logger.addHandler(file_handler)

template_dir = os.path.abspath('templates')
app = Flask(__name__, template_folder=template_dir)
app.config.from_object(Config)

# Add the logger to Flask app
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
app.logger.info('Application startup')

ai_helper = SecurityAIHelper()
prompts = SecurityPrompts()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()
        security_control = data.get('security_control', '')
        
        if not security_control:
            logger.error('No security control provided')
            return jsonify({"error": "No security control provided"}), 400
        
        logger.info(f'Processing security control: {security_control}')
        result = ai_helper.get_implementation_requirements(security_control)
        
        if result.get('status') == 'error':
            logger.error(f'Error in AI processing: {result.get("message")}')
            
        return jsonify(result)
    except Exception as e:
        logger.error(f'Error in analyze endpoint: {str(e)}', exc_info=True)
        return jsonify({"error": "An internal error occurred", "details": str(e)}), 500

@app.route('/get-prompt', methods=['POST'])
def get_prompt():
    try:
        data = request.get_json()
        security_control = data.get('security_control', '')
        prompt_type = data.get('prompt_type', 'implementation')
        
        if not security_control:
            logger.error('No security control provided')
            return jsonify({"error": "No security control provided"}), 400
        
        logger.info(f'Getting prompt for type: {prompt_type}')
        
        if prompt_type == 'implementation':
            prompt = prompts.implementation_prompt(security_control)
        elif prompt_type == 'validation':
            prompt = prompts.validation_prompt(security_control)
        else:
            logger.error(f'Invalid prompt type: {prompt_type}')
            return jsonify({"error": "Invalid prompt type"}), 400
            
        return jsonify({"prompt": prompt})
    except Exception as e:
        logger.error(f'Error in get_prompt endpoint: {str(e)}', exc_info=True)
        return jsonify({"error": "An internal error occurred", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)