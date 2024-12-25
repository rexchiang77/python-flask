from flask import Flask
from flask import request

app = Flask(__name__ )

@app.route('/hello')
@app.route('/哈囉')
@app.route('/')
def hello_world():
    str = '姓名:江晉任<br>學號:B11037102'
    return str
 
if __name__ == '__main__':
    app.run(port=5155, host="140.118.150.191")