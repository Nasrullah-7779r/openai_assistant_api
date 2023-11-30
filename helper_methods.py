import asyncio
import time
import requests
from fastapi import status, HTTPException


def add_message_to_thread(client, content, thread):
    message = client.beta.threads.messages.create(
    thread_id=thread["id"],
    role="user",
    content=content
    
    )
    return message  


def run_assistant(client, assistant, instruction, thread):
    run = client.beta.threads.runs.create(
    thread_id=thread["id"],
    assistant_id=assistant["id"],
    instructions=instruction
    )
    return run

def wait_for_run(client, run, thread):
    
    
    print("\nPlease wait, your query is running")
    i = 1
    while run.status != "completed":
        
        # run = await asyncio.to_thread(
        #       client.beta.threads.runs.retrieve(
        #       thread_id=thread["id"],
        #       run_id=run.id)   
        # ) 

        run =  client.beta.threads.runs.retrieve(
              thread_id=thread["id"],
              run_id=run.id
              ) 
       
        if run.status == "failed":
                print("run status is failed")
                exit()
        # print("status in func " + run.status)
        if i == 1:
            print("running assistant.") 
        else:
            print("." * i, end = '')
        
        i=i+1
        # await asyncio.sleep(5)
        # time.sleep(5)
        
        if(i==12):
            return -1   # means its getting more time than usuall

    if run.status == "failed":
          print("run status is failed")
          return None

    return run    


def see_run_steps(thread, run, key):
    id = thread["id"]
    url = f"https://api.openai.com/v1/threads/{id}/runs/{run.id}/steps"

    header = {    
        "Content-Type": "Application/json",
        "Authorization": f"Bearer {key}",
        "OpenAI-Beta": "assistants=v1"
    }

    request = requests.get(url, headers=header)

    print(request.text)


def see_messages(message, key):
    
    url = f"https://api.openai.com/v1/threads/{message.thread_id}/messages"

    header = {    
    "Content-Type": "Application/json",
    "Authorization": f"Bearer {key}",
    "OpenAI-Beta": "assistants=v1"
    
    }

    request = requests.get(url, headers=header)

    print(request.text)   


def print_final_messages(messages):
    # i = 0
    # for message in (messages.data):
        print(messages.data[0].role["assistant"] + ": " + messages.data[0].content[0].text.value)  
        
        # i = i+1
        print("\n")    
