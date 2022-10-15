FROM python:3-slim
WORKDIR /ersubot/

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT ["python3", "main.py"]
