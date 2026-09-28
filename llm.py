import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

# Load environment variables
load_dotenv()

# Initialize LLM
llm = init_chat_model("groq:openai/gpt-oss-20b")