from flask import Flask, render_template
from templates.index import index

app = Flask(__name__)

# 首页
app.register_blueprint(index.index)


@app.route('/pages/about')
def about():
    return render_template('./pages/about.html')


@app.route('/pages/help')
def help():
    return render_template('./pages/help.html')


@app.route('/pages/root')
def root():
    return render_template('./pages/root.html')


@app.route('/pages/output')
def output():
    return render_template('./pages/output.html')


@app.route('/pages/familiar')
def familiar():
    return render_template('./pages/familiar.html')


@app.route('/pages/websit')
def websit():
    return render_template('./pages/websit.html')


if __name__ == "__main__":
    app.run(debug=True, port=14638)
