mac: mac_venv_activate mac_pip
	python3 P3000.py

mac_pip: mac_venv_activate
	pip3 install -r requirements.txt

mac_venv_activate: mac_venv_create
	source venv/bin/activate

mac_venv_create:
	python3 -m venv venv

unx: unx_venv_activate unx_pip
	python3 P3000.py

unx_pip: unx_venv_activate
	pip3 install -r requirements.txt

unx_venv_activate: unx_venv_create
	source venv/bin/activate

unx_venv_create:
	python3 -m venv venv

win: win_venv_activate win_pip
	python P3000.py

win_pip: win_venv_activate
	pip install -r requirements.txt

win_venv_activate: win_venv_create
	source venv/Scripts/activate

win_venv_create:
	python -m venv venv

m:mac
Mac:m
macOS:m
macos:m
apple:m
Apple:m

u:unx
unix:u
Unix:u
l:u
linux:u
Linux:u
g:u
gnu:u
GNU:u

w:win
Win:w
windows:w
Windows:w