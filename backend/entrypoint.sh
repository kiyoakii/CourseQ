#!/usr/bin/env bash

if [ ! -f "course/app/config/secure.py" ]; then
  echo "secure.py not found. Use the default secure instead"
  cp course/app/config/secure_template.py course/app/config/secure.py
fi

/wait.sh -t 120 mysql:3306

cd course && python3 manage.py db upgrade

gunicorn --workers 4 --bind 0.0.0.0:8000 course:app
