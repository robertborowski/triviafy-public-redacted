# -------------------------------------------------------------- Imports
from backend.utils.localhost_print_utils.localhost_print import localhost_print_function
from backend.db.queries.select_queries.select_queries_triviafy_quiz_master_table.select_quiz_count_for_company_slack import select_quiz_count_for_company_slack_function
from backend.db.queries.select_queries.select_queries_triviafy_quiz_winners_table.select_quiz_winner_count_for_team_channel_combo import select_quiz_winner_count_for_team_channel_combo_function

# -------------------------------------------------------------- Main Function
def admin_supporting_winner_counts_function(postgres_connection, postgres_cursor, pulled_team_id, pulled_channel_id, pulled_team_name, pulled_channel_name, pulled_user_count, master_all_companies_winner_counts_arr_of_dicts):
  localhost_print_function('=========================================== admin_supporting_winner_counts_function START ===========================================')

  # Pull the current quiz count
  company_current_quiz_count_arr = select_quiz_count_for_company_slack_function(postgres_connection, postgres_cursor, pulled_team_id, pulled_channel_id)
  company_current_quiz_count_int = company_current_quiz_count_arr[0]

  # Pull the user win count
  quiz_winners_count_arr = select_quiz_winner_count_for_team_channel_combo_function(postgres_connection, postgres_cursor, pulled_team_id, pulled_channel_id)
  if quiz_winners_count_arr == None:
    quiz_winners_count_arr = []
    quiz_winners_count_arr.append((0, '0', '0', '0'))


  # ------------------------ Add to Dictionary START ------------------------
  indv_company_dict = {}
  indv_company_dict['company_team_id'] = pulled_team_id
  indv_company_dict['company_channel_id'] = pulled_channel_id
  indv_company_dict['company_team_name'] = pulled_team_name
  indv_company_dict['company_channel_name'] = pulled_channel_name
  indv_company_dict['company_user_count'] = pulled_user_count
  indv_company_dict['company_current_quiz_count_int'] = company_current_quiz_count_int
  indv_company_dict['quiz_winners_count_arr'] = quiz_winners_count_arr

  master_all_companies_winner_counts_arr_of_dicts.append(indv_company_dict)
  # ------------------------ Add to Dictionary END ------------------------
  

  localhost_print_function('=========================================== admin_supporting_winner_counts_function END ===========================================')
  return master_all_companies_winner_counts_arr_of_dicts



# ---------------------------------------------------------------------------------------------------------------------------- Job to Run The Main Function
if __name__ == "__main__":
  admin_supporting_winner_counts_function()