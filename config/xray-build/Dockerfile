FROM teddysun/xray

COPY ./build.sh /build.sh
COPY ./addUser.sh /addUser.sh
COPY ./main.py /main.py
COPY ./kill.sh /kill.sh
ARG mode
RUN apk update && apk add bash py3-flask perl-json
RUN apk add --no-cache bash
WORKDIR  /
CMD ["python3", "/main.py"]
