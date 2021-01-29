FROM python
WORKDIR "/falcon-app"
COPY ./ssl ./

RUN pip3 install mysql.connector 
RUN pip3 install falcon 
RUN pip3 install jinja2 
RUN pip3 install falcon-jinja2 
RUN pip3 install uwsgi

ARG APP_USER=appuser

RUN useradd -u 1234 $APP_USER

COPY . .

RUN echo $(ls)

EXPOSE 9090

CMD uwsgi --http-socket :9090 --wsgi-file main.py 