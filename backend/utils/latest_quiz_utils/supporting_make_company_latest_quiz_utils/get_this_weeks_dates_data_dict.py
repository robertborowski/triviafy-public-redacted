# -------------------------------------------------------------- Imports
from datetime import date, datetime, timedelta

# -------------------------------------------------------------- Main Function
def get_this_weeks_dates_data_dict_function():
  """ Get this weeks dates data in dictionary format """
  print('=========================================== get_this_weeks_dates_data_dict_function START ===========================================')
  
  # ------------------------ Get Today's Date START ------------------------
  # Today's date
  today_date = date.today()
  # Today's date, day of week
  today_day_of_week = today_date.strftime('%A')
  # ------------------------ Get Today's Date END ------------------------


  # ------------------------ Get This Week's Dates START ------------------------
  # Plus 1 day
  today_date_plus_one = date.today() + timedelta(days=1)
  today_day_of_week_plus_one = today_date_plus_one.strftime('%A')

  # Plus 2 day
  today_date_plus_two = date.today() + timedelta(days=2)
  today_day_of_week_plus_two = today_date_plus_two.strftime('%A')

  # Plus 3 day
  today_date_plus_three = date.today() + timedelta(days=3)
  today_day_of_week_plus_three = today_date_plus_three.strftime('%A')

  # Plus 4 day
  today_date_plus_four = date.today() + timedelta(days=4)
  today_day_of_week_plus_four = today_date_plus_four.strftime('%A')

  # Plus 5 day
  today_date_plus_five = date.today() + timedelta(days=5)
  today_day_of_week_plus_five = today_date_plus_five.strftime('%A')

  # Plus 6 day
  today_date_plus_six = date.today() + timedelta(days=6)
  today_day_of_week_plus_six = today_date_plus_six.strftime('%A')
  # ------------------------ Get This Week's Dates END ------------------------


  # ------------------------ This Week's Dates Dict START ------------------------
  this_week_dates_dict = {
    today_day_of_week : today_date.strftime('%Y-%m-%d'),
    today_day_of_week_plus_one : today_date_plus_one.strftime('%Y-%m-%d'),
    today_day_of_week_plus_two : today_date_plus_two.strftime('%Y-%m-%d'),
    today_day_of_week_plus_three : today_date_plus_three.strftime('%Y-%m-%d'),
    today_day_of_week_plus_four : today_date_plus_four.strftime('%Y-%m-%d'),
    today_day_of_week_plus_five : today_date_plus_five.strftime('%Y-%m-%d'),
    today_day_of_week_plus_six : today_date_plus_six.strftime('%Y-%m-%d'),
  }
  # ------------------------ This Week's Dates Dict END ------------------------

  print('returning this_week_dates_dict')
  print(this_week_dates_dict)
  print('=========================================== get_this_weeks_dates_data_dict_function END ===========================================')
  return this_week_dates_dict