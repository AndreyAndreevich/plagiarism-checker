FROM python:3.8-slim-buster
WORKDIR /app
ADD . .
#RUN pip3 install -r requirements.txt
CMD python
CMD [ "python3", "main.py"]
