IP=$(ip -o route get to 8.8.8.8 | sed -n 's/.*src \([0-9.]\+\).*/\1/p')
echo $IP >./config/xray-build/ip.txt
echo $IP >./frontend/ip.txt
