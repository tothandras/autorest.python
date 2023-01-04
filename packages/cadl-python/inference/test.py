from azure.openai.models import CompletionsRequest
from azure.openai.models import CompletionsPrompt1, CompletionsPrompt2, CompletionsPrompt3
from azure.openai._model_base import _deserialize


response1 = CompletionsRequest(prompt=CompletionsPrompt1(name1="name1"))
response2 = CompletionsRequest(prompt=CompletionsPrompt2(name2="name2"))
response3 = CompletionsRequest(prompt=CompletionsPrompt3(name3="name3"))
response = [response1, response2, response3]

# A the following code doesn't work
for item in response:
    result = _deserialize(CompletionsRequest, item)
    if hasattr(result.prompt, "name1"):
        print(result.prompt.name1)
    
    if hasattr(result.prompt, "name2"):
        print(result.prompt.name2)

    if hasattr(result.prompt, "name3"):
        print(result.prompt.name3)

# B the following code  work
# for item in response:
#     result = _deserialize(CompletionsRequest, item)
#     if result.prompt.get("name1"):
#         print(result.prompt.name1)

#     if result.prompt.get("name2"):
#         print(result.prompt.name2)

#     if result.prompt.get("name3"):
#         print(result.prompt.name3)


# C the following code  work
for item in response:
    result = _deserialize(CompletionsRequest, item)
    if result.prompt.get("name1"):
        print(result.prompt.name1)

    if result.prompt.get("name2"):
        print(result.prompt["name2"])

    if result.prompt.get("name3"):
        print(result.prompt["name3"])
