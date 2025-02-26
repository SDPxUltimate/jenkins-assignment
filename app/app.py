
from flask import Flask, jsonify 


app = Flask(__name__)

@app.route('/getcode', methods=['GET'])
def getcode():
    return "333"

@app.route('/is_prime/<num>', methods=['GET'])
def is_prime(num):
    with app.app_context():
        try:
            num = int(num)
            if num < 2:
                results = False
            else:
                results = True
                for i in range(2, int(num**0.5)+1):
                    if num % i == 0:
                        results = False
                        break
        except:
            results = { 'error_msg' : 'input must be a number' }
            res = jsonify(results)
            return results, 400

        resp = jsonify(results)
        
        return resp, 200

@app.route('/cir_sur/<num>', methods=['GET'])
def cir_sur(num):
    with app.app_context():
        try:
            num = float(num)
            if num < 0:
                results = 0.00
            else:
                results = 4 * 3.14 * pow(num, 2)
        except:
            results = { 'error_msg' : 'input must be a number' }
            res = jsonify(results)
            return results, 400

        resp = jsonify(results)
        
        return resp, 200


@app.route('/plus/<num1>/<num2>', methods=['GET'])
def plus(num1, num2):
    with app.app_context():
        try:
            num1 = float(num1)
            num2 = float(num2)
            ans = num1 + num2
            if ans.is_integer():
                ans = int(ans)
            results = { 'result' : ans}

        except:
            results = { 'error_msg' : 'inputs must be numbers' }
            res = jsonify(results)
            return res, 400

        
        res = jsonify(results)
        
        return res, 200


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)

