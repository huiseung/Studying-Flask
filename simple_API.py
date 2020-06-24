from flask import Flask

app = Flask(__name__)

@app.route("/ping", methods=["GET"])
def ping():
    return "pong"

"""
ping함수를 엔드포인트로 등록
고유주소는 "/ping", http 메소드는 "GET"
"""