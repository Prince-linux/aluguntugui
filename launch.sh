#! /bin/bash

# The settings module that will be used
export DJANGO_SETTINGS_MODULE=aluguntugui.local_settings

# The address and port that django will use
django_listen='127.0.0.1:8000'

trap 'kill $(jobs -p)' EXIT

./manage.py runserver $django_listen &
status=$?
if [[ $status -ne 0 ]]; then
    printf "failed to start django: %d\n" $status
    exit 1
fi

./manage.py qcluster &
status=$?
if [[ $status -ne 0 ]]; then
    printf "failed to start qcluster: %d\n" $status
    exit 1
fi

while sleep 60; do
    pgrep -f -a 'python ./manage.py runserver' > /dev/null 2>&1
    status=$?
    if [[ $status -ne 0 ]]; then
	printf "django has died"
	exit 1
    fi
      
    pgrep -f -a 'python ./manage.py qcluster' > /dev/null 2>&1
    status=$?
    if [[ $status -ne 0 ]]; then
	printf "qcluster has died"
	exit 1
    fi
done
      
