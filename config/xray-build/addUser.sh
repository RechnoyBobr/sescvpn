#!/bin/bash

UUID=$(eval "xray uuid")
sed "16i {\"id\": \"$UUID\"}, " ../server-config-example.json >newconf.json

perl -MJSON -e '@text=(<>);print to_json(from_json("@text", {relaxed=>1}), {pretty=>1})' ./newconf.json >newconf2.json
