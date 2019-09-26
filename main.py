from flask import Flask, render_template, jsonify
import RPi.GPIO as GPIO
app = Flask(__name__)

@app.route('/')
def index():
    # return '<h1>hello world</h1>'
    return render_template('index.html')

@app.route('/turnoff')
def turnoff():
    print('正在关灯')
    GPIO.output(24,GPIO.LOW)
    print('关灯成功')
    return jsonify(success = True)

@app.route('/turnon')
def turnon():
    print('正在开灯')
    GPIO.output(24,GPIO.HIGH)
    print('开灯成功')
    return jsonify(success = True)

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(24,GPIO.OUT)
    app.run(host='0.0.0.0', port=1080, debug=False)
    # app.run(debug=True)