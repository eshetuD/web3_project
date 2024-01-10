import openai
from dotenv import load_dotenv
import os
import base64
#Load environment variables from .env file
load_dotenv()

# Access OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")

# Use the OpenAI API key in your code
openai.api_key = openai_api_key



# Read the content of the logo.svg file
with open('logo.svg', 'rb') as logo_file:
    logo_content = logo_file.read()

# Encode the content to base64
encoded_logo = base64.b64encode(logo_content).decode('utf-8')

logo = 'logo.svg'

response = openai.Image.create(
  model="dall-e-3",
  prompt="""
          generate an image with small size logo on top right corner leave blank space for logo
          font family should be 'Times New Roman' font size has to be '16 px', background color is white with thin border color red, there should be space for Name signature and date 
          leave blank space for document body, do not place sample stamp on the image
          be aware that is has to be readable by human that means it has to be in ENGLISH
          No stamp, and No signature know that there is only signature place, do not complicate the image, it has to
          readable no confusion and no meaningless design
        """,
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response['data'][0]['url']

print(image_url)