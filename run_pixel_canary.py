"""
Interactive Terminal Client for stealth/pixel-canary via Vercel AI Gateway.
Zero external dependencies (uses standard library urllib).
"""

import os
import sys
import json
import urllib.request
import urllib.error

API_URL = "https://ai-gateway.vercel.sh/v1/chat/completions"
MODEL_ID = "stealth/pixel-canary"

def stream_chat(prompt: str, token: str):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }
    
    payload = {
        "model": MODEL_ID,
        "messages": [
            {"role": "system", "content": "You are Pixel Canary, an elite coding and systems engineering assistant."},
            {"role": "user", "content": prompt}
        ],
        "stream": True,
        "temperature": 0.2
    }
    
    req = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers=headers,
        method="POST"
    )
    
    try:
        with urllib.request.urlopen(req) as resp:
            print("\n--- [Pixel Canary Stream] ---\n")
            for line in resp:
                decoded_line = line.decode("utf-8").strip()
                if not decoded_line or decoded_line == "data: [DONE]":
                    continue
                if decoded_line.startswith("data: "):
                    raw_json = decoded_line[6:]
                    try:
                        chunk = json.loads(raw_json)
                        choices = chunk.get("choices", [])
                        if choices:
                            delta = choices[0].get("delta", {})
                            content = delta.get("content", "")
                            if content:
                                sys.stdout.write(content)
                                sys.stdout.flush()
                    except json.JSONDecodeError:
                        continue
            print("\n\n--- [End of Stream] ---\n")
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8", errors="replace")
        print(f"\n[HTTP Error {e.code}]: {error_body}")
    except Exception as e:
        print(f"\n[Connection Error]: {e}")

def main():
    token = os.environ.get("VERCEL_AI_GATEWAY_TOKEN") or os.environ.get("AI_GATEWAY_API_KEY")
    
    if not token:
        print("=" * 60)
        print("Pixel Canary Gateway Authentication")
        print("=" * 60)
        print("No VERCEL_AI_GATEWAY_TOKEN detected in environment.")
        token = input("Enter your Vercel AI Gateway Token / API Key: ").strip()
        if not token:
            print("Token is required to route requests through the gateway.")
            sys.exit(1)
            
    print(f"\nConnected to gateway targeting: {MODEL_ID}")
    print("Type your prompt below (or 'exit' / 'quit' to stop).\n")
    
    while True:
        try:
            prompt = input("You > ").strip()
            if not prompt:
                continue
            if prompt.lower() in ("exit", "quit"):
                print("Closing session.")
                break
            stream_chat(prompt, token)
        except (KeyboardInterrupt, EOFError):
            print("\nSession terminated.")
            break

if __name__ == "__main__":
    main()
