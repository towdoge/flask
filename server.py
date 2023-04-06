from flask import Flask, request
from model import Model
from socket import gethostbyname, gethostname

app = Flask(__name__)


@app.route('/')
def hello_world():
    print('Hello World!')
    print(request.args.get('info'))
    return request.args.__str__()


@app.route('/register', methods=['POST'])
def register():
    # if get post form /register
    print(request.headers)
    print(request.form)
    file = request.form.get('file', '')
    if file:
        model = Model(file)
        model.read_data()
        model.solve()
        model.write()
        # model.error()
        if model.status == 'error':
            # return some error message
            return "error"
    return "finish"


if __name__ == '__main__':
    res = gethostbyname(gethostname())
    app.run(host=res, port=7399, debug=True)
