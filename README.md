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
i built this only with my setup in mind, so i will go over setup on NixOS.

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

for other distros you will probably have to install packages manually, particularly python 3.12 (specific version i used), and then run:
```bash
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install django==5.0.1
$ python manage.py runserver
```

by default it should have two entries: "Django Docs" and "nixpkgs", and one category: "Programming" i added those myself since i plan on using this as well, but i forgot to delete them from the database.

## to-do
* add ability to delete bookmarks without having to use the django admin panel
* add ability to add new categories without having to use the django admin panel
