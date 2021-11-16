import fileinput, platform
for line in fileinput.input(f'/usr/local/venv/lib/python{platform.python_version().split('.')}/site-packages/aredis/connection.py', inplace=True): print(line.replace('loop=self.loop),', '),'), end='')
