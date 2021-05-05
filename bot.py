import os
import slack
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter

# Loading the .env file, environment variables
env_path = Path('.') / '.env'
load_dotenv(dotenv_path = env_path)

# Start flask app
app = Flask(__name__)
# Routing the app to ngrok server
slack_event_adapter = SlackEventAdapter(os.environ.get('SLACK_SIGNING_SECRET'),'/slack/events', app)

# Slack Bot token
bot_token = os.environ.get('SLACK_BOT_TOKEN')
client = slack.WebClient(token=bot_token)

# Get the ID of bot
BOT_ID = client.api_call('auth.test')['user_id']

# Used for message_count function
message_counts = {}

# Event listener, if a message is sent in the chat
@slack_event_adapter.on('message')
def message(payload):
  event = payload.get('event', {})
  channel_id = event.get('channel')
  user_id = event.get('user')
  text = event.get('text')

  if BOT_ID != user_id:
    # Add user to count dictionary to track how many messages they've sent
    if user_id in message_counts:
      message_counts[user_id] += 1
    else:
      message_counts[user_id] = 1
    
    client.chat_postMessage(channel=channel_id, text=text)

@app.route('/message-count', methods=['POST'])
def message_count():
  data = request.form
  user_id = data.get('user_id')
  channel_id = data.get('channel_id')
  message_count = message_counts.get(user_id, 0)
  client.chat_postMessage(channel=channel_id, text=f"Messages: {message_count}")
  return Response(), 200

if __name__ == "__main__":
  # Run
  app.run(debug=True)