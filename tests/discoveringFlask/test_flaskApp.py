
import flask

app = flask.Flask(__name__)


@app.before_request
def set_up():
    pass


@app.route('/api')
def demo():
    return flask.jsonify({'success': True})


@app.after_request
def tear_down(arg):
    pass


def on_exception(*args, **kwargs):
    print '-------- exception --------'
    print args
    print kwargs


flask.got_request_exception.connect(on_exception)


if __name__ == '__main__':
    app.run()
