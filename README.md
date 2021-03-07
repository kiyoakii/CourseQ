# Course Page and Forum

## Installation

Generate MySQL root password for docker

```shell
python3 -c "import secrets; print('MYSQL_ROOT_PASSWORD=%s\n' % secrets.token_hex(32));" >> .env
```

Build and launch the program, in port 2000

```shell
DPORT=2000 docker-compose up
```
