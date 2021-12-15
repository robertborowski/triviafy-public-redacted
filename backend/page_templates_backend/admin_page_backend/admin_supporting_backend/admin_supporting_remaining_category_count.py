# -------------------------------------------------------------- Imports
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function
from backend.db.queries.select_queries.select_queries_triviafy_categories_selected_table.select_current_categories_team_channel_combo import select_current_categories_team_channel_combo_function
from backend.db.queries.select_queries.select_queries_triviafy_all_questions_table.select_admin_category_remaining_questions_per_team_channel_combo import select_admin_category_remaining_questions_per_team_channel_combo_function
from backend.db.queries.select_queries.select_queries_triviafy_all_questions_table.select_admin_category_remaining_all_categories_per_team_channel import select_admin_category_remaining_all_categories_per_team_channel_function

# -------------------------------------------------------------- Main Function
def admin_supporting_remaining_category_count_function(postgres_connection, postgres_cursor, pulled_team_id, pulled_channel_id, pulled_team_name, pulled_channel_name, pulled_user_count, master_all_companies_remainder_arr_of_dicts):
  localhost_print_function('=========================================== admin_supporting_remaining_category_count_function START ===========================================')

  # Pull all team channel combo selected categories as str
  company_current_categories_str = select_current_categories_team_channel_combo_function(postgres_connection, postgres_cursor, pulled_team_id, pulled_channel_id)


  # ------------------------ Not All Categories START ------------------------
  if company_current_categories_str != 'All Categories':
    # Turn str into array
    company_current_categories_arr = company_current_categories_str.split(',')
    
    # Remainder set to point out categories that ran out of all questions
    remainder_categories_selected_set = {''}
    for i in company_current_categories_arr:
      remainder_categories_selected_set.add(i)
    remainder_categories_selected_set.remove('')
    
    # LIKE str for the SQL SELECT Statement
    sql_like_statement_arr = []
    for i_category in company_current_categories_arr:
      indv_like_statement = "question_categories_list LIKE '%%" + i_category + "%%'"
      sql_like_statement_arr.append(indv_like_statement)
    sql_like_statement_str = ' OR '.join(sql_like_statement_arr)

    # SQL SELECT Statement to pull all category remainder counts
    remaining_category_count_arr_of_dict = select_admin_category_remaining_questions_per_team_channel_combo_function(postgres_connection, postgres_cursor, pulled_team_id, pulled_channel_id, sql_like_statement_str)
    
    # Separate out the categories that ran out of questions
    for i in remaining_category_count_arr_of_dict:
      if i['question_categories_list'] in remainder_categories_selected_set:
        remainder_categories_selected_set.remove(i['question_categories_list'])

    # Exclude the categories that have more than x questiosn available
    remaining_category_count_having_less_than_x_arr_of_dict = []
    for i_dict in remaining_category_count_arr_of_dict:
      if i_dict['count'] < 10:
        remaining_category_count_having_less_than_x_arr_of_dict.append(i_dict)
    # Push individual company to a dict
    indv_company_dict = {}
    indv_company_dict['company_team_id'] = pulled_team_id
    indv_company_dict['company_channel_id'] = pulled_channel_id
    indv_company_dict['company_team_name'] = pulled_team_name
    indv_company_dict['company_channel_name'] = pulled_channel_name
    indv_company_dict['company_user_count'] = pulled_user_count
    indv_company_dict['category_remainder_count'] = remaining_category_count_having_less_than_x_arr_of_dict
    indv_company_dict['categories_ran_out_of_questions'] = remainder_categories_selected_set
    master_all_companies_remainder_arr_of_dicts.append(indv_company_dict)
  # ------------------------ Not All Categories END ------------------------
  

  # ------------------------ Yes All Categories START ------------------------
  if company_current_categories_str == 'All Categories':
    team_channel_question_count_left_int = select_admin_category_remaining_all_categories_per_team_channel_function(postgres_connection, postgres_cursor, pulled_team_id, pulled_channel_id)
    if team_channel_question_count_left_int < 40:
      temp_dict = {}
      temp_dict['question_categories_list'] = 'All Categories'
      temp_dict['count'] = team_channel_question_count_left_int
      temp_arr = []
      temp_arr.append(temp_dict)

      # Push individual company to a dict
      indv_company_dict = {}
      indv_company_dict['company_team_id'] = pulled_team_id
      indv_company_dict['company_channel_id'] = pulled_channel_id
      indv_company_dict['company_team_name'] = pulled_team_name
      indv_company_dict['company_channel_name'] = pulled_channel_name
      indv_company_dict['company_user_count'] = pulled_user_count
      indv_company_dict['category_remainder_count'] = temp_arr
      indv_company_dict['categories_ran_out_of_questions'] = {}
      master_all_companies_remainder_arr_of_dicts.append(indv_company_dict)
  # ------------------------ Yes All Categories END ------------------------


  localhost_print_function('=========================================== admin_supporting_remaining_category_count_function END ===========================================')
  return master_all_companies_remainder_arr_of_dicts



# ---------------------------------------------------------------------------------------------------------------------------- Job to Run The Main Function
if __name__ == "__main__":
  admin_supporting_remaining_category_count_function()