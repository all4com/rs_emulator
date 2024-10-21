FROM python:3.9.2

# アプリケーションディレクトリを作成する
WORKDIR /work

# pipのアップデート
RUN pip install --upgrade pip

# pipでインストールしたいモジュールをrequirements.txtに記述しておいて、
# コンテナ内でpipにインストールさせる
# requirements.txtの書き方は[pip freeze]コマンドから参考に出来る
COPY requiriments.txt .
RUN pip install -r requiriments.txt

# アプリケーションコードをコンテナにコピー
# COPY . .

# EXPOSE 8000
# CMD [ "python", "-m", "http.server", "55661" ]
CMD [ "python", "-m", "login.login" ]
# CMD ["./exec.sh"]