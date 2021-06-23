# -------------------------------------------------------------- Imports
from datetime import date, timedelta
import os, time

# -------------------------------------------------------------- Main Function
def free_trial_period_start_end_function():
  print('=========================================== free_trial_period_start_end_function START ===========================================')

  os.environ['TZ'] = 'US/Eastern'
  time.tzset()

  # ------------------------ Free Trial Periods START ------------------------
  free_trial_start_timestamp = date.today()
  free_trial_start_timestamp = free_trial_start_timestamp.strftime('%Y-%m-%d %H:%M:%S')


  free_trial_end_timestamp = date.today() + timedelta(days=30)
  free_trial_end_timestamp = free_trial_end_timestamp.strftime('%Y-%m-%d %H:%M:%S')
  # ------------------------ Free Trial Periods END ------------------------


  print('returning free trial start and end dates')
  print('=========================================== free_trial_period_start_end_function END ===========================================')
  return free_trial_start_timestamp, free_trial_end_timestamp