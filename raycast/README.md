## Script installation

1. Add the `ask-gpt.py` script to a directory of your choice, be it an already existing scripts directory or a new one. 
  > If it's a new directory, you'll have to tell Raycast about it 
  - In Raycast, go to `Extensions`, then `scripts`, click the `Add` icon, `pick script directory` and point it to the directory you chose.
2. Create a new file in the scripting directory and name it `openai.toml`. Put your API key in it like `apikey = "sk-abcde"`
3. This script references `#!/usr/bin/env python3` for Python, but you might want to repoint it at an installation that works for you.

You should be good to go. Fire up Raycast, type `ask` and `<tab>` to start filling the prompt argument.

Feel free to modify the script, there's plenty to adjust to your liking. 

The script is commented in a way that should help navigate it pretty easily.

Most notable things which you might want to tweak are the constants around the top of the script, these specify the `model`, `tokens` and `temperature` - I encourage you to read a bit more about these in the OpenAI documentation. 

All outputs are saved to files under `.ask-gpt/outputs/` for your future reference.
