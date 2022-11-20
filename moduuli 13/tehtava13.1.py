from flask import Flask

app = Flask(__name__)


@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    num = int(luku)
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return {"Number": num, "isPrime": False}
        return {"Number": num, "isPrime": True}
    return {"Number": num, "isPrime": False}


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3999)
