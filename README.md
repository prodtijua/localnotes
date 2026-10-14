# localnotes
local-first django bookmark manager/note taking app

## features
* save a site by adding an entry
* add a title, description and category for that entry/bookmark
* add your own categories in a dedicated categories page
* sort saved bookmarks by category

## requirements
* Python 3.12 (for Nix users, defined in flake.nix)
* Django 5.0.1

## installation
* i have provided an installation/run shell script called "localnotes", which will put you in the .venv, make migrations, migrate and run the program.
* if the --install flag is passed, it will install django 5.0.1 by itself and exit after doing so.
* for NixOS users, it will enter the flake to run the program, eliminating the need to install Python system-wide.
```bash
$ git clone <this-repo>; cd <this-repo>
$ ./localnotes --install (required before running to install django)
$ ./localnotes
```
and then go to 127.0.0.1:8000 on a browser of your choice

## flags
* the ```--install``` flag installs dependencies (in this case, only django 5.0.1)
* the ```--create-symlink``` flag creates a symlink in ```~/.local/bin```, which allows the command to be run globally
* the ```--remove-symlink``` flag removes the symlink in ```~/.local/bin```
* the ```--help``` flag pulls up a help menu with all flags