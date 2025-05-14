import csv
import requests
from io import StringIO

# Function to call the LLM and get a response
def call_llm(question, api_key):
    # Replace this URL and headers with your actual LLM API endpoint and headers
    url = "https://api.example.com/v1/complete"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    data = {
        "prompt": question,
        "model": "your_model_name"
    }
    
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json().get("result", "")
    else:
        raise Exception(f"API request failed with status code {response.status_code}")

# Load test data
input_csv_path = 'test.csv'
output_csv_path = 'result.csv'

# Read the input CSV file
with open(input_csv_path, mode='r', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    
    # Prepare header for output CSV
    headers = ['Question', 'Expected Answer', 'LLM Response']
    
    # Open a new CSV file to write the results
    with open(output_csv_path, mode='w', encoding='utf-8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=headers)
        
        # Write headers to the output CSV
        writer.writeheader()
        
        for row in reader:
            question = row['Question']
            expected_answer = row['Expected Answer']
            
            # Call LLM and get response
            llm_response = call_llm(question, api_key='your_api_key_here')
            
            # Write the results to the output CSV
            writer.writerow({
                'Question': question,
                'Expected Answer': expected_answer,
                'LLM Response': llm_response
            })

print(f"Results saved to {output_csv_path}")
