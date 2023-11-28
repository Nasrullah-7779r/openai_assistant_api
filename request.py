import requests


query = "why log of any number is less than the original number"

url = f"http://127.0.0.1:8000/ask_query/{query}"
header = {
    "Content-Type": "application/json",
    # "query": f"{query}"
    }

response = requests.get(url,header)

print(response.text)