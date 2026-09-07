# localnotes
local-first django bookmark manager/note taking app

## features
* save a site by adding an entry
* add a title, description and category for that entry/bookmark
* currently you have to use the django admin panel to delete entries and add categories: so i made a default admin user called "admin", with its password being "1", you can access the admin panel by going to 127.0.0.1:8000/admin after running manage.py as shown below.

## requirements
* Python 3.12
* Django 5.0.1
(for NixOS users, Python 3.12 is defined in flake.nix, and it will be available after you run "nix develop" in the project directory)

## installation
for NixOS or any distro/OS with the nix package manager (you have to have flakes enabled):
```bash
$ git clone {this repo}; cd {this repo}
$ nix develop
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install django==5.0.1
$ python manage.py runserver
```
and then go to 127.0.0.1:8000 on your browser

for non-Nix distros, you will probably have to have python 3.12 system-wide
```bash
$ git clone {this repo}; cd {this repo}
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install django==5.0.1
$ python manage.py runserver
```
## to-do
* add ability to add new categories and delete existing categories without having to use the django admin panel
