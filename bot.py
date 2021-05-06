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
welcome_messages = {}

class WelcomeMessage:
  START_TEXT = {
    'type': 'section',
    'text': {
      'type': 'mrkdwn',
      'text': (
        'Welcome to this awesome channel! \n\n'
        '*Get started by completing the tasks!*'
      )
    }
  }

  DIVIDER = {
    'type': 'divider'
  }

  def __init__(self, channel, user):
    self.channel = channel
    self.user = user
    self.icon_emoji = ':robot_face:'
    self.timestamp = ''
    self.completed = False
  
  def get_message(self):
    return {
      'ts': self.timestamp,
      'channel': self.channel,
      'username': 'Welcome Robot!',
      'icon_emoji': self.icon_emoji,
      'blocks': [
        self.START_TEXT,
        self.DIVIDER,
        self._get_reaction_task()
      ]
    }

  def _get_reaction_task(self):
    checkmark = ':white_check_mark:'
    if not self.completed:
      checkmark = ':white_large_square:'

    text = f'{checkmark} *React to this message!*'

    return {
      'type': 'section',
      'text': {
        'type': 'mrkdwn',
        'text': text
      }
    }
  
def send_welcome_message(channel, user):
  welcome = WelcomeMessage(channel, user)
  message = welcome.get_message()
  response = client.chat_postMessage(**message)
  welcome.timestamp = response['ts']

  if channel not in welcome_messages:
    welcome_messages[channel] = {}
  welcome_messages[channel][user] = welcome
  

# Event listener, if a message is sent in the chat
@slack_event_adapter.on('message')
def message(payload):
  event = payload.get('event', {})
  channel_id = event.get('channel')
  user_id = event.get('user')
  text = event.get('text')

  if user_id != None and BOT_ID != user_id:
    # Add user to count dictionary to track how many messages they've sent
    if user_id in message_counts:
      message_counts[user_id] += 1
    else:
      message_counts[user_id] = 1

    if text.lower() == 'start':
      send_welcome_message(f'@{user_id}', user_id)
    
    #client.chat_postMessage(channel=channel_id, text=text)

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