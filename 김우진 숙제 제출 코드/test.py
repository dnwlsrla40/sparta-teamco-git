from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbStock

## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/first_select', methods=['GET'])
def find_first_select():
    selected = request.args.get('selected')
    code = db.codes.find_one({'name': selected})
    print("first",code['code'])
    return jsonify({'data': code['code']})

@app.route('/second_select', methods=['GET'])
def find_second_select():
    selected = request.args.get('selected')
    code = db.codes.find_one({'name': selected})
    print("second",code['code'])
    return jsonify({'data': code['code']})

@app.route('/third_select', methods=['GET'])
def find_third_select():
    selected = request.args.get('selected')
    code = db.codes.find_one({'name': selected})
    print("third",code['code'])
    return jsonify({'data': code['code']})


# # 주문 목록보기(Read) API
# @app.route('/order', methods=['GET'])
# def view_orders():
#     orders = list(db.order.find({}, {'_id': False}))
#     return jsonify({'result': 'success', 'orders':orders})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)