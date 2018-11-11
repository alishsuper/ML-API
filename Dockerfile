FROM ubuntu:14.04
MAINTAINER Alisher Mukashev <ali_2475@mail.ru>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get -y install python-pip python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose python-sklearn

copy python-app /var/python-app

copy cfg /etc/cfg

RUN pip install -r /etc/cfg/python-deps.txt

ENV FLASK_PORT 8080

EXPOSE $FLASK_PORT

CMD ["/usr/bin/python","/var/python-app/wine_model.py"]
