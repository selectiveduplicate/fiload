# fiload
**fiload** is a simple command-line tool for uploading files to Dropbox.

# Installation

1. Clone the repo:
	```bash
	git clone https://github.com/selectiveduplicate/fiload/
	```
2. ``cd`` into **fiload**:
	```bash
	cd ~/fiload
	```
3. Install as per ``requirements.txt``:
	```bash
	pip install -r requirements.txt
	```
4. Make ``fiload.py`` executable for convenience:
	```bash
	chmod u+x fiload.py
	```
5. Run by:
	```bash
	./fiload.py
	```
	or
	```bash
	python3 fiload.py
	```
    
# Usage
You need to provide the canonical paths to your files/directories that you want to upload, each item seperated by a single comma. For example,


```bash
~/dummyfile.txt,~/Pictures/Wallpapers
```

If you put in multiple directories, they will all be inside a single zip archive. All files will be available in Dropbox as ``/home/Documents``.
