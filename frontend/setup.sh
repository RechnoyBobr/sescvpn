IP=$(cat ./ip.txt)
RES="BACKEND_HOST=${IP}"
echo $RES >.env.local
