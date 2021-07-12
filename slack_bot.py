import requests
 
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-2148803419396-2166465567280-X4yzFZX1CZ1GFVecrOKYXZeP"
 
post_message(myToken,"#stock","Hello world!")
