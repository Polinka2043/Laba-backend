FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN git stash
RUN git checkout v1.0

EXPOSE 5001

CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
