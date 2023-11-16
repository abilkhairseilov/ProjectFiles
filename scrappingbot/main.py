from contextlib import redirect_stdout


with open('logs.txt', 'a+') as f:
    with redirect_stdout(f):
