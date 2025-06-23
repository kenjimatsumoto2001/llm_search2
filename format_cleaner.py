#これはoutputされたものを整形するプログラム


from ollama import Client
client = Client(
  host='http://localhost:11434',
  headers={'Content-Type': 'application/json'}
)


try: 
    response = client.chat(model='llama3.3:latest', messages=[
      {
        'role': 'user',
        'content': 'Why is the sky blue?',
      },
    ])
    print(response['message']['content'])
    # or access fields directly from the response object
    print(response.message.content)
except Exception as e:
    print(f"エラーが発生しました: {e}")
    response = None