# -------------------------------------------------------------- Imports
from urllib.parse import urlparse, urlunparse

# -------------------------------------------------------------- Main Function
def check_if_url_www_function(current_url):
  """Returns: Checks if current URL starts with www."""
  urlparts = urlparse(current_url)
  if urlparts.netloc == 'www.triviafy.com':
    return True
  return False