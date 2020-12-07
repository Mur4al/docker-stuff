#code here

import signal


def sigterm(x, y):
    pass


signal.signal(signal.SIGTERM, sigterm)

print("hello pipenv-docker-development world!")

signal.sigwait([signal.SIGTERM])

print("shutdown...")
