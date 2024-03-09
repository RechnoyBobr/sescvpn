#!/bin/bash

UUID=$(eval "xray uuid")
sed "/clients\": \[/a\ {\"id\": \"$UUID\"}," ../server-config-example-reverse.json >newconf.json

perl -MJSON -e '@text=(<>);print to_json(from_json("@text", {relaxed=>1}), {pretty=>1})' ./newconf.json >config.json
#rm ./newconf.json
