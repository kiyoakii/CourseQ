FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY requirements.txt .

RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

COPY ./app /app

EXPOSE 80
