FROM python:3.9-slim

# メタ情報の付与
LABEL maintainer="shin1008@gmail.com"
LABEL version="1.0"
LABEL description="ex02"

# 作業ディレクトリを変更
WORKDIR /tmp/mydir

COPY requirements.txt ${PWD}

RUN pip install -r requirements.txt
ARG wdir
WORKDIR $wdir
