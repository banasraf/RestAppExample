set -ex
python test_user.py -u $DJANGO_SUPERUSER_USERNAME -p $DJANGO_SUPERUSER_PASSWORD -a $SERVER_URL
