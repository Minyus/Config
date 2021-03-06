# tensorflow official image
FROM tensorflow/tensorflow:1.15.2-py3

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

# Spark dependencies
ENV APACHE_SPARK_VERSION 2.4.5
ENV HADOOP_VERSION 2.7
# Copied from https://downloads.apache.org/spark/spark-2.4.5/spark-2.4.5-bin-hadoop2.7.tgz.sha512
ENV APACHE_SPARK_SHA512_CHECKSUM 2426A20C548BDFC07DF288CD1D18D1DA6B3189D0B78DEE76FA034C52A4E02895F0AD460720C526F163BA63A17EFAE4764C46A1CD8F9B04C60F9937A554DB85D2

RUN apt-get -y update && \
    apt-get install --no-install-recommends -y openjdk-8-jre-headless ca-certificates-java && \
    rm -rf /var/lib/apt/lists/*

RUN cd /tmp && \
    wget -q http://mirrors.ukfast.co.uk/sites/ftp.apache.org/spark/spark-${APACHE_SPARK_VERSION}/spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz && \
    echo "${APACHE_SPARK_SHA512_CHECKSUM} *spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" | sha512sum -c - && \
    tar xzf spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz -C /usr/local --owner root --group root --no-same-owner && \
    rm spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz
RUN cd /usr/local && ln -s spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} spark

# Spark config
ENV SPARK_HOME /usr/local/spark
ENV PYTHONPATH $SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.7-src.zip
ENV SPARK_OPTS --driver-java-options=-Xms1024M --driver-java-options=-Xmx4096M --driver-java-options=-Dlog4j.logLevel=info

# Set the working directory
WORKDIR /usr/local/etc

# Copy the current directory contents into the container
COPY . /usr/local/etc

# make sure pip, virtualenv and setuptools are updated
# RUN python3 -m pip install --upgrade --user pip setuptools

# RUN pip install --upgrade pip

RUN pip install --upgrade keyrings.alt
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

RUN python -m spacy download en

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

# kedro viz
EXPOSE 4141

# mlflow server
EXPOSE 5000

# tensorboard
EXPOSE 6006

# jupyter notebook
EXPOSE 8888

RUN echo 'root:welcomewelcome' | chpasswd
CMD ["/usr/sbin/sshd", "-D"]

COPY .xonshrc /root/
COPY .vimrc /root/

RUN curl -L -O https://github.com/peco/peco/releases/download/v0.5.3/peco_linux_amd64.tar.gz
RUN tar -zxvf peco_linux_amd64.tar.gz && sudo mv peco_linux_amd64/peco /usr/local/bin && rm -rf peco_linux_amd64 peco_linux_amd64.tar.gz

RUN pip3 install git+https://github.com/Minyus/scikit-optimize@depr/fit_params
