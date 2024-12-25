from flask import Flask
from flask import request

app = Flask(__name__ )

# @app.route('/hello')
# @app.route('/哈囉')
# @app.route('/')
# def hello_world():
#     str = '姓名:江晉任<br>學號:B11037102'
#     return str

@app.route('/hello')
@app.route('/哈囉')
@app.route('/')
def hello_world():
    html_content = '''
    <html>
        <head>
            <title>跳到 GitHub</title>
        </head>
        <body>
            <p>姓名: 江晉任</p>
            <p>學號: B11037102</p>
            <p><a href="https://github.com/rexchiang77/python-flask" target="_blank">點我跳到我的 GitHub</a></p>
        </body>
    </html>
    '''
    return html_content
 
if __name__ == '__main__':
    app.run(port=8090, host="0.0.0.0")