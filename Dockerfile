# Linux x64
FROM ubuntu:latest

# Copy files
COPY . /usr/workspace


ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Moscow 

#install python
RUN apt update
RUN apt install -y python3-pip


#install chrome
RUN apt install -y wget
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt install -y ./google-chrome-stable_current_amd64.deb
#RUN printf "y\n13\n8\n" | apt install ./google-chrome-stable_current_amd64.deb

#install chrome drive
RUN wget -N http://chromedriver.storage.googleapis.com/93.0.4577.63/chromedriver_linux64.zip
RUN apt-get install unzip
RUN unzip chromedriver_linux64.zip
RUN chmod +x chromedriver
RUN mv -f chromedriver /usr/local/share/chromedriver
RUN ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
RUN ln -s /usr/local/share/chromedriver /usr/bin/chromedriver

#add pip packeges
RUN pip install selenium
RUN pip install lxml

WORKDIR /usr/workspace
CMD ["python3", "./test_buyme.py"]

