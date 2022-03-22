FROM python
RUN ["python", "-m", "venv", "--copies", "/usr/local/venv"]
COPY server.pyc patch.pyc ca.crt client.root.crt client.root.key /usr/local/venv/
WORKDIR /usr/local/venv
RUN ["bin/pip", "install", "asyncpg", "aredis", "aiokafka", "aiohttp", "aiohttp_cors", "uvloop"]
RUN ["bin/python", "patch.pyc"]

FROM scratch
ENV PYTHONPATH=/usr/local/lib/python:/usr/local/lib/python/site-packages:/usr/local/lib/python/lib-dynload password=''
WORKDIR /usr/local/venv
COPY --from=0 /usr/local/venv .
COPY --from=python:slim /usr/local/lib/libpython*.so.1.0 /usr/lib/x86_64-linux-gnu/
COPY --from=python:slim /usr/local/lib/python* /usr/local/lib/python/
COPY --from=python:slim /lib/x86_64-linux-gnu /lib/x86_64-linux-gnu/
COPY --from=python:slim /usr/lib/x86_64-linux-gnu /usr/lib/x86_64-linux-gnu/
COPY --from=python:slim /lib64 /lib64
ENTRYPOINT ["bin/python", "server.pyc"]
