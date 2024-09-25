# confnect
STACK:
- vue.js
- FastAPI
- Postgresql
- Docker

## Description
App dedicated to conferences, admins, managers etc. Usually at big events are sections where users can ask.
It could create questions hell without good their managing - our app is for it! Admin can create event on 
our desktop then with one click generate QRCode&invitation code, and all participant can easily join. Then
they can create questions which are show on the screen on live! Admin can easily decide when to reply on 
questions. What's more - participants can send feeback, ask for contact after meet, or take part in live
quizes, polls or other our features!

## Versions
### 0.0.1 - beta
- register/login
- create events
- generate invitation codes
- ask live questions
- send feedback
- send forms on launch page

### 0.0.2
- view questions after meet (optional)
- reply to questions after meet (optional)
- notifications about new replies for attendances (optional)

### 0.0.3
- create votes
- generate votes statistics

### 0.1.0
- send reviews
- check admins profiles
- set events to mode: private | public

### 0.1.1
- create polls

### 0.1.2 
- create quizes

## How to run
### To run backend
`cd backend`
`docker-compose build`
`docker-compose up`
link: `http://0.0.0.0:8000/`
docs: `http://0.0.0.0:8000/docs`

## dev run
`redis-server`
`poetry run celery -A source.celery.celery_app worker --loglevel=info`
`poetry run celery -A source.celery.celery_app beat --loglevel=info`
`poetry run uvicorn source.main:app --reload`