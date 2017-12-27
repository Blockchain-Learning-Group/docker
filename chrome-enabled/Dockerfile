# Define and load OS
FROM ubuntu:16.04
MAINTAINER Adam Lemmon "adam@blockchainlearninggroup.com"

# Install Nodejs and npm
FROM node:8.7.0

# Install npm packages, testrpc and truffle
RUN npm install -g ethereumjs-testrpc@4.1.3
RUN npm install -g truffle@3.4.11

# pip3 and  py hash lib
RUN apt-get update
RUN apt-get -y install python3-pip
RUN pip3 install pysha3==1.0.2

# Expose port for the apps to run out of so local browser can connect
EXPOSE 3000

RUN apt-get update; apt-get clean

#######################
# Google Chrome Setup #
#######################
# Add a user for running applications.
RUN useradd apps
RUN mkdir -p /home/apps && chown apps:apps /home/apps

# Install x11vnc.
RUN apt-get install -y x11vnc
# Install xvfb.
RUN apt-get install -y xvfb
# Install fluxbox.
RUN apt-get install -y fluxbox
# Install wget.
RUN apt-get install -y wget
# Install wmctrl.
RUN apt-get install -y wmctrl
# Set the Chrome repo.
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
# Install Chrome.
RUN apt-get update && apt-get -y install google-chrome-stable

COPY start.sh /
RUN ["chmod", "+x", "/start.sh"]
CMD '/start.sh'
