from flask import Flask

app = Flask(__name__)


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)

@app.route('/greet')
@app.route('/greet/<float:celsius>')
def temperature(celsius):
    #celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return "input:{}  Result:{}".format(celsius,fahrenheit)


def hello_world():
    return "<h1>Hello World :)</h1>"


if __name__ == '__main__':
    app.run()
