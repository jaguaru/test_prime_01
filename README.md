# test_prime_01
Small Backend API using Flask for Prime Hire

# API CRUD Publications 1.0
API CRUD for create publications.

## Installation

Clone the repository

```
git clone https://github.com/jaguaru/test_prime_01.git
```

Create the directory for the virtual environment

```
mkdir vserver
```

Install the virtual environment

```
virtualenv -p python3 vserver
```

Activate the virtual environment

```
source vserver/bin/activate
```

Install the libraries

```
cd app
pip install -r requirements.txt
```


## Example with curl to use the API

```
curl -H "Content-Type: application/json" -X POST http://0.0.0.0:7007/home/
```

## API for renting the rooms for events

### Example with curl using the API to create a room

```
curl -H "Content-Type: application/json" -X POST -d '{ "room_name": "Blue", "capacity": "100" }' http://0.0.0.0:7007/api/v1/bussiness/create_room/
```

### Example with curl using the API to create an event

```
curl -H "Content-Type: application/json" -X POST -d '{ "event_name": "Weeding", "event_type": "PUBLIC", "room_code": "8172Y2EP" }' http://0.0.0.0:7007/api/v1/bussiness/create_event/
```