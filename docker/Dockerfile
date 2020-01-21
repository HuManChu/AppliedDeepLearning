From ubuntu:18.04

RUN apt update && apt install -y python3-pip

RUN pip3 install fastai

RUN pip3 install transformers

ADD . /

CMD ["/bin/bash", "run.sh"]
