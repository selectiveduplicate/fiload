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
3. Make the Bash script executable:
	```bash
	chmod u+x zipit.sh
	```
   For convenience, make ``fiload.py`` executable too.
   
4. Run by:
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
