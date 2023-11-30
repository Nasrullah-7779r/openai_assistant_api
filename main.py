from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from routers import file_assistant, math_tutor

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/file_assistant", response_class=HTMLResponse)
def file_assistnt(request: Request):
    return templates.TemplateResponse("file_assistant.html", {"request": request})


# @app.get('/')
# def test():
#     return {"test":"success"}

app.include_router(router=math_tutor.router)
app.include_router(router=file_assistant.router)

# To debug FastAPI
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)


# print_final_messages(response)

# gave another user message 
# updated_content = "could you please show me the steps involve solving the question?"
# updated_content = input("Do you have any other query\n")

# add_message_to_thread(client,updated_content,thread)

# # rerun the assistant with updated content
# instruction = "gave answer according to the user response"
# run_assistant(client,assistant,instruction,thread)

# # wait_for_run(client,run, thread_1)

# # repeating step 6 to update the messages, so new generated messages can be printed in the next print statement
# messages = client.beta.threads.messages.list(
#   thread_id=thread["id"]
# )

# print_final_messages(messages)

# list run steps
# see_run_steps(thread_1, run, key)
