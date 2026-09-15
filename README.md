# localnotes
local-first django bookmark manager/note taking app

## features
* save a site by adding an entry
* add a title, description and category for that entry/bookmark
* add your own categories in a dedicated categories page
* sort saved bookmarks by category

## requirements
* Python 3.12
* Django 5.0.1
(for Nix users, Python 3.12 is defined in flake.nix, and it will be available after you run "nix develop" in the project directory)

## installation
for NixOS or any distro/OS with the nix package manager (you have to have flakes enabled):
```bash
$ git clone {this repo}; cd {this repo}
$ nix develop
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install django==5.0.1
$ python manage.py migrate (IMPORTANT!)
$ python manage.py runserver
```
and then go to 127.0.0.1:8000 on your browser

for non-Nix distros, you will probably have to have python 3.12 system-wide
```bash
$ git clone {this repo}; cd {this repo}
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install django==5.0.1
$ python manage.py migrate (IMPORTANT!)
$ python manage.py runserver
```
p.s. i specifically wrote "python" here but use whatever command you have to for python 3.12, be it python3, python3.12, python312 etc.
