FROM python:3.9-slim

# メタ情報の付与
LABEL maintainer="shin1008@gmail.com"
LABEL version="1.0"
LABEL description="env_scikitlearn"

# パッケージのインストール
RUN apt-get update && apt-get install -y \
tzdata \
&& rm -rf /var/lib/apt/lists/*

# モジュールのインストール
WORKDIR /tmp/work
COPY requirements.txt ${PWD}
RUN pip install -r requirements.txt

# 環境変数の定義
ENV TZ=Asia/Tokyo
ENV USER shin1008

# 一般権限のユーザを追加
RUN useradd -m ${USER} --uid 1000
RUN gpasswd -a ${USER} sudo
RUN echo "${USER}:password" | chpasswd

# ユーザの切り替え
USER ${USER}