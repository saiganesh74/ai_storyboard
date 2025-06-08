from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_storyboard(scene_description):
    prompt = f"""
You are a storyboard artist. Convert the following scene into 6 short storyboard frames:
Scene: {scene_description}
Each frame should be 1-2 sentences only.
"""

    response = client.chat.completions.create(
        model="gpt-4", 
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=400,
        temperature=0.7
    )

    return response.choices[0].message.content
