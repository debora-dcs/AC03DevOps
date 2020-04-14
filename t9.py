import os
from flask import Flask, jsonify, request
from math import sq
app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():

    limit = 100

    c = 1
    p = 1
    number = 3

    cousins = "2,"

    while p < limit:
        iscousin = 1
        for i in range(2, number):
            if number % i == 0:
                iscousin = 0
                break
        if (iscousin):
            cousins = cousins + str(number) + ","
            p += 1
            if(p % 10 == 0):
                cousins = cousins + "<br>"
        number+=1

    return cousins


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    
