import json
import random
import time
from threading import Thread

from flask import Flask, jsonify, request, Blueprint, abort

app = Flask(__name__)

def use_cpu():
    foo = 1
    for x in xrange(10000, 20000):
        foo *= x**3


def use_memory():
    def hold_memory():
        foo = ' ' * 100000000
        time.sleep(60)
    Thread(target=hold_memory).start()


@app.route('/')
def user_list():
    use_cpu()
    return jsonify(users=users)


app.run(host='0.0.0.0', port=80)
