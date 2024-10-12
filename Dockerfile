FROM python:3.12-slim
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y git
COPY . .
RUN git stash
RUN git checkout v2.0
EXPOSE 5001
ENV FLASK_APP=back
CMD ["flask", "run", "--host=0.0.0.0"]
