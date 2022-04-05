FROM amancevice/pandas:1.4.2-alpine


RUN mkdir -p /home/app/
COPY . /home/app/
RUN pip install flask
RUN pip install sqlalchemy
RUN pip install lxml

EXPOSE 5000
WORKDIR /home/app/
ENTRYPOINT ["python"]
RUN cd /home/app/
CMD ["main.py"]