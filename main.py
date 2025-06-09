import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
def main():
    args = sys.argv[1:]
    if not args:
        print("Not argument")
        sys.exit(1)
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    user_prompt = " ".join(args)
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]),]
    response=generateContent(client,messages)
    if "--verbose" in args:
        verbose(messages,response)
def generateContent(client,messages):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages
    )
    print(response.text)
    return response
def verbose(messages,response):
    print(f"User prompt: {messages}")
    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)
if __name__ == "__main__":
    main()