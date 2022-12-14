FROM python:3.9-alpine

COPY requirements.txt /requirements.txt
#更改安装源
COPY sources.list /sources.list
RUN cat /sources.list > /etc/apk/repositories
RUN apk update
RUN apk add ffmpeg

# 删除缓存文件和虚拟包
RUN pip install -r /requirements.txt \
    && rm -rf .cache/pip


ENV app /app
WORKDIR ${app}
ADD . $app

# 自己的部分
CMD ["python3", "main.py"]


