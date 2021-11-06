import fileinput
for line in fileinput.input('ha.py', inplace=True): print(line.replace('loop=self.loop),', '),'), end='')
