set -ex
python manage.py migrate
python manage.py createsuperuser --no-input