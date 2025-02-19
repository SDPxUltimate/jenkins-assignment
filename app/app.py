
from flask import Flask, jsonify 


app = Flask(__name__)

@app.route('/getcode', methods=['GET'])
def getcode():
    return "333"


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

