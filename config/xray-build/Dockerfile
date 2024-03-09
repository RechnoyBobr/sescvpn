FROM teddysun/xray

COPY ./build.sh /build.sh
ARG mode
RUN apk update && apk add bash
RUN apk add --no-cache bash
RUN apk add perl-json
RUN cd /
RUN  if [[ -z "$mode" ]]; then echo $(eval /build.sh -n > /etc/xray/config.json); else echo $(eval /build.sh -r > /etc/xray/config.json); fi
