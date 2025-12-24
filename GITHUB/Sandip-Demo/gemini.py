import google.generativeai as genai
import os

GOOGLE_API_KEY = "AIzaSyAUn7KPkngh6vDxmT6AX7sRW62pqJ6_l7I" 
GEMINI_MODEL = "gemini-2.5-flash-lite"


genai.configure(api_key=GOOGLE_API_KEY)

system_prompt = """
You are a good cv designer.
"""

model = genai.GenerativeModel(GEMINI_MODEL, system_instruction=system_prompt)

prompt = """
which human landed on the mars first ?
"""

response = model.generate_content(prompt+" ____")
print(response.text)
