from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os
def extract(base_url="https://openrouter.ai/api/v1",model="openrouter/free"):
    load_dotenv()
    class Structure(BaseModel):
        full_name: str
        strong_foot: str
        position: str
        nationality: str
        all_clubs: list[str]
    prompt=input("Enter some information about a football player: ")
    client=OpenAI(base_url=base_url,api_key=os.getenv("API_KEY"))
    completion=client.beta.chat.completions.parse(
        model=model,
        messages=[{"role":"user","content":f"Extract information from this text: \"{prompt}\""}],
        response_format=Structure
    )
    return completion.choices[0].message.parsed
if __name__ == "__main__":
    result=extract()
    print("\nExtracted Structured Data:")
    print(result)