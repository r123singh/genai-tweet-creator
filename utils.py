from openai import OpenAI

client = None

current_tweet = ""

def init_client(openai_api_key):
    global client
    if client is None:
        client = OpenAI(api_key=openai_api_key)
    
def generate_tweet(description):
    global current_tweet
    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=1,
        messages=[
            {
                "role":"system",
                "content": f"You are social media expert on Twitter. Write a post based on the context provided: {description}"
            },
            {
                "role": "user",
                "content": "Create tweet"
            }
        ]
    )
    current_tweet = response.choices[0].message.content
    return current_tweet
