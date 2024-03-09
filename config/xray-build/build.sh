#!/bin/bash
array=()
for i in {a..z} {A..Z} {0..9}; do
	array[$RANDOM]=$i
done

sId=$(printf %s ${array[@]::8})
X25519=()
for item in $(eval "xray x25519"); do X25519+=($item); done
pvk=${X25519[2]}
pbk=${X25519[5]}
uuid=$(eval "xray uuid")
