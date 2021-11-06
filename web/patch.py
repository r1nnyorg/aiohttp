import fileinput, os
for line in fileinput.input(f'/usr/local/venv/lib/python{os.getenv("VERSION")}/site-packages/aredis/connection.py', inplace=True): print(line.replace('loop=self.loop),', '),'), end='')
