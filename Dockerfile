FROM python:3.12-slim
WORKDIR /app

COPY requirements.txt .
RUN apt-get update && apt-get install -y git
RUN pip install -r requirements.txt

COPY back.py .
RUN git stash
RUN git checkout v2.0
EXPOSE 5000
ENV FLASK_APP=back.py
CMD ["flask", "run", "--host=0.0.0.0"]
