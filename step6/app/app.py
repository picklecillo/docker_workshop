from flask import Flask

from worker import add_to_hits, celery

app = Flask(__name__)


def add_to_hits_task_result():
    result = add_to_hits.delay()
    while not result.ready():
        result = celery.AsyncResult(result.task_id)

    return str(result.get())


@app.route('/')
def hello_world():
    result = add_to_hits_task_result()

    return f'Hello World! {result} hits'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
