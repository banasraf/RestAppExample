from client import Client, auth_as
import argparse

parser = argparse.ArgumentParser(description='Test script.')
parser.add_argument('-u', '--superuser-username', action='store', help='Superuser username', required=True)
parser.add_argument('-p', '--superuser-password', action='store', help='Superuser password', required=True)
parser.add_argument('-a', '--server-url', action='store', help='Server url', required=True)

if __name__ == '__main__':
  args = parser.parse_args()
  client = Client(args.server_url)
  username = args.superuser_username
  password = args.superuser_password
  with auth_as(username, password):
    initial_users = list(client.get_users())
    users = [
      {
        'username': 'user1',
        'password': 'pass1',
        'email': 'u1@mail.com'
      },
      {
        'username': 'user2',
        'password': 'pass2',
        'email': 'u2@mail.com'
      }
    ]
    for user in users:
      client.register_user(**user)

    get_users = list(client.get_users())
    get_users_info = list(map(lambda json: {'username': json['username'], 'email': json['email']},
                          get_users))
    for user in users:
      assert {'username': user['username'],
              'email': user['email']} in get_users_info
    
    added_usernames = [user['username'] for user in users]

    for user in get_users:
      if user['username'] in added_usernames:
        client.delete_abs(user['url'])

    assert list(client.get_users()) == initial_users

      
    

    