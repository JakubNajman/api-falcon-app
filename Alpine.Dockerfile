FROM google/cloud-sdk:alpine

RUN apk add gettext
RUN apk add py-pip
RUN apk add python3-dev
RUN apk add libffi-dev
RUN apk add openssl-dev
RUN apk add gcc
RUN apk add libc-dev
RUN apk add make
RUN pip install docker-compose

