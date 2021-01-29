import falcon
import mysql.connector
import json

from falcon_jinja2 import FalconTemplate
from db import MysqlConnection

falcon_template = FalconTemplate(path='./templates')
mysql = MysqlConnection()


class IndexAll:
    @falcon_template.render('index.html')
    ###ONGET###
    def on_get(self, req, resp):
        data = mysql.listAll(10)
        resp.context = {'data': data}

class GetByID:
    @falcon_template.render('getbyid.html')
    ###ONGET###
    def on_get(self,req,resp, id):
        record = mysql.getById(id)
        resp.context = {'record': record}

class DeleteById:
    @falcon_template.render('delete.html')
    ###ONGET###
    def on_get(self, req, resp, id):
        detail = mysql.deleteById(id)
        resp.context = {'detail': detail}

class Status:
    @falcon_template.render('status.html')
    ###ONGET###
    def on_get(self, req, resp):
        resp.body = falcon.HTTP_200      

class UpdateById:
    @falcon_template.render('update.html')
    ###ONGET###
    def on_get(self, req, resp, id):
        record = mysql.getById(id)
        resp.context = {'record' :record}
    ###ONPOST###
    def on_post(self, req, resp, id):
        print(req.params)
        company_name=str(req.params["company_name"])
        print(company_name)
        location=req.params["location"]
        date=req.params["date"]
        detail=req.params["detail"]
        rocket_status=req.params["rocket_status"]
        rocket=req.params["rocket"]
        mission_status=req.params["mission_status"]
        mysql.updateById(id, company_name, location, date, detail, rocket_status, rocket, mission_status)

class Login:
    @falcon_template.render('login.html')
    ###ONGET###
    def on_get(self, req, resp):
            error = ''
            resp.context = {'error' : error}
    ###ONPOST###
    def on_post(self, req, resp):
        error = ''
        username = req.params["username"]
        password = req.params["password"]
        print(username)
        # record = mysql.loginGetByUsername(username)
        # if username != record[0][0] or password != record[0][1]:
        if username != 'admin' or password != 'admin':
            error = 'Podales niepoprawne dane logowania - sprobuj jeszcze raz.'
            LoginFailed.on_get(self, req, resp, error)
        else:
            application.add_route('/index/{id}', GetByID())
            application.add_route('/index', IndexAll())
            application.add_route('/delete/{id}', DeleteById())
            application.add_route('/update/{id}', UpdateById())
            IndexAll.on_get(self, req, resp)

class LoginFailed:
    @falcon_template.render('loginfailed.html')
    ###ONGET###
    def on_get(self, req, resp, error):
        resp.context = {'error' : error}
    ###ONPOST###
    def on_post(self, req, resp, error):
        Login.on_get(self, req, resp)

application = falcon.API()
application.req_options.auto_parse_form_urlencoded = True
application.add_route('/', Login())
application.add_route('/status', Status())