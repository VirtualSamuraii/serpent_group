# Serpent C2

## Setup the server

### Install python dependencies

```pip3 install -r requirements.txt```

### Run the C2 Server
python3 -m flask --app c2.py run --host=0.0.0.0 --debug --reload

### Use

**Step 1: Initialize the database**
To initialize the database, run:

```curl http://127.0.0.1:5000/db```

**Step 2: Run the malicious agent on your target host**

Once you launched the server, you should be able to see the debug logs.

Replace the IP address with yours at line 9 on the C2 client.py :

```server_ip = "\<SET_SERVER_IP>"```

Launch the agent in order to simulate infection:

```python3 client.py```


## Setup the C2 web dashboard

1/ Open the ```web_app/src/services/DashboardServices.js``` file and replace with your C2 Server IP Address

2/ Run : ```cd web_app/```

3/ Run : ```npm run install```

4/ Run : ```npm run build```

5/ Run : ```serve -s dist/```


### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
