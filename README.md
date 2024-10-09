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

## Notes
Frontend is not ready to use. Backend is finished. Copy `.env.sample` to `.env`. If you need some private info for development
      -> contact me kamilf827@gmail.com

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