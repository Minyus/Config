# tensorflow official image
FROM tensorflow/tensorflow:1.13.0rc0-py3

# Set the working directory
WORKDIR /usr/local/etc

# Copy the current directory contents into the container
COPY . /usr/local/etc

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt
