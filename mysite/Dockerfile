FROM python:3.10
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
# mysiteフォルダの中身をコンテナの/codeにコピー
COPY . /code/
RUN pip install --no-cache-dir -r requirements.txt
# 起動コマンド
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
