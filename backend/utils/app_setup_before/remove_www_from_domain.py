from flask import render_template, Blueprint, session, request, redirect
from urllib.parse import urlparse, urlunparse

def remove_www_from_domain_function(current_url):
  """Returns: Redirect www requests to non-www."""
  urlparts = urlparse(current_url)
  if urlparts.netloc == 'www.triviafy.com':
    urlparts_list = list(urlparts)
    urlparts_list[1] = 'triviafy.com'
    return urlunparse(urlparts_list)