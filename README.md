# Runn Backend :tw-1f3c3:

> Note: Please checkout Astra&trade; Database setup on [astra](https://github.com/Saurabh-Singh-00/runn-backend/tree/astra "astra") branch if you **don't** want to setup Apache Cassandra&trade; locally on your system.

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

> Add a `.env` file in the `src` folder before proceeding and paste the contents from `.env_sample`


- Get your cassandra host network IP
```console
sudo docker inspect runn-network
```

```js
"Containers": {
    "9184a78b0ccb6f2993407d3a9858fc9f28ce2dfce0b3a1c1bba51fd0d3f351e1": {
        "Name": "runn-IN-1",
        "EndpointID": "0432eacdf5859f0cf2aea94cb6adb400b88e79d7457945c430a14a8a9f522386",
        "MacAddress": "02:42:ac:12:00:02",
        "IPv4Address": "172.18.0.2/16",
        "IPv6Address": ""
    }
}
```
> Also replace the `HOST` in `settings/dev.py` with above `IPv4Address` you will get.

<h4>1. <img src="https://cdn.iconscout.com/icon/free/png-24/docker-226091.png" />  Docker&trade; Setup for Django server
</h4>

- Navigate to the cloned repository and paste the following in your shell
```console
sudo docker-compose run backend python src/manage.py sync_cassandra
```

- Run Django Server
```console
sudo docker-compose run -p 8000:8000 backend
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
- [X] Add Astra&trade; Connection
