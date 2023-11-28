import pdb
import os
from  helper_methods import add_message_to_thread, print_final_messages, run_assistant, see_run_steps, wait_for_run
from openai import OpenAI

key=os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=key)


assistant = {
          "created_at":1701145225,
          "id": "asst_W81J8ydY1ZZBFTnEnrmQ2WVC",
          "model":"gpt-4-1106-preview",
          # "tools":"ToolCodeInterpreter(type='code_interpreter')",
          "tools": [{"type": "code_interpreter"}],
          "file_ids":[],
          "metadata":{} ,
          "name":"Math tutor",
          "description":"None",
          "instruction":"You are a personal math tutor. Write and run code to answer math questions.",
          "object":"assistant"
}


thread = {
          "created_at":1701145225,
          "id": "thread_SjIA3mcPj8vZ7MqN8RfHsaLa",
          "metadata":{},
          "object":"thread"
}


# 3 step --> pass message to that thread with user role & content
message = client.beta.threads.messages.create(
    thread_id=thread["id"],
    role="user",
    content= input("Hi, I am your math instructor. feel free to ask any query.\n")
    # content= "I need to solve the equation `4x^2 - 3x + 11 = 14`. Can you help me?"
)


#  4 step --> run the assistant on thread
run = client.beta.threads.runs.create(
  thread_id=thread["id"],
  assistant_id=assistant["id"],
  instructions="Please address the user as Jane Doe. The user has a premium account."
)

#  5 step --> check the run status by retrieve

run = wait_for_run(client, run, thread)

print("status in main " + run.status)

# 6 step --> display the Assistant's response
messages = client.beta.threads.messages.list(
  thread_id=thread["id"]
)

print_final_messages(messages)

# gave another user message 
# updated_content = "could you please show me the steps involve solving the question?"
updated_content = input("Do you have any other query\n")

add_message_to_thread(client,updated_content,thread)

# rerun the assistant with updated content
instruction = "gave answer according to the user response"
run_assistant(client,assistant,instruction,thread)

# wait_for_run(client,run, thread_1)

# repeating step 6 to update the messages, so new generated messages can be printed in the next print statement
messages = client.beta.threads.messages.list(
  thread_id=thread["id"]
)

print_final_messages(messages)

# list run steps
# see_run_steps(thread_1, run, key)
