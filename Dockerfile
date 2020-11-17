FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install -U textblob

RUN pip install Werkzeug==0.16.1

COPY . .

CMD [ "python", "./run.py" ]