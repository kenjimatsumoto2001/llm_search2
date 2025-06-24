import ollama

response1 = ollama.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': 'What is the capital of France? (Only capital name)',
  },
])
response2 = ollama.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': 'And what about Germany? (Only capital name)',
  },
])

print(response1['message']['content'])
print(response2['message']['content'])
