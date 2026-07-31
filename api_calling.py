from google import genai
from  dotenv import load_dotenv
import os
load_dotenv()
 
API_key =os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key= API_key)
def note_generator(images):
    prompt = """Perform a comprehensive forensic analysis of the attached image.
    Identify the primary subject matter, technical composition, and underlying context. 
 Provide a detailed descriptive synthesis followed by a structured technical briefing using clear, 
 professional terminology. Deliver the entire response in plain text format without the use of markdown characters."""
   
    response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=[images , prompt]
)
    return response.text
    
def quize_generator(images , info):
    prompt =f"Generate 25 quizzes with answers based on {info} and avoid markdown"
    response = client.models.generate_content(
    model="gemini-3.1-flash-lite-preview",
    contents=[images , prompt]
)
    return response.text
    


