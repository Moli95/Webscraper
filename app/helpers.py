from app import app
from app import db, Results
from rq import get_current_job

def get_result(id):
    return Results.query.filter_by(id=id).first()

def is_result_exist(id):
    return Results.query.filter_by(id=id).count()

def save_results(data, url):
    job = get_current_job()
    result = Results(
        id=job._id,
        website_url=url,
        used_method=app.config['USED_METHOD'],
        created_at=job.created_at,
        result=data
    )
    db.session.add(result)
    db.session.commit()    
