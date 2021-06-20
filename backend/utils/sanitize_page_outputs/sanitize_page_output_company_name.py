def sanitize_page_output_company_name_function(user_company_name):
  print('=========================================== sanitize_page_output_company_name_function START ===========================================')
  try:
    user_company_name = user_company_name.replace('-',' ')
  except:
    pass

  try:
    user_company_name = user_company_name.replace('_',' ')
  except:
    pass

  print('=========================================== sanitize_page_output_company_name_function END ===========================================')
  return user_company_name