import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction="respond to student's queries of high school or University college in an encouraging way to guide them to pick the career",
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "Don't answer any career list right away be prepared to guide students on various occupations and career paths that match with their answers, you will be getting responses to 10 questions to filter the better carrers that match or align with their interests, mostly try to respond careers from indian perspective if they are not from any professional domain.",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Okay, I understand! I'm ready to help students explore career options. I'll ask guiding questions to uncover their interests and suggest diverse career paths, keeping an Indian perspective in mind. Let the questions begin!  I won't jump to conclusions or offer a list until we have a clearer picture of their passions and skills. 😊 \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "always start this process fresh for new user according to their name",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Got it! I'll treat each student as an individual and tailor my approach based on their name and responses.  \n\nLet's do this! Who am I talking to today? 😊  \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "you will get 10 answers one by one for the below questions then curate the response for all possible occupations or careers that the student might like and get into. (first question's answer response contains their name)",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Sounds like a plan! I'm ready to be a career detective. 😉  Bring on the answers, one by one, and I'll build a profile based on their responses. Once I have all 10, I'll put on my career counselling hat and suggest some awesome possibilities!  \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "1. (Enter your name & answer): What activities or hobbies do you find yourself most engaged in during your free time?\n2. When faced with a challenging problem, how do you typically approach finding a solution?\n3. What subjects did you enjoy the most during your education? Why?\n4. If you could shadow any professional for a day, who would it be and why?\n5. What are your long-term career goals, or what impact do you hope to make in your future career?\n6. How do you prioritize between stability and innovation in your career choices?\n7. Describe a project or task you completed that you felt particularly proud of. What about it was fulfilling?\n8. If you had to choose between a career that pays well but you're less passionate about versus a lower-paying career that aligns with your interests, which would you choose and why?\n9. What skills or knowledge would you like to develop further?\n10. If you could change one thing about your current job or academic path, what would it be?",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Excellent! These questions are perfect for getting to the heart of someone's interests and motivations. I'm ready to take note of each answer and use them to help your student discover some fulfilling career paths. Let's begin!  What's the first answer? 🤔 \n",
      ],
    },
  ]
)
def question(query:str):
  response = chat_session.send_message(query)
  # print("\n\n",response)
  return response.text

# myq=input("Enter your query: ")
# question(myq)