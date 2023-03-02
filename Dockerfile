FROM python:3
ADD requirements.txt /
RUN pip install -r requirements.txt
ADD manage.py /
ADD db.sqlite3 /
ADD templates /
ADD httpApp /
ADD DDoS /
ADD Clients_net /
CMD ["python", "./manage.py", "runserver"]