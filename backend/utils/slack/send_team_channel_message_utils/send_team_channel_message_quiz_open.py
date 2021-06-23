# -------------------------------------------------------------- Imports
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


# -------------------------------------------------------------- Main Function
def send_team_channel_message_quiz_open_function(slack_bot_token, user_channel, quiz_end_day_of_week, quiz_end_time):
  print('=========================================== send_team_channel_message_quiz_open_function START ===========================================')

  output_text = f":tada: Hi <!here>, your team's weekly Triviafy quiz is now OPEN!\n:hourglass_flowing_sand: Quiz closes on {quiz_end_day_of_week}, {quiz_end_time}.\n:white_check_mark: Login and submit your answers at: https://triviafy.com/"

  # Set up client with the USER's Bot Access Token. NOT your's from the environment variable
  client = WebClient(token=slack_bot_token)
  # Have the bot send a test message to the channel
  try:
    response = client.chat_postMessage(
      channel=user_channel,
      text=output_text
    )
    print('sent slack message')
  except SlackApiError as e:
    print('did not send message to slack channel')
    print(e.response['error'])

  print('=========================================== send_team_channel_message_quiz_open_function END ===========================================')
  return True, output_text