# -------------------------------------------------------------- Imports
from datetime import date, timedelta

# -------------------------------------------------------------- Main Function
def get_upcoming_week_dates_data_dict_function():
  print('=========================================== get_upcoming_week_dates_data_dict_function START ===========================================')
  
  # ------------------------ Get Today's Date START ------------------------
  # Today's date
  today_date = date.today()
  # Today's date, day of week
  today_day_of_week = today_date.strftime('%A')
  # ------------------------ Get Today's Date END ------------------------


  # ------------------------ If Today is Sunday START ------------------------
  if today_day_of_week == 'Sunday':
    # Sunday
    sunday_date = date.today()
    # Monday
    monday_date = date.today() + timedelta(days=1)
    # Tuesday
    tuesday_date = date.today() + timedelta(days=2)
    # Wednesday
    wednesday_date = date.today() + timedelta(days=3)
    # Thursday
    thursday_date = date.today() + timedelta(days=4)
    # Friday
    friday_date = date.today() + timedelta(days=5)
    # Saturday
    saturday_date = date.today() + timedelta(days=6)
  # ------------------------ If Today is Sunday END ------------------------
  # ------------------------ If Today is Monday START ------------------------
  if today_day_of_week == 'Monday':
    # Sunday
    sunday_date = date.today() - timedelta(days=1)
    # Monday
    monday_date = date.today()
    # Tuesday
    tuesday_date = date.today() + timedelta(days=1)
    # Wednesday
    wednesday_date = date.today() + timedelta(days=2)
    # Thursday
    thursday_date = date.today() + timedelta(days=3)
    # Friday
    friday_date = date.today() + timedelta(days=4)
    # Saturday
    saturday_date = date.today() + timedelta(days=5)
  # ------------------------ If Today is Monday END ------------------------
  # ------------------------ If Today is Tuesday START ------------------------
  if today_day_of_week == 'Tuesday':
    # Sunday
    sunday_date = date.today() - timedelta(days=2)
    # Monday
    monday_date = date.today() - timedelta(days=1)
    # Tuesday
    tuesday_date = date.today()
    # Wednesday
    wednesday_date = date.today() + timedelta(days=1)
    # Thursday
    thursday_date = date.today() + timedelta(days=2)
    # Friday
    friday_date = date.today() + timedelta(days=3)
    # Saturday
    saturday_date = date.today() + timedelta(days=4)
  # ------------------------ If Today is Tuesday END ------------------------
  # ------------------------ If Today is Wednesday START ------------------------
  if today_day_of_week == 'Wednesday':
    # Sunday
    sunday_date = date.today() - timedelta(days=3)
    # Monday
    monday_date = date.today() - timedelta(days=2)
    # Tuesday
    tuesday_date = date.today() - timedelta(days=1)
    # Wednesday
    wednesday_date = date.today()
    # Thursday
    thursday_date = date.today() + timedelta(days=1)
    # Friday
    friday_date = date.today() + timedelta(days=2)
    # Saturday
    saturday_date = date.today() + timedelta(days=3)
  # ------------------------ If Today is Wednesday END ------------------------
  # ------------------------ If Today is Thursday START ------------------------
  if today_day_of_week == 'Thursday':
    # Sunday
    sunday_date = date.today() - timedelta(days=4)
    # Monday
    monday_date = date.today() - timedelta(days=3)
    # Tuesday
    tuesday_date = date.today() - timedelta(days=2)
    # Wednesday
    wednesday_date = date.today() - timedelta(days=1)
    # Thursday
    thursday_date = date.today()
    # Friday
    friday_date = date.today() + timedelta(days=1)
    # Saturday
    saturday_date = date.today() + timedelta(days=2)
  # ------------------------ If Today is Thursday END ------------------------
  # ------------------------ If Today is Friday START ------------------------
  if today_day_of_week == 'Friday':
    # Sunday
    sunday_date = date.today() - timedelta(days=5)
    # Monday
    monday_date = date.today() - timedelta(days=4)
    # Tuesday
    tuesday_date = date.today() - timedelta(days=3)
    # Wednesday
    wednesday_date = date.today() - timedelta(days=2)
    # Thursday
    thursday_date = date.today() - timedelta(days=1)
    # Friday
    friday_date = date.today()
    # Saturday
    saturday_date = date.today() + timedelta(days=1)
  # ------------------------ If Today is Friday END ------------------------
  # ------------------------ If Today is Saturday START ------------------------
  if today_day_of_week == 'Saturday':
    # Sunday
    sunday_date = date.today() - timedelta(days=6)
    # Monday
    monday_date = date.today() - timedelta(days=5)
    # Tuesday
    tuesday_date = date.today() - timedelta(days=4)
    # Wednesday
    wednesday_date = date.today() - timedelta(days=3)
    # Thursday
    thursday_date = date.today() - timedelta(days=2)
    # Friday
    friday_date = date.today() - timedelta(days=1)
    # Saturday
    saturday_date = date.today()
  # ------------------------ If Today is Saturday END ------------------------


  # ------------------------ This Week's Dates Dict START ------------------------
  this_upcoming_week_dates_dict = {
    'Sunday' : sunday_date.strftime('%Y-%m-%d'),
    'Monday' : monday_date.strftime('%Y-%m-%d'),
    'Tuesday' : tuesday_date.strftime('%Y-%m-%d'),
    'Wednesday' : wednesday_date.strftime('%Y-%m-%d'),
    'Thursday' : thursday_date.strftime('%Y-%m-%d'),
    'Friday' : friday_date.strftime('%Y-%m-%d'),
    'Saturday' : saturday_date.strftime('%Y-%m-%d')
  }
  # ------------------------ This Week's Dates Dict END ------------------------

  print('returning this_upcoming_week_dates_dict')
  print('=========================================== get_upcoming_week_dates_data_dict_function END ===========================================')
  return this_upcoming_week_dates_dict