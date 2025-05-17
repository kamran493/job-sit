#!/usr/bin/env bash
# اجرای دستورات پس از نصب

python manage.py migrate
python manage.py collectstatic --noinput
python manage.py shell < create_superuser.py