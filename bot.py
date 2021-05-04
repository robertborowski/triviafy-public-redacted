import os
import slack
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
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

# Event listener, if a message is sent in the chat
@slack_event_adapter.on('message')
def message(payload):
  event = payload.get('event', {})
  channel_id = event.get('channel')
  user_id = event.get('user')
  text = event.get('text')

  if BOT_ID != user_id:
        client.chat_postMessage(channel=channel_id, text=text)


if __name__ == "__main__":
  # Run
  app.run(debug=True)