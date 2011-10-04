#!/usr/bin/env bash
# Currently we save users
./manage.py dumpdata --format=json --indent=4 auth.User auth.Group auth.Permission > customer/fixtures/initial_data.json

