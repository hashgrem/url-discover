"""
Project name: Url Discover
Version: 1.0
Copyright© 14/10/2022, DEMARD Jérémy

"""
from datetime import datetime
from threading import Thread
from colorama import Fore, Back, Style, init
import requests
import argparse
import validators
import time
import sys


def Menu():
	parser = argparse.ArgumentParser()
	parser.add_argument('-u', '--url', type=str, required=True, help='url you want to test')
	parser.add_argument('-w', '--wordlist', type=str, required=True, help='wordlist path')
	parser.add_argument('-t', '--thread', type=int, required=True, help='number of threads')

	args = parser.parse_args()
	user_args = [args.url, args.wordlist, args.thread]

	return user_args

def GetWordlist(wordlist):
	try:
		with open(wordlist, 'r') as w:
			words = w.read().splitlines()
		w.close()

		return words
	except:
		print(f"{Fore.RED}Error: check your wordlist path{Style.RESET_ALL}")
		sys.exit()

def SplitWordlist(wordlist, nb_chuncks):
		words = GetWordlist(wordlist)
		chunks = [words[w:w+nb_chuncks] for w in range(0, len(words), nb_chuncks)]

		return chunks

def Bruteforce(chuncked_wordlists, url, codes):
	timer_start = time.perf_counter()
	threads = []
	try:
		print(f"{Fore.GREEN}[+] Scan successfully started...\n{Style.RESET_ALL}")
		for each_list in chuncked_wordlists:
			threads.append(Thread(target=Attack, args=(each_list, url, codes)))
		for t in threads:
			t.start()
	except:
		print(f"{Fore.RED}Oops ! An error occured while starting threads.{Style.RESET_ALL}")
		sys.exit()

	timer_end = time.perf_counter()
	duration = timer_end - timer_start
	time.sleep(2)
	print("\nExecuted in: "+str(duration)+" seconds.")

def Attack(wordlist, url, codes):
	for word in wordlist:
		word.rstrip()
		concat_url = url+word
		query = requests.get(concat_url).status_code
		if query in codes:
			print(f"\t/{word} --------> {query}")
		
if __name__ == "__main__":

	print(f"""                                
██╗   ██╗██████╗ ██╗                                         
██║   ██║██╔══██╗██║                                         
██║   ██║██████╔╝██║                                         
██║   ██║██╔══██╗██║                                         
╚██████╔╝██║  ██║███████                                    
                                                             
██████╗ ██╗███████╗ ██████╗ ██████╗ ██╗   ██╗███████╗██████╗ 
██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║  ██║██║███████╗██║     ██║   ██║██║   ██║█████╗  ██████╔╝
██║  ██║██║╚════██║██║     ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
██████╔╝██║███████║╚██████╗╚██████╔╝ ╚████╔╝ ███████╗██║  ██║""")

	init()

	print("\nA tool to find hidden pages, files and directories behind URL\n\n")
	print(f"""{Fore.YELLOW}Exemple usage:{Style.RESET_ALL} python3 urlDiscover.py -u "https://exemple.test/" -w /path/to/my/wordlist.txt -t 10\n""")
	print("Dev by Teiiko (Teiiko#8831 on Discord)\n")
	print(Fore.BLUE+"Version 1.0\n"+Style.RESET_ALL)

	args = Menu()
	url = str(args[0])

	if validators.url(url) != True:
		print(f"""{Fore.RED}Error: check your URL syntax. Url needs to be given with double quotes, or without any quotes.{Style.RESET_ALL}""")
	else:
		if url.endswith('/') != True:
			url = url+'/'

		try:
			check_url = requests.get(url)
		except:
			print(f"{Fore.RED}Error: URL is unreachable.{Style.RESET_ALL}")
			sys.exit()
		
		codes = [200, 204, 301, 302, 307, 401, 407] #http's status codes
		nb_threads = args[2]
		wordlist_path = str(args[1])
		lists = SplitWordlist(wordlist_path, nb_threads)
		now = datetime.now()
		dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

		print(f"""
	 =======================================================
		
	 [-] target = {Fore.GREEN+url+Style.RESET_ALL}

	 [-] wordlist = {wordlist_path}

	 [-] starting at = {dt_string}

	 =======================================================
			""")

		Bruteforce(lists, url, codes)


		