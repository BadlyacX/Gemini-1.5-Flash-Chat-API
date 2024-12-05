import google.generativeai as genai
from google.colab import userdata

genai.configure(api_key=userdata.get('GEMINI_API_KEY'))

model = genai.GenerativeModel("gemini-1.5-flash")  

print("Enter a prompt to chat:")
while True:
  prompt = input()
  if  prompt == "exit":
    break
  response = model.generate_content(prompt)
  print(response.text)
