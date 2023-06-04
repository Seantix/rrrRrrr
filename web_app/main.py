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
        review_param=flask.request.form.get('review')

    elif flask.request.method == 'GET':
        review_param=flask.request.args.get('review')


    if review_param is None:
        review_param=""


    return flask.render_template(
        'feedback.html',
        content=review_param,
    )
    

if __name__ == '__main__':
    app.run(debug=True)
