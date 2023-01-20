#!/usr/bin/env /usr/local/bin/python3.9

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Ask GPT
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🤖
# @raycast.argument1 { "type": "text", "placeholder": "Prompt for the model" }
# @raycast.packageName OpenAI GPT Productivity Toolset

# Documentation:
# @raycast.description Ask OpenAI GPT models a question
# @raycast.author Tomasz Sobota
# @raycast.authorURL https://techbranch.net

import json
import requests
import toml
import sys
import os

# -------------------
#  OpenAI PARAMETERS
# -------------------
# modify to your preference

MODEL = "text-davinci-003"  # Most expensive, slow but most capable model
# MODEL = "text-curie-001"      # Less expensive, faster and almost as capable model
# MODEL = "text-ada-001"      # Least expensive, fastest but least capable model

# MAX_TOKENS = 20             # Allow only brief answers, might yield too general answers
MAX_TOKENS = 256              # Allow a rather lenghty answer, encourages more context
# MAX_TOKENS = 1024           # A large allowance for tokens, for long and complex answers

TEMPERATURE = 0.7             # (0.0 -> 1.0) 0 would mean only safest answers

#
# -------------------

#
# Check if the necessary configs exist
#

if not os.path.exists('openai.toml'):
  raise Exception("""
    \n\nSorry, you have to provide the API key in a openai.toml file.\n
    The format should be: \n
    
    apikey="sk-abcdefg"\n
    
    Feel free to try again once you have the file configured
    """)

# ----------------------
# Load the configuration
#

config = toml.load('openai.toml')

# ----------------------------
#  Read the script parameters
#

api_key = config["apikey"]
prompt = sys.argv[1]

# -----------------------------------
#  Prepare the web request to OpenAI
#

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

data = {
  "model": MODEL,
  "prompt": prompt,
  "max_tokens": MAX_TOKENS,
  "temperature": TEMPERATURE
}

# --------------------------------
#  Make the web request to OpenAI
#

try:
  response_raw = requests.post(
    "https://api.openai.com/v1/completions",
    headers=headers,
    data=json.dumps(data)
  )
  response = response_raw.json()
except Exception as err:
  print(f"Encountered a {type(err)} error trying to communicate with OpenAI, here's the traceback")
  print(err)
  raise err

# --------------------------------
#  Parse the response from OpenAI
#

output = ""

if not (response.get("error") is None):
  output = (
    f"Something went wrong with the request, here's the error:\n"
    f"Error: {response.get('error')}"
  )

else:
  answer = response['choices'][0]['text'].replace("\n", "")
  completion_tokens = response['usage']['completion_tokens']
  total_tokens = response['usage']['total_tokens']
  
  output = (
    f"Received an answer from {MODEL}:\n\n"
    f"Prompt: {prompt}\n---\nAnswer: \033[97;40m {answer} \033[0m \n\n"
    f"Used {completion_tokens} completion tokens and {total_tokens} in total"
  )

  #  Save the final output to a file
  #

  try:
    filename_txt = f".ask-gpt/outputs/{response['id']}.txt"
    filename_json = f".ask-gpt/outputs/{response['id']}.json"
    
    # make sure directories exist
    os.makedirs(os.path.dirname(filename_txt), exist_ok=True)
    
    # plain text output
    text_file = open(filename_txt, "w")
    _ = text_file.write(output)
    text_file.close()
    
    # raw json output
    json_file = open(filename_json, "w")
    _ = json_file.write(json.dumps(response))
    json_file.close()

  except Exception as err:
    output = output + f"\nFailed to save the output to a file, here's the error:\n{err}"

# --------------------------
#  Display the final output
#

print(output)
