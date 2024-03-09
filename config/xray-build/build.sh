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
echo $pbk >to.txt
echo $sId >>to.txt
echo $uuid >uuid.txt
while getopts ":rn" opt; do
	case $opt in
	r)
		# There will be script gen for reverse proxy
		cat <<EndOfScript
    {
      "log": {
        "loglevel": "warn"
      },
      "reverse": {
        "portals": [
          {
            "tag": "portal",
            "domain": "reverse.sescvpn.com"
          }
        ]
      },
      "inbounds": [
        {
          "port": 443,
          "protocol": "vless",
          "tag": "vless_tls",
          "settings": {
            "clients": [
              
            ],
            "decryption": "none"
          },
          "streamSettings": {
            "network": "tcp",
            "security": "reality",
            "realitySettings": {
              "show": false,
              "dest": "www.microsoft.com:443",
              "xver": 0,
              "serverNames": [
                "www.microsoft.com",
                "www.github.com"
              ],
              "privateKey": "$pvk",
              "minClientVer": "",
              "maxClientVer": "",
              "maxTimeDiff": 0,
            "shortIds": [
            "$sId"
            ]
            }
          },
          "sniffing": {
            "enabled": true,
            "destOverride": [
              "http",
              "tls"
            ]
          }
        }
      ],
      "outbounds": [
        {
          "protocol": "freedom",
          "tag": "direct"
        },
        {
          "protocol": "blackhole",
          "tag": "block"
        }
      ],
      "routing": {
        "rules": [
          {
            "type": "field",
            "inboundTag": [
              "incoming"
            ],
            "outboundTag": "portal"
          }
        ]
      }
    }
EndOfScript
		;;
	n)
		# There will be script gen for normal mode
		cat <<EndOfScript
    {  
      "log": {
        "loglevel": "info"
      },
      "routing": {
        "rules": [],
        "domainStrategy": "AsIs"
      },
      "inbounds": [
        {
          "port": 443,
          "protocol": "vless",
          "tag": "vless_tls",
          "settings": {
            "clients": [
            ],
            "decryption": "none"
          },
          "streamSettings": {
            "network": "tcp",
            "security": "reality",
        "realitySettings": {
          "show": false,
          "dest": "www.microsoft.com:443",
          "xver": 0,
          "serverNames": [
            "www.microsoft.com"
          ],
          "privateKey": "$pvk",
          "minClientVer": "",
          "maxClientVer": "",
          "maxTimeDiff": 0,
          "shortIds": [
            "$sId"
          ]
        }
          },
          "sniffing": {
            "enabled": true,
            "destOverride": [
              "http",
              "tls"
            ]
          }
        }
      ],
      "outbounds": [
        {
          "protocol": "freedom",
          "tag": "direct"
        }
      ]
    }
EndOfScript
		;;
	esac
done
