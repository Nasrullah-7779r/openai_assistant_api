from fastapi import APIRouter, status, HTTPException
from execute_once import assistant2, thread, client
from helper_methods import print_final_messages, wait_for_run


router = APIRouter(tags=["File Assistant"])

@router.get('/ask_query_from_file/{query}', status_code=status.HTTP_202_ACCEPTED)
async def ask_query(query: str):

# 3 step --> pass message to that thread with user role & content
    message = client.beta.threads.messages.create(
    thread_id=thread["id"],
    role="user",
    content= query
    )

    #  4 step --> run the assistant on thread
    run = client.beta.threads.runs.create(
    thread_id=thread["id"],
    assistant_id=assistant2["id"],
    instructions="Please answer the user query, and if you don't know then just simple say you don't know it"
    )

    #  5 step --> check the run status by retrieve
    run = wait_for_run(client, run, thread)
    if run == None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="run status failed")

    if run == -1:
          raise HTTPException(status_code=status.HTTP_408_REQUEST_TIMEOUT, detail="run has taken more time than usuall")  
   
    # 6 step --> display the Assistant's response
    messages = client.beta.threads.messages.list(
    thread_id=thread["id"]
    )
    # return {"messages":"success"}
    return messages
    # print_final_messages(messages)


