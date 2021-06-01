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


  # ------------------------ If Today is Monday START ------------------------
  if today_day_of_week == 'Monday':
    # Monday
    monday_date = date.today()
    monday_day_of_week = monday_date.strftime('%A')
    # Tuesday
    tuesday_date = date.today() + timedelta(days=1)
    tuesday_day_of_week = tuesday_date.strftime('%A')
    # Wednesday
    wednesday_date = date.today() + timedelta(days=2)
    wednesday_day_of_week = wednesday_date.strftime('%A')
    # Thursday
    thursday_date = date.today() + timedelta(days=3)
    thursday_day_of_week = thursday_date.strftime('%A')
    # Friday
    friday_date = date.today() + timedelta(days=4)
    friday_day_of_week = friday_date.strftime('%A')
    # Saturday
    saturday_date = date.today() + timedelta(days=5)
    saturday_day_of_week = saturday_date.strftime('%A')
    # Sunday
    sunday_date = date.today() + timedelta(days=6)
    sunday_day_of_week = sunday_date.strftime('%A')
  # ------------------------ If Today is Monday END ------------------------
  # ------------------------ If Today is Tuesday START ------------------------
  elif today_day_of_week == 'Tuesday':
    # Monday
    monday_date = date.today() - timedelta(days=1)
    monday_day_of_week = monday_date.strftime('%A')
    # Tuesday
    tuesday_date = date.today()
    tuesday_day_of_week = tuesday_date.strftime('%A')
    # Wednesday
    wednesday_date = date.today() + timedelta(days=1)
    wednesday_day_of_week = wednesday_date.strftime('%A')
    # Thursday
    thursday_date = date.today() + timedelta(days=2)
    thursday_day_of_week = thursday_date.strftime('%A')
    # Friday
    friday_date = date.today() + timedelta(days=3)
    friday_day_of_week = friday_date.strftime('%A')
    # Saturday
    saturday_date = date.today() + timedelta(days=4)
    saturday_day_of_week = saturday_date.strftime('%A')
    # Sunday
    sunday_date = date.today() + timedelta(days=5)
    sunday_day_of_week = sunday_date.strftime('%A')
  # ------------------------ If Today is Tuesday END ------------------------
  # ------------------------ If Today is Wednesday START ------------------------
  elif today_day_of_week == 'Wednesday':
    # Monday
    monday_date = date.today() - timedelta(days=2)
    monday_day_of_week = monday_date.strftime('%A')
    # Tuesday
    tuesday_date = date.today() - timedelta(days=1)
    tuesday_day_of_week = tuesday_date.strftime('%A')
    # Wednesday
    wednesday_date = date.today()
    wednesday_day_of_week = wednesday_date.strftime('%A')
    # Thursday
    thursday_date = date.today() + timedelta(days=1)
    thursday_day_of_week = thursday_date.strftime('%A')
    # Friday
    friday_date = date.today() + timedelta(days=2)
    friday_day_of_week = friday_date.strftime('%A')
    # Saturday
    saturday_date = date.today() + timedelta(days=3)
    saturday_day_of_week = saturday_date.strftime('%A')
    # Sunday
    sunday_date = date.today() + timedelta(days=4)
    sunday_day_of_week = sunday_date.strftime('%A')
  # ------------------------ If Today is Wednesday END ------------------------
  # ------------------------ If Today is Thursday START ------------------------
  elif today_day_of_week == 'Thursday':
    # Monday
    monday_date = date.today() - timedelta(days=3)
    monday_day_of_week = monday_date.strftime('%A')
    # Tuesday
    tuesday_date = date.today() - timedelta(days=2)
    tuesday_day_of_week = tuesday_date.strftime('%A')
    # Wednesday
    wednesday_date = date.today() - timedelta(days=1)
    wednesday_day_of_week = wednesday_date.strftime('%A')
    # Thursday
    thursday_date = date.today()
    thursday_day_of_week = thursday_date.strftime('%A')
    # Friday
    friday_date = date.today() + timedelta(days=1)
    friday_day_of_week = friday_date.strftime('%A')
    # Saturday
    saturday_date = date.today() + timedelta(days=2)
    saturday_day_of_week = saturday_date.strftime('%A')
    # Sunday
    sunday_date = date.today() + timedelta(days=3)
    sunday_day_of_week = sunday_date.strftime('%A')
  # ------------------------ If Today is Thursday END ------------------------
  # ------------------------ If Today is Friday START ------------------------
  elif today_day_of_week == 'Friday':
    # Monday
    monday_date = date.today() - timedelta(days=4)
    monday_day_of_week = monday_date.strftime('%A')
    # Tuesday
    tuesday_date = date.today() - timedelta(days=3)
    tuesday_day_of_week = tuesday_date.strftime('%A')
    # Wednesday
    wednesday_date = date.today() - timedelta(days=2)
    wednesday_day_of_week = wednesday_date.strftime('%A')
    # Thursday
    thursday_date = date.today() - timedelta(days=1)
    thursday_day_of_week = thursday_date.strftime('%A')
    # Friday
    friday_date = date.today()
    friday_day_of_week = friday_date.strftime('%A')
    # Saturday
    saturday_date = date.today() + timedelta(days=1)
    saturday_day_of_week = saturday_date.strftime('%A')
    # Sunday
    sunday_date = date.today() + timedelta(days=2)
    sunday_day_of_week = sunday_date.strftime('%A')
  # ------------------------ If Today is Friday END ------------------------
  # ------------------------ If Today is Saturday START ------------------------
  elif today_day_of_week == 'Saturday':
    # Monday
    monday_date = date.today() - timedelta(days=5)
    monday_day_of_week = monday_date.strftime('%A')
    # Tuesday
    tuesday_date = date.today() - timedelta(days=4)
    tuesday_day_of_week = tuesday_date.strftime('%A')
    # Wednesday
    wednesday_date = date.today() - timedelta(days=3)
    wednesday_day_of_week = wednesday_date.strftime('%A')
    # Thursday
    thursday_date = date.today() - timedelta(days=2)
    thursday_day_of_week = thursday_date.strftime('%A')
    # Friday
    friday_date = date.today() - timedelta(days=1)
    friday_day_of_week = friday_date.strftime('%A')
    # Saturday
    saturday_date = date.today()
    saturday_day_of_week = saturday_date.strftime('%A')
    # Sunday
    sunday_date = date.today() + timedelta(days=1)
    sunday_day_of_week = sunday_date.strftime('%A')
  # ------------------------ If Today is Saturday END ------------------------
  # ------------------------ If Today is Sunday START ------------------------
  elif today_day_of_week == 'Sunday':
    # Monday
    monday_date = date.today() - timedelta(days=6)
    monday_day_of_week = monday_date.strftime('%A')
    # Tuesday
    tuesday_date = date.today() - timedelta(days=5)
    tuesday_day_of_week = tuesday_date.strftime('%A')
    # Wednesday
    wednesday_date = date.today() - timedelta(days=4)
    wednesday_day_of_week = wednesday_date.strftime('%A')
    # Thursday
    thursday_date = date.today() - timedelta(days=3)
    thursday_day_of_week = thursday_date.strftime('%A')
    # Friday
    friday_date = date.today() - timedelta(days=2)
    friday_day_of_week = friday_date.strftime('%A')
    # Saturday
    saturday_date = date.today() - timedelta(days=1)
    saturday_day_of_week = saturday_date.strftime('%A')
    # Sunday
    sunday_date = date.today()
    sunday_day_of_week = sunday_date.strftime('%A')
  # ------------------------ If Today is Sunday END ------------------------

  


  # ------------------------ This Week's Dates Dict START ------------------------
  this_week_dates_dict = {
    'Monday' : monday_date.strftime('%Y-%m-%d'),
    'Tuesday' : tuesday_date.strftime('%Y-%m-%d'),
    'Wednesday' : wednesday_date.strftime('%Y-%m-%d'),
    'Thursday' : thursday_date.strftime('%Y-%m-%d'),
    'Friday' : friday_date.strftime('%Y-%m-%d'),
    'Saturday' : saturday_date.strftime('%Y-%m-%d'),
    'Sunday' : sunday_date.strftime('%Y-%m-%d')
  }
  # ------------------------ This Week's Dates Dict END ------------------------

  print('returning this_week_dates_dict')
  print(this_week_dates_dict)
  print('=========================================== get_this_weeks_dates_data_dict_function END ===========================================')
  return this_week_dates_dict