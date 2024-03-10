#!/bin/bash
UUID=$(eval "xray uuid")
echo $UUID >/uuid
sed "/clients\" : \[.*/a\ {\"id\": \"$UUID\"}," /etc/xray/config.json >/etc/xray/temp.json
perl -MJSON -e '@text=(<>);print to_json(from_json("@text", {relaxed=>1}), {pretty=>1})' ./etc/xray/temp.json >/etc/xray/config.json
rm /etc/xray/temp.json
