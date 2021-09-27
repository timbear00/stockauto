import requests
 
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-2148803419396-2166465567280-TWmTgUrWJ7T9gdcd7L6tbF2R"
 
post_message(myToken,"#stock","Hello world!")
