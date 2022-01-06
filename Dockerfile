FROM python:3.8.10-buster

WORKDIR /usr/local/app
RUN pip3 install flask pymupdf

COPY cutter.py server.py ./

EXPOSE 5000
CMD [ "python3", "server.py" ]