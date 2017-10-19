FROM alpine

RUN apk update
RUN apk add python

ADD badrik.py /

CMD [ "python", "./badrik.py" ]