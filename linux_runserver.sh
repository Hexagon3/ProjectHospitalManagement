#! /usr/bin/bash 

my_app_path=$( dirname $(readlink -f "$0"))
source "$my_app_path/Backend/pyenv/bin/activate"

cd "$my_app_path/Backend/HospitalManagement"
python manage.py runserver 8590 
