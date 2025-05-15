import csv
from openai import OpenAI


# Initialize LM Studio client

input_cvs_path = "test.csv"
output_cvs_path = "result.csv"

class LlmData:
    BASEURL = "http://localhost:1234/v1"
    APIKEY = "lm-studio"
    MODEL_1 = "qwen2.5-7b-instruct"
    MODEL_2 = "gemma-3-12b-it"
    client = OpenAI(base_url=BASEURL, api_key=APIKEY)
    SYSTEM_PROMPT = "You are a helpful assistant that can answer questions about history, science, people, places, or concepts. Answer the following question with a person, name, place, date, etc. that answers the question. Output only the answer and put it in double quotes and square brackets as follows [\"answer\"]. Discard all the other information except the answer and omit punctuation or escape symbols. Feel free to think through the answer before you respond. If you do not know, respond with: I don't know."
    PROMPT = "where does the movie the sound of music take place?"
 

# Make the LLM call
def call_llm(question):
    response = LlmData.client.chat.completions.create(
        model=LlmData.MODEL_2,
        messages=[
        {"role": "system", "content": LlmData.SYSTEM_PROMPT},
        {"role": "user", "content": question}
        ]
    )
    
    try:
        return response.choices[0].message.content
    except Exception:
        print('Failed to forward or retreive the request.')
        

# Fill the output CSV
def csvprocess(inputcsv, outputcsv):
    
    with open(inputcsv, mode='r', encoding='utf-8') as infile, \
        open(outputcsv, mode='w', newline='', encoding='utf-8') as outfile:

        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['result']
    
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            question = row['question']
            answer = row.get('answer', '')  # Keep the original answer if available
            airesponse = call_llm(question)  # Get response from LLM model
            writer.writerow({
                'question': question,
                'answer': answer,
                'result': airesponse
            })

    print(f"Results have been written to {outputcsv}.")
    return outputcsv
    

if __name__ == "__main__":

    csvprocess(input_cvs_path, output_cvs_path)
    



