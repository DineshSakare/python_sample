FROM python:3
ADD app.py /
RUN pip install psycopg2
CMD [ "python","-u","./app.py"]
