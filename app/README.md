# Security Implementation Generator

A Flask application that uses AI to generate detailed implementation requirements for security controls.

## Setup

1. Clone the repository
```bash
git clone [repository-url]
cd [repository-name]
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create `.env` file and add your OpenAI API key
```
OPENAI_API_KEY=your-api-key-here
SECRET_KEY=your-secret-key-here
```

5. Run the application
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Project Structure
```
.
├── app/
│   ├── __init__.py
│   ├── prompts.py      # AI prompt templates
│   └── ai_helper.py    # AI interaction logic
├── templates/
│   └── index.html      # Main template
├── .env                # Environment variables (not in repo)
├── config.py          # Configuration settings
└── app.py            # Main application file
```

## Features
- Generate implementation requirements for security controls
- View AI prompts used for generation
- Detailed logging for debugging
