# -------------------------------------------------------------- Imports
from datetime import date, timedelta
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def get_next_weeks_dates_data_dict_function():
  localhost_print_function('=========================================== get_next_weeks_dates_data_dict_function START ===========================================')
  
  # ------------------------ Get Today's Date START ------------------------
  # Today's date
  today_date_next_week = date.today() + timedelta(days=7)
  # Today's date, day of week
  today_day_of_week_next_week = today_date_next_week.strftime('%A')
  # ------------------------ Get Today's Date END ------------------------


  # ------------------------ If Today is Sunday START ------------------------
  if today_day_of_week_next_week == 'Sunday':
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
  if today_day_of_week_next_week == 'Monday':
    # Sunday
    sunday_date = date.today() + timedelta(days=6)
    # Monday
    monday_date = date.today() + timedelta(days=7)
    # Tuesday
    tuesday_date = date.today() + timedelta(days=8)
    # Wednesday
    wednesday_date = date.today() + timedelta(days=9)
    # Thursday
    thursday_date = date.today() + timedelta(days=10)
    # Friday
    friday_date = date.today() + timedelta(days=11)
    # Saturday
    saturday_date = date.today() + timedelta(days=12)
  # ------------------------ If Today is Monday END ------------------------
  # ------------------------ If Today is Tuesday START ------------------------
  if today_day_of_week_next_week == 'Tuesday':
    # Sunday
    sunday_date = date.today() + timedelta(days=5)
    # Monday
    monday_date = date.today() + timedelta(days=6)
    # Tuesday
    tuesday_date = date.today() + timedelta(days=7)
    # Wednesday
    wednesday_date = date.today() + timedelta(days=8)
    # Thursday
    thursday_date = date.today() + timedelta(days=9)
    # Friday
    friday_date = date.today() + timedelta(days=10)
    # Saturday
    saturday_date = date.today() + timedelta(days=11)
  # ------------------------ If Today is Tuesday END ------------------------
  # ------------------------ If Today is Wednesday START ------------------------
  if today_day_of_week_next_week == 'Wednesday':
    # Sunday
    sunday_date = date.today() + timedelta(days=4)
    # Monday
    monday_date = date.today() + timedelta(days=5)
    # Tuesday
    tuesday_date = date.today() + timedelta(days=6)
    # Wednesday
    wednesday_date = date.today() + timedelta(days=7)
    # Thursday
    thursday_date = date.today() + timedelta(days=8)
    # Friday
    friday_date = date.today() + timedelta(days=9)
    # Saturday
    saturday_date = date.today() + timedelta(days=10)
  # ------------------------ If Today is Wednesday END ------------------------
  # ------------------------ If Today is Thursday START ------------------------
  if today_day_of_week_next_week == 'Thursday':
    # Sunday
    sunday_date = date.today() + timedelta(days=3)
    # Monday
    monday_date = date.today() + timedelta(days=4)
    # Tuesday
    tuesday_date = date.today() + timedelta(days=5)
    # Wednesday
    wednesday_date = date.today() + timedelta(days=6)
    # Thursday
    thursday_date = date.today() + timedelta(days=7)
    # Friday
    friday_date = date.today() + timedelta(days=8)
    # Saturday
    saturday_date = date.today() + timedelta(days=9)
  # ------------------------ If Today is Thursday END ------------------------
  # ------------------------ If Today is Friday START ------------------------
  if today_day_of_week_next_week == 'Friday':
    # Sunday
    sunday_date = date.today() + timedelta(days=2)
    # Monday
    monday_date = date.today() + timedelta(days=3)
    # Tuesday
    tuesday_date = date.today() + timedelta(days=4)
    # Wednesday
    wednesday_date = date.today() + timedelta(days=5)
    # Thursday
    thursday_date = date.today() + timedelta(days=6)
    # Friday
    friday_date = date.today() + timedelta(days=7)
    # Saturday
    saturday_date = date.today() + timedelta(days=8)
  # ------------------------ If Today is Friday END ------------------------
  # ------------------------ If Today is Saturday START ------------------------
  if today_day_of_week_next_week == 'Saturday':
    # today_day_of_week_next_week
    sunday_date = date.today() + timedelta(days=1)
    # Monday
    monday_date = date.today() + timedelta(days=2)
    # Tuesday
    tuesday_date = date.today() + timedelta(days=3)
    # Wednesday
    wednesday_date = date.today() + timedelta(days=4)
    # Thursday
    thursday_date = date.today() + timedelta(days=5)
    # Friday
    friday_date = date.today() + timedelta(days=6)
    # Saturday
    saturday_date = date.today() + timedelta(days=7)
  # ------------------------ If Today is Saturday END ------------------------


  # ------------------------ This Week's Dates Dict START ------------------------
  next_week_dates_dict = {
    'Sunday' : sunday_date.strftime('%Y-%m-%d'),
    'Monday' : monday_date.strftime('%Y-%m-%d'),
    'Tuesday' : tuesday_date.strftime('%Y-%m-%d'),
    'Wednesday' : wednesday_date.strftime('%Y-%m-%d'),
    'Thursday' : thursday_date.strftime('%Y-%m-%d'),
    'Friday' : friday_date.strftime('%Y-%m-%d'),
    'Saturday' : saturday_date.strftime('%Y-%m-%d')
  }
  # ------------------------ This Week's Dates Dict END ------------------------

  localhost_print_function('=========================================== get_next_weeks_dates_data_dict_function END ===========================================')
  return next_week_dates_dict