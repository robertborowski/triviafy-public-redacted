# -------------------------------------------------------------- Imports
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function

# -------------------------------------------------------------- Main Function
def sanitize_page_output_company_name_function(user_company_name):
  localhost_print_function('=========================================== sanitize_page_output_company_name_function START ===========================================')
  try:
    user_company_name = user_company_name.replace('-',' ')
  except:
    pass

  try:
    user_company_name = user_company_name.replace('_',' ')
  except:
    pass

  localhost_print_function('=========================================== sanitize_page_output_company_name_function END ===========================================')
  return user_company_name