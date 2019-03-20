FROM python:3.6-alpine

COPY . /app
WORKDIR /app

RUN pwd

RUN ls

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]