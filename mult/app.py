import json
from bottle import Bottle, HTTPResponse, request

app = Bottle()

@app.route("/mult", methods=["GET"])
def mult():
    res = {}
    op1 = request.query.get('op1')
    op2 = request.query.get('op2')

    if not op1 or not op2:
        res['resultado'] = "op1 ou op2 não informado"
        return HTTPResponse(
            status=400,
            body=json.dumps(res),
            headers={'Content-Type': 'application/json'},
        )

    res['resultado'] = float(op1) * float(op2)
    return HTTPResponse(
        status=200,
        body=json.dumps(res),
        headers={'Content-Type': 'application/json'},
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)