
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
                results = "false"
            else:
                results = "true"
                for i in range(2, int(num**0.5)+1):
                    if num % i == 0:
                        results = "false"
                        break
        except:
            results = { 'error_msg' : 'input must be a number' }
            return results, 400
        
        return results , 200


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
    app.run(debug=True, host="0.0.0.0", port=5000)

