import flask

app = flask.Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')


@app.route('/misc')
def misc():
    return flask.render_template('misc.html')


@app.route('/motherboard')
def motherboard():
    return flask.render_template('motherboard.html')


@app.route('/sys_memory')
def sys_memory():
    return flask.render_template('sys_memory.html')



if __name__ == '__main__':
    app.run(debug=True)
