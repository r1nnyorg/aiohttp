import fileinput
for line in fileinput.input(f'/usr/local/venv/lib/python/site-packages/aredis/connection.py', inplace=True): print(line.replace('loop=self.loop),', '),'), end='')
