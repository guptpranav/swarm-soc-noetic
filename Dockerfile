# fetching base image
FROM ubuntu:20.04

# installing basic QoL
RUN apt update
RUN apt install -y software-properties-common
RUN add-apt-repository main
RUN add-apt-repository universe
RUN apt-get install -y sudo

# creating non-root user main
RUN useradd -ms /bin/bash main
RUN usermod -aG sudo main
RUN echo main:main | chpasswd
# setting it as default while running container
USER main