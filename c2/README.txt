# Serpent C2

## Installation


1) Installer les dépendances Python
> pip install -r requirements.txt

2) Pour lancer le serveur
> export FLASK_APP=c2
> flask run --eager-loading --host=0.0.0.0
(host 0.0.0.0 pour le mettre sur toutes les interfaces, donc accessible via l'host)



V2:

installer pip

pip3 install -r requirements.txt

## Launch
python3 -m flask --app c2.py run --host=0.0.0.0 --debug --reload
python3 -m flask --app c2.py run --host=0.0.0.0 --debug


## Use

**Step 1: Initialize the database**
To initialize the database, run:
> curl 127.0.0.1:5000/db

Just hit the /db endpoint to create the database

**Step 2: Launch the malicious agent**
Once you launched the server, you should be able to see the debug logs.

Replace client's server IP placeholder with yours at line 9:

> server_ip = "\<SET_SERVER_IP>"

Launch the agent in order to simulate infection:
> python3 client.py
