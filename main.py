import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
import argparse

# Check if the correct number of arguments is passed (script name + 1 argument)
if len(sys.argv) < 2:
    print("Usage: python3 main.py <question>")
    sys.exit(1)

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# --- PARSER DES ARGUMENTS ---
parser = argparse.ArgumentParser(description="Query Gemini via CLI")
parser.add_argument("prompt", nargs="+", help="Your question to Gemini")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()



client = genai.Client(api_key=api_key)
user_prompt = args.prompt

if args.verbose:
    print(f"User prompt: {user_prompt}")

#messages = [
 #   types.Content(role="user", parts=[types.Part(text=user_prompt)]),
#]


response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=user_prompt)


print(response.text)

if args.verbose and hasattr(response, "usage_metadata"):
    metadata = response.usage_metadata
    print(f"Prompt tokens: {metadata.prompt_token_count}")
    print(f"Response tokens: {metadata.candidates_token_count}")
#print("Prompt tokens: " + str(response.usage_metadata.prompt_token_count))
#print ("Response tokens:")

