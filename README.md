# NumAPI v0.0.1

NumAPI is Numbersapi test assignment done by Deniss Kaahin. Time spent: 4 hours

## Installation

You need to have docker installed. I used FastApi and Python 3.9 (I heard you used it as well). 
Run these commands from main directory:

```bash
docker build -t numapi .
docker run -d --name numapi -p 8090:80 numapi
```

I used port 8090, just to not compete with other local projects, you can use any, even 80:80 :)
App will be available at the address http://localhost:8090

## Usage

### Documentation:
http://localhost:8090/docs
http://localhost:8090/redoc

### Testing
Run from main directory
```bash
docker exec -it numapi /bin/bash
cd app
pytest
```

Test coverage report
```bash
docker exec -it numapi /bin/bash
cd app
coverage run -m pytest
coverage report -m
```
