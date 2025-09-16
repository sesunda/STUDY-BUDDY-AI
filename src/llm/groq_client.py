from langchain_groq import ChatGroq
from src.config.settings import settings

def get_groq_llm():
    return ChatGroq(
        groq_api_key = settings.GROQ_API_KEY,
        model_name = settings.MODEL_NAME,
        temperature=settings.TEMPERATURE
    )