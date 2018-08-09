#! /bin/bash

# Tag may be provided via env var ie, TAG=2.0.0 ./build-push-image.sh

docker build -t blockchainlg/dapp-dev-env${TAG} .
docker push blockchainlg/dapp-dev-env${TAG}
