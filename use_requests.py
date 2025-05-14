import json
import requests
from requests.auth import HTTPBasicAuth



def request_llama(number):

    URL = "https://ml-hub.ameriadev.de/v1/chat/completions"
    BASIC_AUTH = HTTPBasicAuth('robukhovskyi', r'LR%aMB7Vom@m5bjf2TVa')
    PROMPT = "What is the capital of Germany?"
    PAYLOAD = {
        "model": "casperhansen/llama-3-70b-instruct-awq",
        "messages": [
                    {
                    "role": "user",
                    "content": PROMPT
                }],
        "stream": False
    }

    response = requests.post(URL, auth=BASIC_AUTH, data=json.dumps(PAYLOAD), verify=False)

    counter = 0
    
    for i in range(number):
        counter += 1
        if response.status_code == 200:
            response_text = response.text
            data = json.loads(response_text)            
            print(counter), print(data), print("\n" * 2)
        else:
            return "Something went wrong", response.status_code, response.text
    
    
def main(number):
    request_llama(number)
        
        
         

if __name__ == "__main__":
    main(5)