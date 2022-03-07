FROM python:3.10.2-alpine


RUN mkdir -p /home/app/
COPY . /home/app/
RUN pip install flask

WORKDIR /home/app/
ENTRYPOINT ["python"]
RUN cd /home/app/
CMD ["main.py"]