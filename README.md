# WebScraper

WebScraper is simple flask based application which allows to scrape page source of websites and modife them.

### Installation
- Git clone repo
- Create and activate virtual enviroment 
- Mak sure you have installed redis
- Install depedencis
```
pip install -r requirements.txt
```
- Run bellow commands. Each in new terminal
```
redis-server
```
```
rq-worker
```
```
export APP_SETTINGS=config.cfg
```
```
flask run
```

### Endpoints:

#### /add-task [POST]
- Ads new tasks to the que

##### Headers:
Key | Value
---|---
Content-Type | application/json

##### Parameters:

Name | Required | Type | Description
--- | --- | --- | ---
url | 'required` | string | The url to website which you want to crawl

##### Example Request body data:

```
{
	"url": "http://www.google.com"
}
```

##### Example response:
```
{
    "enqueued_at": "Tue, 02 Feb 2021 18:53:04 GMT",
    "task_id": "287cbb96-db29-4005-99a8-2615f58bafd8",
    "task_status": "queued",
    "website_url": "http://www.google.com"
}
```
#### /results/id [GET]
- Check results of the task 

##### Parameters:

Name | Required | Type | Description
--- | --- | --- | ---
id | 'required` | string | Task Id which results you want to check

##### Example Request:
```
http://127.0.0.1:5000/results/3a8501a9-dd51-4f1b-a89b-35c8f9c16d9c
```
##### Example response:
```
{
"created_at": "2021-02-01 22:40:14.023543",
"result": "22",
"status": "finished",
"task_id": "3a8501a9-dd51-4f1b-a89b-35c8f9c16d9c",
"used_method": "number_of_embeds",
"website_url": "http://www.google.com"
}
```
### Project structure

config.cfg - config file\
run.py - starting file\
app/tasks.py - place for business methods\
app/views.py - routings and controllers of endpoints\
app/helpers.py - helper functions\
app/init.py - init file for flask and db\


### Todos
 - Create more business methods
 - Docker
 - Tests
 

License
----
MIT

Last Updated:
02.02.2021
