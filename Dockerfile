FROM python:3.11
WORKDIR /python-app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["python", "-m", "app.main"]
