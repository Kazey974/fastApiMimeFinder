# fastApiMimeFinder

Welcome to my MIME Type finder !

## Installation

Via a docker container :

```
docker build -t mime-server .
docker run -p 8080:8080 mime-server
```

Or install and launch locally :
```
pip install -r requirements.txt
python app/main.py
```

## Usage

You can now find out your file actual MIME type.

Send it to `http://localhost:8080/mime-type` with a curl :
```
curl -F 'myfile=@pathToFile' http://localhost:8080/mime-type
```

Or use the form available on `http://localhost:8080/`
