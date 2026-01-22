from backend.llm_client import get_chat_response

try:
    print('Testing streaming...')
    gen = get_chat_response('Hello', stream=True)
    for chunk in gen:
        print(f'Chunk: {chunk}')
    print('Stream done.')
except Exception as e:
    print(f'CRASH: {e}')
