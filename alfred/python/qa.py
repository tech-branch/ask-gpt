import json
import requests
import sys
import os

# Get API key
api_key = os.getenv('apikey')

# Define prompt
prompt = sys.argv[1]

# Define request headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
}

# Define request body
data = {
    "model": os.getenv('model'),
    "prompt": prompt,
    "max_tokens": int(os.getenv('maxtokens')),
    "temperature": float(os.getenv('temperature'))
}

# Send request to GPT-3 completion API
response = requests.post(
    "https://api.openai.com/v1/completions",
    headers=headers,
    data=json.dumps(data)
)

clean_response = response.json()["choices"][0]["text"].replace("\n", "")

# Print response
print(json.dumps({
    "variables": {
	    "prompt": prompt,
        "response": clean_response
    },
    "items": [
        {
            "uid": "1",
            "title": "Curie replied:",
            "subtitle": clean_response,
            "arg": clean_response,
            "text": {
                "copy": clean_response,
                "largetype": clean_response
            }
        }
    ]
}))
