FROM python:3.9-alpine

RUN apk update
RUN pip install --no-cache-dir pipenv

WORKDIR /usr/src/app
COPY Pipfile Pipfile.lock bootstrap.sh ./
COPY LangPars ./LangPars

RUN pipenv install

EXPOSE 5000
RUN chmod +x bootstrap.sh
ENTRYPOINT ["/usr/src/app/bootstrap.sh"]