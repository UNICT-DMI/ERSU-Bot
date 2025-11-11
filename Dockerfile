FROM python:3.12-slim
WORKDIR /ersubot/

RUN apt-get update && \
    apt-get install -y locales && \
    sed -i -e 's/# it_IT.UTF-8 UTF-8/it_IT.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales

ENV LANG=it_IT.UTF-8
ENV LC_ALL=it_IT.UTF-8

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT ["python3", "main.py"]
