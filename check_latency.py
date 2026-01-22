import time
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

def test_latency():
    print('Testing Gemini API Speed...')
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    start_time = time.time()
    print(f'Sending request at {start_time}')
    
    # Test Streaming Latency
    response = model.generate_content('Tell me a short joke.', stream=True)
    
    first_token_time = None
    for chunk in response:
        if first_token_time is None:
            first_token_time = time.time()
            print(f'Time to First Token (TTFT): {first_token_time - start_time:.4f} seconds')
    
    end_time = time.time()
    print(f'Total Generation Time: {end_time - start_time:.4f} seconds')

if __name__ == '__main__':
    test_latency()
