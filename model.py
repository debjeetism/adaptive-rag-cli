from dotenv import load_dotenv
load_dotenv()

import os
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

llm_model = ChatGoogleGenerativeAI(
    google_api_key=GOOGLE_API_KEY, 
    model="gemini-2.5-flash",              # Standard text model, or "gemini-pro-vision" for image support
    temperature=0
)

embed_model = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004",
    google_api_key=GOOGLE_API_KEY
)