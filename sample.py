import ollama
response = ollama.chat(model='deepseek-r1:70b', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response['message']['content'])