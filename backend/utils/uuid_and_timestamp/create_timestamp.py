from datetime import datetime
import os, time

def create_timestamp_function():
  print('=========================================== create_timestamp_function START ===========================================')
  os.environ['TZ'] = 'US/Eastern'
  time.tzset()
  print('=========================================== create_timestamp_function END ===========================================')
  return datetime.now().strftime('%Y-%m-%d %H:%M:%S')