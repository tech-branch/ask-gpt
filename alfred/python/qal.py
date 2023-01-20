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
request_bodies = [
    {
        "model": os.getenv('model'),
        "prompt": prompt,
        "max_tokens": int(os.getenv('maxtokens')),
        "temperature": float(os.getenv('temperature'))
    },
    {
        "model": os.getenv('model'),
        "prompt": prompt,
        "max_tokens": int(os.getenv('maxtokens_expensive')),
        "temperature": float(os.getenv('temperature'))
    },
    {
        "model": os.getenv('model_expensive'),
        "prompt": prompt,
        "max_tokens": int(os.getenv('maxtokens')),
        "temperature": float(os.getenv('temperature'))
    },
    {
        "model": os.getenv('model_expensive'),
        "prompt": prompt,
        "max_tokens": int(os.getenv('maxtokens_expensive')),
        "temperature": float(os.getenv('temperature'))
    },
]
responses = []
# Send request to GPT-3 completion API
for data in request_bodies:
    try:
        response = requests.post(
            "https://api.openai.com/v1/completions",
            headers=headers,
            data=json.dumps(data)
        )
        response_json = response.json()
        response_object = {
            "model-and-tokens": f"{response_json['model']} @ {response_json['usage']['completion_tokens']} tokens",
            "response": response_json["choices"][0]["text"].replace("\n", "")
        }
        responses.append(response_object)
    except:
        pass

items = []
for idx, response in enumerate(responses):
    items.append({
        "uid": str(idx),
        "title": response["model-and-tokens"],
        "subtitle": response["response"],
        "arg": response["response"],
        "text": {
            "copy": response["response"],
            "largetype": response["response"]
        }
    })

# Print response
print(json.dumps({
    "variables": {
	    "prompt": prompt,
        "responses": json.dumps(responses, indent=2)
    },
    "items": items
}))

# Why do trees have so many branches?
