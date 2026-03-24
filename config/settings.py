"""
Configuration settings for Streamlit application
"""

# API Configuration
API_BASE_URL = "http://127.0.0.1:8000"
PUBLIC_BASE_URL = "https://bhuvanpatil24-sentinelai.hf.space"
# UI Configuration
APP_TITLE = "Company Internal RAG Chatbot"
APP_ICON = "🤖"
PAGE_LAYOUT = "wide"

# Chat Configuration
MAX_TOP_K = 20
MAX_TOKENS_LIMIT = 500

# Admin Configuration
AVAILABLE_ROLES = [
    "System Architect",
    "Frontend Developer",
    "DevOps Engineer",
    "Content Strategist",
    "Marketing Analyst",
    "Intern"
]

# UI Messages
WELCOME_MESSAGE = """
👋 Welcome to the Company Internal RAG Chatbot!

I can help you find information from company documents based on your role and department access.

How to use:
- Type your question in the chat input below
- I'll search through accessible documents and provide an answer
- Sources will be cited for transparency
- You can adjust search parameters in the sidebar

Privacy: Your queries and the documents you can access are determined by your role.
"""
