#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements_divine.txt

python manage.py collectstatic --no-input
python manage.py migrate


echo "from django.contrib.auth.mode ls import User; User.objects.create_superuser('gandolfdgrey','barrymore@venax.co','Tomiwa@me123')" | python3 manage.py shell