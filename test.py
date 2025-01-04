import ollama
import json

response = ollama.chat(
    model='llama3.2-vision:11b-instruct-q4_K_M',
    messages=[{
        'role': 'user',
        'content': (
            "Extract the text from the image and represent it as a JSON object. "
            "The JSON object should have keys for 'Known Conditions', 'Allergies', 'Current Medications', "
            "and 'Past Surgeries or Major Treatments'. "
            "Each key's value should be a string or array, as appropriate, based on the text shown. "
            "Do not modify the text, add any extra words, or make any assumptions. "
            "Ensure that the capitalization and spacing of the original text are retained. "
            "If a particular section has multiple lines, format it as a comma-separated list within the JSON string. "
            "For example, if 'Known Conditions' contains 'Chronic Kidney Disease' and 'Hypertension' it should "
            "be represented as string 'Chronic Kidney Disease, Hypertension' "
            "Return only the raw JSON data."
            "Return only a single valid JSON object and do not include any text before or after the object."
        ),
        'images': ['/workspaces/ollama/1.png'],
        'format': 'json'
    }]
)


content = response['message']['content']
try:
    json_data = json.loads(content)
    print(json.dumps(json_data, indent=4))
except json.JSONDecodeError as e:
    print("Error: Could not parse JSON:", e)
    print("Raw content received from Ollama:")
    print(content)