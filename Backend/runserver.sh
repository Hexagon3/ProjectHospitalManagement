#! /usr/bin/bash 

my_app_path=$( dirname $(readlink -f "$0"))
source "$my_app_path/pyenv/bin/activate"

cd "$my_app_path/HospitalManagement"
python manage.py runserver 