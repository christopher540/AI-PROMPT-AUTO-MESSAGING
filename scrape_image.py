from groq import Groq
import pytesseract
from PIL import Image
import os

def get_options(path,user_input):
    client = Groq(
            api_key=os.environ.get("KEYS")
        )

    #profile=input('Enter profile path: ')
    profile=path
    im = Image.open(profile)
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    text = pytesseract.image_to_string(im, lang='eng+chi_tra')
    chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"""
                    you are a message prompt generator chatbot and your task it 
                    based on the information provided, please create one concise outreach messages targeting this person. 
                    Here’s the information extracted from their profile:
                    {text}
                    
                    Additional context:
                    {user_input}

                    here is the exact example output, just strictly give me the message with not introduction:
                    Hi Christopher, I came across your profile at City University of Hong Kong and was impressed by your interests in Data Analytics and Machine Learning. Would love to connect and discuss potential collaborations.
                    
                    """
                }
            ],
            model="llama3-8b-8192",
        )


    options=chat_completion.choices[0].message.content
    options=options.split('\n')[-1]
    

    return options