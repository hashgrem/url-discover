# url-discover v1.0

urlDiscover is an open source tool that automates the process of finding hidden pages, files, and directories on websites. It can be usefull for recon step on CTF's challenges and penetration test.

![alt text](https://github.com/hashgrem/url-discover/blob/master/image.jpg?raw=true)

## Installation
First of all, you need python3 to use urlDiscover, you can download it from this link: https://www.python.org/downloads/

You can download the zip version on github, or traditionally clone the repository from your command line:
```
git clone https://github.com/hashgrem/url-discover.git
```

After dowloading, you'll need to install libraries to run the script correctly. You can run the following command:
```
pip install -r requirements.txt
```

## Usage

To display basic usage and switches, you can use help tag, by running the following command:
```
python3 urlDiscover.py -h

usage: urlDiscover.py [-h] -u URL -w WORDLIST -t THREAD

options:
    -h, --help                            show this help message and exit
    -u URL, --url URL                     url you want to test
    -w WORDLIST, --wordlist WORDLIST      wordlist path
    -t THREAD, --thread THREAD            number of threads 
```
You can increase execution speed by setting a higher number of thread, depending on your CPU capacity

## Disclaimer

A little remind: you are the only one responsible for the use you make of this tool. You must be allowed by your target or by the organisation you are testing
