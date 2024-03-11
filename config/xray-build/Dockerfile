FROM teddysun/xray

COPY ./build.sh /build.sh
COPY ./addUser.sh /addUser.sh
COPY ./main.py /main.py
COPY ./kill.sh /kill.sh
RUN apk update && apk add bash py3-flask perl-json
RUN apk add --no-cache bash
RUN chmod +x /kill.sh
EXPOSE 6000
WORKDIR  /
ENTRYPOINT [ "python" ]
CMD ["/main.py"]
