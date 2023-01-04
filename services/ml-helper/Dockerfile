FROM gcr.io/google.com/cloudsdktool/cloud-sdk:alpine

ENV SRC=""

RUN apk add --no-cache bash

ADD start.sh /start.sh
RUN mkdir -p /data
CMD ["/start.sh"]
