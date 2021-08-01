from flask import Flask
import pyfirmata

PIN = 13

PORT = 'COM5'

board = pyfirmata.Arduino(PORT)

app = Flask(__name__)

@app.route("/prender")
def prender():

    board.digital[PIN].write(1)
    return "PRENDIDO"


@app.route("/apagar")
def apagar():

    board.digital[PIN].write(0)
    return "APAGADO"


app.run(host="192.168.1.44", port="8080")