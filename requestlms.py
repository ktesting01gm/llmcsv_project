from openai import OpenAI

# Initialize LM Studio client

BASEURL = "http://localhost:1234/v1"
APIKEY = "lm-studio"
MODEL = "qwen2.5-7b-instruct"
client = OpenAI(base_url=BASEURL, api_key=APIKEY)



# Call the LLM Studio function
SYSTEM_PROMPT = "You are a helpful assistant that can answer questions about history, science, people, places, or concepts. Answer the following question with a person, name, place, date, etc. that answers the question. Output only the answer in square brackets so it is easy to read. Discard all the other information except the answer and omit punctuation or escape symbols. Feel free to think through the answer before you respond. If you do not know, respond with: [I don't know]"

PROMPT = "The last time la dodgers won the world series?"



response = client.chat.completions.create(
    model = MODEL,
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": PROMPT"}],
        temperature=0.7
)

print(completion.choices[0].message)

