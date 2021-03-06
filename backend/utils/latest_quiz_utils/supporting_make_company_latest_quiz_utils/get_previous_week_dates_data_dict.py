# -------------------------------------------------------------- Imports
from datetime import date, timedelta
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def get_previous_week_dates_data_dict_function():
  localhost_print_function('=========================================== get_previous_week_dates_data_dict_function START ===========================================')
  
  # ------------------------ Get Today's Date START ------------------------
  # Today's date
  today_date = date.today()
  # Today's date, day of week
  today_day_of_week = today_date.strftime('%A')
  # ------------------------ Get Today's Date END ------------------------


  # ------------------------ If Today is Sunday START ------------------------
  if today_day_of_week == 'Sunday':
    # Sunday
    sunday_date = date.today() - timedelta(days=7)
    # Monday
    monday_date = date.today() - timedelta(days=6)
    # Tuesday
    tuesday_date = date.today() - timedelta(days=5)
    # Wednesday
    wednesday_date = date.today() - timedelta(days=4)
    # Thursday
    thursday_date = date.today() - timedelta(days=3)
    # Friday
    friday_date = date.today() - timedelta(days=2)
    # Saturday
    saturday_date = date.today() - timedelta(days=1)
  # ------------------------ If Today is Sunday END ------------------------
  # ------------------------ If Today is Monday START ------------------------
  if today_day_of_week == 'Monday':
    # Sunday
    sunday_date = date.today() - timedelta(days=8)
    # Monday
    monday_date = date.today() - timedelta(days=7)
    # Tuesday
    tuesday_date = date.today() - timedelta(days=6)
    # Wednesday
    wednesday_date = date.today() - timedelta(days=5)
    # Thursday
    thursday_date = date.today() - timedelta(days=4)
    # Friday
    friday_date = date.today() - timedelta(days=3)
    # Saturday
    saturday_date = date.today() - timedelta(days=2)
  # ------------------------ If Today is Monday END ------------------------
  # ------------------------ If Today is Tuesday START ------------------------
  if today_day_of_week == 'Tuesday':
    # Sunday
    sunday_date = date.today() - timedelta(days=9)
    # Monday
    monday_date = date.today() - timedelta(days=8)
    # Tuesday
    tuesday_date = date.today() - timedelta(days=7)
    # Wednesday
    wednesday_date = date.today() - timedelta(days=6)
    # Thursday
    thursday_date = date.today() - timedelta(days=5)
    # Friday
    friday_date = date.today() - timedelta(days=4)
    # Saturday
    saturday_date = date.today() - timedelta(days=3)
  # ------------------------ If Today is Tuesday END ------------------------
  # ------------------------ If Today is Wednesday START ------------------------
  if today_day_of_week == 'Wednesday':
    # Sunday
    sunday_date = date.today() - timedelta(days=10)
    # Monday
    monday_date = date.today() - timedelta(days=9)
    # Tuesday
    tuesday_date = date.today() - timedelta(days=8)
    # Wednesday
    wednesday_date = date.today() - timedelta(days=7)
    # Thursday
    thursday_date = date.today() - timedelta(days=6)
    # Friday
    friday_date = date.today() - timedelta(days=5)
    # Saturday
    saturday_date = date.today() - timedelta(days=4)
  # ------------------------ If Today is Wednesday END ------------------------
  # ------------------------ If Today is Thursday START ------------------------
  if today_day_of_week == 'Thursday':
    # Sunday
    sunday_date = date.today() - timedelta(days=11)
    # Monday
    monday_date = date.today() - timedelta(days=10)
    # Tuesday
    tuesday_date = date.today() - timedelta(days=9)
    # Wednesday
    wednesday_date = date.today() - timedelta(days=8)
    # Thursday
    thursday_date = date.today() - timedelta(days=7)
    # Friday
    friday_date = date.today() - timedelta(days=6)
    # Saturday
    saturday_date = date.today() - timedelta(days=5)
  # ------------------------ If Today is Thursday END ------------------------
  # ------------------------ If Today is Friday START ------------------------
  if today_day_of_week == 'Friday':
    # Sunday
    sunday_date = date.today() - timedelta(days=12)
    # Monday
    monday_date = date.today() - timedelta(days=11)
    # Tuesday
    tuesday_date = date.today() - timedelta(days=10)
    # Wednesday
    wednesday_date = date.today() - timedelta(days=9)
    # Thursday
    thursday_date = date.today() - timedelta(days=8)
    # Friday
    friday_date = date.today() - timedelta(days=7)
    # Saturday
    saturday_date = date.today() - timedelta(days=6)
  # ------------------------ If Today is Friday END ------------------------
  # ------------------------ If Today is Saturday START ------------------------
  if today_day_of_week == 'Saturday':
    # Sunday
    sunday_date = date.today() - timedelta(days=13)
    # Monday
    monday_date = date.today() - timedelta(days=12)
    # Tuesday
    tuesday_date = date.today() - timedelta(days=11)
    # Wednesday
    wednesday_date = date.today() - timedelta(days=10)
    # Thursday
    thursday_date = date.today() - timedelta(days=9)
    # Friday
    friday_date = date.today() - timedelta(days=8)
    # Saturday
    saturday_date = date.today() - timedelta(days=7)
  # ------------------------ If Today is Saturday END ------------------------


  # ------------------------ This Week's Dates Dict START ------------------------
  previous_week_dates_dict = {
    'Sunday' : sunday_date.strftime('%Y-%m-%d'),
    'Monday' : monday_date.strftime('%Y-%m-%d'),
    'Tuesday' : tuesday_date.strftime('%Y-%m-%d'),
    'Wednesday' : wednesday_date.strftime('%Y-%m-%d'),
    'Thursday' : thursday_date.strftime('%Y-%m-%d'),
    'Friday' : friday_date.strftime('%Y-%m-%d'),
    'Saturday' : saturday_date.strftime('%Y-%m-%d')
  }
  # ------------------------ This Week's Dates Dict END ------------------------

  localhost_print_function('returning previous_week_dates_dict')
  localhost_print_function('=========================================== get_previous_week_dates_data_dict_function END ===========================================')
  return previous_week_dates_dict