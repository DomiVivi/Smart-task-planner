# API CONTRACT VERSION 2

## Task Schema

| Параметр | Значение |
|---|---|
|id|UUID|
|title|string|
|description|string|
|status|enum: new, in_progress, done|
|created_at|ISO8601|

## 	Endpoint 1 (Task Service)

POST /api/tasks <br>
Принимает:

| Параметр | Значение |
|---|---|
|title|string|
|description|string|
|status|enum: new|

Возвращает: Task + 201

## Endpoint 2 (Notification Service):
POST /api/webhooks/task_created <br>
Принимает: Task <br>
Возвращает: 200 OK 

## Формат сообщения вебхука
| Параметр | Значение |
|---|---|
|event|task_created|
|timestamp|ISO8601|
|task|{Task}|

