import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

found = False
for m in genai.list_models():
    if '1.5-flash' in m.name:
        print(f'FOUND: {m.name}')
        found = True
if not found:
    print('NOT FOUND')
