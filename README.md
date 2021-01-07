# Runn Backend :tw-1f3c3:
**There are two requirements to setup this project.**
1.  Docker&trade;
2. Virtual Environment

> Note: Make sure you have setup Cassandra&trade; database before starting the Django Server

------------

<h4><img src="https://cdn.iconscout.com/icon/free/png-24/docker-226091.png" />  Docker&trade; setup for Apache Cassandra&trade; Database
</h4>

- Create a Bridge Network
```console
sudo docker network create -d bridge runn-network
```

- Create Cassandra&trade; Database
```console
sudo docker container run --name runn-IN-1 --network runn-network -e MAX_HEAP_SIZE="1G" -e HEAP_NEWSIZE="256M" -d cassandra:latest
```

------------

*Clone this repository and follow the steps below*

<h4>1. <img src="https://cdn.iconscout.com/icon/free/png-24/docker-226091.png" />  Docker&trade; Setup for Django server
</h4>

- Navigate to the cloned repository and paste the following in your shell
```console
sudo docker-compose run backend python src/manage.py sync_cassandra
```

<h4>2. <img src="https://cdn.iconscout.com/icon/free/png-24/python-2752092-2284909.png" />  Virtual Environment Setup for Django server
</h4>

- This step is only required when you cannot connect to your Docker&trade; image from VSCode&trade;
```console
pip3 install virtualenv
```

- Create virtual environment
```console
virtualenv venv
```

- Activate Virtual Environment
```console
source venv/bin/activate
```

- Install Project Dependencies
```console
pip install -r requirements.txt
```

#### TODOs:
- [ ] Add Astra&trade; Connection
