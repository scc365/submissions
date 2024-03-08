FROM python:3-alpine

RUN  pip install beautifulsoup4 requests pyfiglet

WORKDIR /app
COPY . . 

ENTRYPOINT [ "python3", "submitted.py" ]
