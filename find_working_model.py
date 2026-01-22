import google.generativeai as genai
import os
from dotenv import load_dotenv
import time

load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

candidates = [
    'gemini-1.5-flash',
    'gemini-1.5-flash-001',
    'gemini-1.5-flash-002',
    'gemini-1.5-pro',
    'gemini-1.0-pro',
    'gemini-pro'
]

print('Testing models...')
for model_name in candidates:
    print(f'Trying {model_name}...', end='')
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content('Hi')
        print(f' SUCCESS!')
        print(f'RECOMMENDATION: Use {model_name}')
        break
    except Exception as e:
        print(f' FAILED ({e})')
        time.sleep(1)
