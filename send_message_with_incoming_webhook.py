# import json
# import requests

# webhook_url = 'https://hooks.slack.com/services/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'
# slack_data = {'text': "My first Slack message yay"}

# response = requests.post(
#     webhook_url, data = json.dumps(slack_data),
#     headers={'Content-Type': 'application/json'}
# )

# if response.status_code != 200:
#     raise ValueError(
#         'Request to slack returned an error %s, the response is:\n%s'
#         % (response.status_code, response.text)
# )
# else:
#     print('success')



from slack_sdk.webhook import WebhookClient
url = 'https://hooks.slack.com/services/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'
webhook = WebhookClient(url)

response = webhook.send(text="Hello!")
assert response.status_code == 200
assert response.body == "ok"