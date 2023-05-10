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

@app.route('/feedback', methods=['POST', 'GET'])
def feedback():
    if flask.request.method == 'POST':
        name_param=flask.request.form.get('name')

    elif flask.request.method == 'GET':
        name_param=flask.request.args.get('name')


    if name_param is None:
        name_param=""


    return flask.render_template(
        'feedback.html',
        content=name_param,
    )
    

if __name__ == '__main__':
    app.run(debug=True)
