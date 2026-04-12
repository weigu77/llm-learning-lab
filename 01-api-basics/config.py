import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("BASE_URL")
MODEL_NAME = "agent/deepseek-v3.2(free)"

if not API_KEY:
    raise ValueError("❌ 找不到 API Key！请检查 .env 文件是否填写了 OPENAI_API_KEY")