import openai
import speech_recognition as sr
import pyttsx3
#Create an open Ai account and generate an api key. Copy the api key and pest it below.
openai.api_key = "<Pest your openai.api_key here >"
engine = pyttsx3.init()
listener = sr.Recognizer()

model = "text-davinci-003"
user = input ("Enter your question here: ")   
    
completion = openai.Completion.create(model ="text-davinci-003",
    prompt = user,
    max_tokens = 1024,
    temperature = 0.5,
    n = 1,
    stop = None)
response = completion.choices[0].text
      
print(response)
