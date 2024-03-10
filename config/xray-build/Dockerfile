FROM teddysun/xray

COPY ./build.sh /build.sh
COPY ./addUser.sh /addUser.sh
COPY ./main.py /main.py
ARG mode
RUN apk update && apk add bash py3-flask perl-json
RUN apk add --no-cache bash
RUN cd /
RUN  if [[ -z "$mode" ]]; then eval /build.sh -n > /etc/xray/config.json; else eval /build.sh -r > /etc/xray/config.json; fi
CMD ["python3", "/main.py"]
