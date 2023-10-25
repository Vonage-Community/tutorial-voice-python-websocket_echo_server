#!/usr/bin/env python3
from flask import Flask, request, jsonify
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)


@app.route("/webhooks/answer")
def answer_call():
    ncco = [
        {
            "action": "talk",
            "text": "We will now connect you to the echo server, wait a moment then start speaking.",
        },
        {
            "action": "connect",
            "from": "Vonage",
            "endpoint": [
                {
                    "type": "websocket",
                    "uri": f"wss://{request.host}/socket",
                    "content-type": "audio/l16;rate=16000",
                }
            ],
        },
    ]

    return jsonify(ncco)


@app.route("/webhooks/events", methods=["POST"])
def events():
    return "200"


@sock.route("/socket", methods=["GET"])
def echo_socket(ws):
    while True:
        data = ws.receive()
        ws.send(data)
