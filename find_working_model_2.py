import google.generativeai as genai
import os
from dotenv import load_dotenv
import time

load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

candidates = [
    'gemini-2.0-flash',
    'gemini-2.0-flash-exp',
    'gemini-exp-1206'
]

print('Testing 2.0 models...')
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
