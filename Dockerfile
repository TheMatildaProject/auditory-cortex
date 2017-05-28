FROM ubuntu:xenial
MAINTAINER Edward Leoni

# Install dependencies
RUN apt update -y
RUN apt install git python-setuptools python-dev python-pip make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev -y
RUN apt install curl -y
RUN apt install wget -y
RUN pip install virtualenvwrapper
RUN apt-get install -y sudo && rm -rf /var/lib/apt/lists/*


RUN useradd -m python_user

WORKDIR /home/python_user
USER python_user

RUN git clone git://github.com/yyuu/pyenv.git .pyenv

ENV HOME  /home/python_user
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

RUN pyenv install 3.6.1

USER root

## Install google cloud SDK
RUN echo "deb http://packages.cloud.google.com/apt cloud-sdk-xenial main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
RUN apt update -y
RUN apt install google-cloud-sdk -y
RUN apt install google-cloud-sdk-app-engine-python -y

# Include project files
RUN mkdir /app
WORKDIR /app
ADD . .

# Init google SDK
RUN gcloud auth activate-service-account --key-file matilda.json

# Install project dependencies
RUN sudo pip install -r requirements.txt

USER python_user

# Prepares to run project
RUN echo "export FLASK_APP=/app/app.py;  export GOOGLE_APPLICATION_CREDENTIALS=/app/matilda.json; flask run --host=0.0.0.0 --port=5000" > /home/python_user/run.sh

EXPOSE 5000

CMD ["sh", "/home/python_user/run.sh"]
