import json
import os
import pdb
import requests
from execute_once import key

key=os.getenv('OPENAI_API_KEY')

# query = "why log of any number is less than the original number"

# url = f"http://127.0.0.1:8000/ask_query/{query}"
# header = {
#     "Content-Type": "application/json",
#     # "query": f"{query}"
#     }

# response = requests.get(url,header)

# print(response.text)

file = {"file": open("text_files/about_parveen_shakir.txt", "rb")}

# uploading file to assistant
url_file = "https://api.openai.com/v1/files"
header_file = {
    # "Content-Type": "multipart/form-data",
    "Authorization": f"Bearer {key}",
    
   }

form_data = {
    "purpose": "assistants",
    # "file":f"{file}"
}
# pdb.set_trace()
response_file = requests.post(url=url_file, headers=header_file, data=form_data, files=file)
print(response_file.text)



# getting file list
# file_list = requests.get(url="https://api.openai.com/v1/files", headers={"Authorization": f"Bearer {key}"})

# print(json.loads(file_list.content))




