
# import os
# from openai import OpenAI

# key=os.getenv('OPENAI_API_KEY')

# client = OpenAI(api_key=key)




# 1 step --> create assistant
    # assistant = client.beta.assistants.create(
    # name="Math Tutor",
    # instructions="You are a personal math tutor. Write and run code to answer math questions.",
    # tools=[{"type": "code_interpreter"}],
    # model="gpt-4-1106-preview"
    # )

    # 2 step --> create a thread to represent a user
    # thread = client.beta.threads.create()





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




