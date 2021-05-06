import os
from slack_sdk import WebClient

# creates a channel named "the-welcome-channel"
def create_channel():
  token = os.environ.get('SLACK_BOT_TOKEN')
  client = WebClient(token=token)
  resp = client.conversations_create(name="the-welcome-channel")


# verifies if "the-welcome-channel" already exists
def channel_exists():
  token = os.environ.get('SLACK_BOT_TOKEN')
  client = WebClient(token=token)

  # grab a list of all the channels in a workspace
  clist = client.conversations_list()
  exists = False
  for k in clist["channels"]:
    print('- - - - - -')
    print(k)
    print('- - - - - -')
    
    # look for the channel in the list of existing channels
    if k['name'] == 'the-welcome-channel':
      exists = True
      break
    
    if exists == False:
      # create the channel since it doesn't exist
      create_channel()

# Create an event listener for "member_joined_channel" events
# Sends a DM to the user who joined the channel
@slack_events_adapter.on("member_joined_channel")
def member_joined_channel(event_data):
  user = event_data['event']['user']
  token = os.environ.get('SLACK_BOT_TOKEN')
  client = WebClient(token=token)
  msg = 'Welcome! Thanks for joining the-welcome-channel'
  client.chat_postMessage(channel=user, text=msg)

#============================================================================
if __name__ == "__main__":
  # Run
  app.run(debug=True)