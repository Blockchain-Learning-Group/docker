#!/bin/bash
appPort=3000 # unique port for the app
rpcPort=8545 # unique port for the rpc

# Users to create containers for
users=( adamjlemmon mtawawala )

# Clearing the created containers
if [ "$1" == "clearall" ]
then
  for user in "${users[@]}"
  	do
  		echo "Removing Container for: $user"
      docker stop $user && docker rm $user
  	done

# Creating containers for all users
else
  for user in "${users[@]}"
  	do
  		echo "New Container for: $user"
      # Start a contianer for each participant
      docker run -dit -p $appPort:3000 -p $rpcPort:8545 -v /home/adam/Desktop/blg:/blg --name=$user blockchainlg/dapp-dev-env
      appPort=$((appPort+1))
      rpcPort=$((rpcPort+1))
  	done
fi
