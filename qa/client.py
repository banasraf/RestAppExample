from glob import glob
import re
from unittest import result
from urllib import response
import requests
from requests.auth import HTTPBasicAuth


_current_auth = None

class auth_as:
  def __init__(self, username, password):
    self.auth = HTTPBasicAuth(username, password)
  
  def __enter__(self):
    global _current_auth
    old_auth = _current_auth
    _current_auth = self.auth
    self.auth = old_auth

  def __exit__(self, type, value, traceback):
    global _current_auth
    auth = _current_auth
    _current_auth = self.auth
    self.auth = auth


def _validate_response(response):
  if not response.ok:
      raise RuntimeError("Response status: ", response.status_code, " Response: ", response.json())


def _get_json(url):
    response = requests.get(url, auth=_current_auth)
    _validate_response(response)
    return response.json()


class Client:
  def __init__(self, url):
    self.url = url


  def get_contents(self, endpoint):
    response = _get_json(self.url + endpoint)
    if 'results' not in response or 'next' not in response:
      raise RuntimeError("Expected paginated response")
    for res in response['results']:
      yield res
    
    while response['next'] is not None:
      response = _get_json(response['next'])
      for res in response['results']:
        yield res

  def get_users(self):
    return self.get_contents('users/')

  def post(self, endpoint, json):
    response = requests.post(self.url + endpoint, auth=_current_auth, json=json)
    _validate_response(response)

  def register_user(self, username, password, email=''):
    self.post('users/', {'username': username, 'password': password, 'email': email})

  def delete_abs(self, url):
    response = requests.delete(url, auth=_current_auth)
    _validate_response(response)

  def delete(self, endpoint):
    response = requests.delete(self.url + endpoint, auth=_current_auth)
    _validate_response(response)

  

  # def create_user(self, endpoint)
  
    

# client = Client('http://localhost:8000/')




# # client.post('users/', {'username': 'user2', 'password': 'pass1', 'email': 'u@mail.com'})

# with auth_as('admin', 'admin'):
#   for user in client.get_contents('users/'):
#     print(user)

#   # client.delete('users/7/')

