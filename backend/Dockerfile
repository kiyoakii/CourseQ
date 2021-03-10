FROM python:3.8-buster
RUN echo \
    deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster main contrib non-free \
    deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-updates main contrib non-free \
    deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-backports main contrib non-free \
    > /etc/apt/sources.list && \
    apt update && \
    apt install -y python3 libmariadb-dev-compat libmariadb-dev&& \
    wget -O /wait.sh https://cdn.jsdelivr.net/gh/vishnubob/wait-for-it@master/wait-for-it.sh && \
    chmod +x /wait.sh
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt --no-cache-dir

ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY . .
RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
