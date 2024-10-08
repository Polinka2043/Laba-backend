FROM python:3.12-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY back.py .

EXPOSE 5000
ENV FLASK_APP=back.py
CMD ["flask", "run", "--host=0.0.0.0"]
