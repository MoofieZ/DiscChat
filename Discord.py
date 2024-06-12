import requests

auth = "Authentication Token"
text = ""
async def sendMessage(channel_id, message):
    url = f'https://discord.com/api/v10/channels/{channel_id}/messages'
    headers = {
        'Authorization': auth,
        'Content-Type': 'application/json'
    }
    payload = {
        "content": str(message)  
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print("Failed")

sendMessage ("ChannelID", text)