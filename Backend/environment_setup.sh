#! /usr/bin/bash 
# sudo apt update 
# sudo apt install python-pip 
my_app_path=$( dirname $(readlink -f "$0"))

python -m venv "$my_app_path/pyenv"

source "$my_app_path/pyenv/bin/activate"
echo $(pwd)
pip install --upgrade pip
pip install -r "$my_app_path/python_requirements.txt"
django-admin
