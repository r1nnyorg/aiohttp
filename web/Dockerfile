FROM python
RUN ["python", "-m", "venv", "--copies", "/usr/local/venv"]
COPY server.pyc /usr/local/venv/
WORKDIR /usr/local/venv
RUN ["bin/pip", "install", "asyncpg", "aredis", "aiokafka", "aiohttp", "aiohttp_cors", "uvloop"]

FROM scratch
ARG VERSION
WORKDIR /usr/local/venv
COPY --from=0 /usr/local/venv .
COPY --from=python:slim /usr/local/lib/libpython$VERSION.so.1.0 /usr/lib/x86_64-linux-gnu/
COPY --from=python:slim /usr/local/lib/python$VERSION /usr/local/lib/python$VERSION/
COPY --from=python:slim /lib/x86_64-linux-gnu /lib/x86_64-linux-gnu/
COPY --from=python:slim /usr/lib/x86_64-linux-gnu /usr/lib/x86_64-linux-gnu/
COPY --from=python:slim /lib64 /lib64/
RUN ["bin/python", "-c", "import fileinput; for line in fileinput.input('/usr/local/venv/lib/python3.10/site-packages/aredis/connection.py', inplace=True): print(line.replace('loop=self.loop),', '),'), end='')"]
ENTRYPOINT ["bin/python", "server.pyc"]
