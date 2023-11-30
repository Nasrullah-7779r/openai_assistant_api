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

assistant_file_object = {
    "object": "file",
    "id": "file-CKtmztxbquCB5dTop4Y3EpV2",
    "purpose": "assistants",
    "filename": "about_nazia.txt",
    "bytes": 2381,
    "created_at": 1701244028, 
    "status": "processed",
    "status_details": None
}

assistant_file_object_2 = {
  "object": "file",
  "id": "file-XIlZkI1dOxYcguQEZzYq7fnX",
  "purpose": "assistants",
  "filename": "about_parveen_shakir.txt",
  "bytes": 3546,
  "created_at": 1701256113,
  "status": "processed",
  "status_details": None
}

# getting file list
# file_list = requests.get(url="https://api.openai.com/v1/files", headers={"Authorization": f"Bearer {key}"})

# print(json.loads(file_list.content))




