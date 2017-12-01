FROM python:3
ADD ./requirements.txt  /requirements.txt 
RUN pip install -r /requirements.txt  && \
    rm /requirements.txt
RUN  echo "Asia/Shanghai" > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata
