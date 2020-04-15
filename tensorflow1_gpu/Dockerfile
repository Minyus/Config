
# tensorflow official image
FROM tensorflow/tensorflow:1.15.2-gpu-py3

# Reference Dockerfile from https://hub.docker.com/r/jupyter/pyspark-notebook/dockerfile

USER root

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get -yq dist-upgrade && \
    apt-get install -yq --no-install-recommends \
    apt-utils \
    wget \
    bzip2 \
    ca-certificates \
    sudo \
    locales \
    fonts-liberation \
    build-essential \
    git \
    libsm6 \
    libxext-dev \
    libxrender1 \
    pandoc \
    tzdata \
    unzip \
    libxext6 \
    libxrender-dev \
    graphviz \
    libgraphviz-dev \
    pkg-config \
    ffmpeg \
    curl \
    net-tools \
    openssh-server \
    xauth \
    tmux \
    tree \
    vim \
    libgmp-dev libmpfr-dev libmpc-dev \
    x11-apps \
    curl \
    net-tools \
    htop &&\
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /usr/local/etc

# Copy the current directory contents into the container
COPY . /usr/local/etc

# make sure pip, virtualenv and setuptools are updated
# RUN python3 -m pip install --upgrade --user pip setuptools

# RUN pip install --upgrade pip

RUN pip install --upgrade keyrings.alt
# Install any needed packages specified in requirements.txt

# Set up sshd
# RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd

# RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config
RUN echo 'X11UseLocalhost no' >> /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile
RUN sed -i '1 i[ -z "$PS1" ] && return\n' /etc/bash.bashrc


RUN update-locale LANG=C.UTF-8

# SSH
EXPOSE 22

# tensorboard
EXPOSE 6006

RUN echo 'root:welcomewelcome' | chpasswd
CMD ["/usr/sbin/sshd", "-D"]
