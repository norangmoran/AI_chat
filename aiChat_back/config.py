import os
from dotenv import load_dotenv
from openai import OpenAI

# .env 파일 로드
load_dotenv()

# 환경 변수 읽기
openai_api_key = os.getenv("OPENAI_API_KEY")