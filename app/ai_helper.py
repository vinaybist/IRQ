from openai import OpenAI
from flask import current_app
from datetime import datetime
from app.prompts import SecurityPrompts
import logging

logger = logging.getLogger(__name__)

class SecurityAIHelper:
    def __init__(self):
        self.prompts = SecurityPrompts()

    def _get_client(self):
        """Get OpenAI client with current app context"""
        try:
            api_key = current_app.config['OPENAI_API_KEY']
            if not api_key:
                logger.error('OpenAI API key not found in configuration')
                raise ValueError('OpenAI API key not configured')
            return OpenAI(api_key=api_key)
        except Exception as e:
            logger.error(f'Error initializing OpenAI client: {str(e)}')
            raise

    def get_implementation_requirements(self, security_control):
        """Gets implementation requirements from AI model"""
        try:
            client = self._get_client()
            logger.info(f'Sending request to OpenAI for security control: {security_control}')
            
            response = client.chat.completions.create(
                model=current_app.config['GPT_MODEL'],
                messages=[
                    {
                        "role": "system",
                        "content": self.prompts.system_prompt()
                    },
                    {
                        "role": "user",
                        "content": self.prompts.implementation_prompt(security_control)
                    }
                ],
                temperature=0.7
            )
            
            logger.info('Successfully received response from OpenAI')
            return {
                "status": "success",
                "requirements": response.choices[0].message.content,
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f'Error in get_implementation_requirements: {str(e)}', exc_info=True)
            return {
                "status": "error",
                "message": str(e),
                "timestamp": datetime.now().isoformat()
            }