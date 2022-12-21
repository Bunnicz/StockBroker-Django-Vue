## Project Overview

Simple Fullstack App using Django and VueJS with user login/register page, which displays world stock data after user authentication with JWT. Stock Data is fetched every 5 secounds from outside service and cached to redis (noSQL) DB for fast procesing.


### Used technologies:

- **Backend**: Django

- **Frontend**: VueJS

- **DataBase**: PostgreSQL

- Other:
  - **Distributed Task Queue**: Celery
  - **Cache Database/Message Broker**: Redis

## Local Development

First, copy `.env.template` to a new file in the project's root directory called `.env`. This file will be read by `docker-compose` in the next step. Adjust any of the values in this file if needed, or add new variables for any secret information you need to pass to docker-compose (or to docker containers).

```sh
docker-compose up
```

Open `http://localhost` in your browser.

You can specify environment variables for docker-compose by adding an `.env` file to the root of the project based on `.env.template`.

Connect to "Backend" container, make migration for DB and create super user:

```sh
docker exec -it Backend bash
python manange.py migrate
python manange.py createsuperuser --email admin@example.com --username admin
```

## To Do:

- [ ] JWT refresh implementation. Currently after token expiration user gets logged out.
- [ ] isAuthenticated bug fix. Currently dosen't hide Login/Register buttons when logged in. In progress...
- [ ] Frontend client beautification. 
- [ ] Frontend standarization
