FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y git
COPY . .

RUN git stash
RUN git checkout v1.0

EXPOSE 5001
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
