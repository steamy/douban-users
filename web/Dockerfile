FROM python:3.6.5

#WORKDIR /spidersite
ADD . /site
WORKDIR /site

RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple/ -r requirements.txt

EXPOSE 8000

CMD python ./spidersite/manage.py runserver 0.0.0.0:8000