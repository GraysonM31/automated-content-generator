# Imports
import re
from g4f.client import Client
from g4f.Provider import You

# Asyncio Fix
import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Format Text
def parseText(text):
    removedFormatting = re.sub(r'#### |[*]{2}', '', text)
    removedCitations = re.sub(r'\[\[\d+\]\]\(https?:\/\/.*?\)', '', removedFormatting)
    removedSpacing = re.sub(r'\s+\.', '.', removedCitations)
    removedNewLines = re.sub(r'\n\s*\n', '\n', removedSpacing).strip()
    cleanedText = removedNewLines
    return cleanedText

# Get AI Response
def askGPT(input):
    client = Client()
    prompt = "Give me 5 fun facts about the following topic: " + input
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  
        provider=You, 
        messages=[{"role": "user", "content": prompt}],
      
    )
    return parseText(response.choices[0].message.content)
