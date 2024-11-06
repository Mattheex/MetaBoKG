import os
from openai import OpenAI


client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Function to call ChatGPT API
def get_chatgpt_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # You can specify "gpt-4" if you have access to it
        messages=[
            {"role": "user", "content": prompt}
        ],
    )
    #print(response)
    return response.choices[0].message.content

# Example usage
prompt = "Write me a RDF schema of mass spectrometre spectra and associated features"
response_text = get_chatgpt_response(prompt)
print(response_text)