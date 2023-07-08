FROM python:3.10

RUN pip install pipenv

ENV PROJECT_DIR /spaggomatic

WORKDIR ${PROJECT_DIR}

COPY . .

RUN pipenv install --system --deploy

RUN apt-get update && apt-get -y install cron
COPY cron/sync_cron /etc/cron.d/sync_cron
RUN chmod 0644 /etc/cron.d/sync_cron
RUN crontab /etc/cron.d/sync_cron

EXPOSE 80
CMD cron && python main.py