FROM python:3.10

RUN pip install pipenv

ENV PROJECT_DIR /spaggomatic

WORKDIR ${PROJECT_DIR}

COPY . .

RUN pipenv install --system --deploy

EXPOSE 80

CMD python main.py