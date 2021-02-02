from app import app
from app import r
from app import q
from app import jsonify
import validators
from flask import request
from app.tasks import task_handler
from app.helpers import get_result, is_result_exist

@app.route("/add-task", methods=["POST"])
def add_task():
    url = request.get_json()['url']
    if not validators.url(url):
        return jsonify(
            status="Please insert a valid website URL."
        ), 400
    task = q.enqueue_call(
        func=task_handler, args=(url,)
    )
    return jsonify(
        task_id=task._id,
        enqueued_at=task.enqueued_at,
        task_status=task._status,
        website_url=url
    )

@app.route("/results/<id>", methods=["GET"])
def check_task(id):
    task = q.fetch_job(id)
    if task is None:
        if not is_result_exist(id):
            return jsonify(
                status='Notexist',
                task_id=id
            ), 400
        else:
            result = get_result(id)
            return jsonify(
                status='finished',
                task_id=id,
                website_url=result.website_url,
                used_method=result.used_method,
                created_at=result.created_at,
                result=result.result
            ), 200        
    elif task._status == 'queued':
        return jsonify(
            status=task._status,
            task_id=id,
            enqueued_at=task.enqueued_at
        ), 200
    elif task._status == 'finished':
        result = get_result(id)
        return jsonify(
            status=task._status,
            task_id=id,
            website_url=result.website_url,
            used_method=result.used_method,
            created_at=result.created_at,
            result=result.result
        ), 200
