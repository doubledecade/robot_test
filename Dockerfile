FROM python:3.7

ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV PORT=程序端口号
ENV WEROBOT_TOKEN=微信公众号的TOKEN

CMD ["python", "app.py"]