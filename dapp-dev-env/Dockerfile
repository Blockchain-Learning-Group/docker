# Define and load OS
FROM ubuntu:16.04
MAINTAINER Adam Lemmon "adam@blockchainlearninggroup.com"

# Install Nodejs and npm
FROM node:8.7.0

# Install npm packages, testrpc and truffle
RUN npm install -g ethereumjs-testrpc@4.1.3
RUN npm install -g truffle@4.1.13
RUN npm install -g original-require@1.0.1

RUN apt-get update

# pip3 and py hash lib
RUN apt-get -y install python3-pip
RUN pip3 install pysha3==1.0.2

# Install tmux, window manager
RUN apt-get install tmux

# Define working directory.
WORKDIR /blg/wallet-template

COPY proof_of_work_mining.py /blg
COPY live_chain_pow_mining.py /blg
