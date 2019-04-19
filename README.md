# DOCKPORT
Script to view which url used image of docker

## Installation
* <b>`git clone git@gitlab.com:PunGy/dockport.git`</b> or <b>`git clone https://gitlab.com/PunGy/dockport.git`</b>
* `pip3 install -r requirements.txt` - installing requirements of project
* `sudo ./init.sh` - put dockport file in /usr/local/bin/

## Requirements
Script using package manager <b>`pip3`</b> and interpreter <b>`python3`</b>. For clipboard using <b>`pyperclip`</b> 

## Usage
in call of scripts must be specified name of image `dockport image [options]`<br/>
><b>Options:</b>
* <b>`-p`</b> - prefix of image, example `dockport nginx -p gitlab` (image: gitlab-nginx), in case if script will find in current directory file <b>.env</b>, <b>no need to write prefix name</b>, it will be autocompleted, in other case it necessarily
* <b>`-b`</b> - copy into clipboard
* <b>`-o`</b> - open in browser (for now only google-chrome)

### Abbreviations
With abbreviations you can shorten long names of images, like `phpmyadmin -> pma`<br/>
Example: `dockport pma -p cooler` will convert to `cooler-phpmyadmin` 
* `pma` - phpmyadmin
* `serve` - nginx


### Сonfigure
In file dockport.py first few objects using to configure script (in #CONFIG ... #CONFIG/)<br/>
You can update this objects for more convenient work
* `config` - basic config of file, here specified name of server, delimiters and so on...
* `abbreviations` - abbreviations to shortening long words, you can add your own
