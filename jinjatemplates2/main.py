#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import logging
import jinja2
import sys
import cgi

# Lets set it up so we know where we stored the template files
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class IndexHandler(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('templates/index.html')
    	self.response.write(template.render({'title': 'HOME','subheading': 'HOME','homenav': 'HOME', 'revnav':'Reviews','foodnav':'Food','loginnav':'Login'}))

class FamilyHandler(webapp2.RequestHandler):
    def get(self):
        logthepathfam=self.request.path
        logging.info('the path for family is:'+logthepathfam)
    	template = JINJA_ENVIRONMENT.get_template('templates'+logthepathfam)#path not hardcoded
    	self.response.write(template.render({'title': 'REVIEWS','subheading':'REVIEWS','revnav':'REVIEWS', 'homenav': 'Home','foodnav':'Food','loginnav':'Login'}))



class FoodHandler(webapp2.RequestHandler):
    def get(self):
        logthepathfood=self.request.path
        logging.info('the path for food is:'+logthepathfood)
    	template = JINJA_ENVIRONMENT.get_template('templates'+logthepathfood)#path not hardcoded
    	self.response.write(template.render({'title': 'FOOD','subheading':'FOOD','revnav':'Reviews', 'homenav': 'Home','foodnav':'FOOD','loginnav':'Login'}))

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        msgdok=""
        template = JINJA_ENVIRONMENT.get_template('templates/login.html')
        self.response.write(template.render({'title': 'LOGIN','subheading':'LOGIN','msg':msgdok, 'revnav':'Reviews', 'homenav': 'Home','foodnav':'Food','loginnav':'LOGIN'}))
    def post(self):
        logun=self.request.get('un')
        logp=self.request.get('p')
        logging.info('username before if condition:'+logun)
        logging.info('password before if condition:'+logp)
        if (self.request.get('un')=="Colleen" and self.request.get('p')=="pass"):
            logging.info('correct user name:'+logun)
            logging.info('correct password:'+logp)
            template = JINJA_ENVIRONMENT.get_template('templates/loggedin.html')
            self.response.write(template.render({'title': 'LOGGED IN','subheading':'LOGGED IN..','revnav':'Reviews', 'homenav': 'Home','foodnav':'Food','loginnav':'LOGIN'}))
        else:
            logging.info('incoreect username:'+logun)
            logging.info('incorrect password:'+logp)
            msgdbad="Bad credentials, please try again"
            template = JINJA_ENVIRONMENT.get_template('templates/login.html')
            self.response.write(template.render({'title': 'LOGIN','subheading':'LOGIN','msg':msgdbad, 'revnav':'Reviews', 'homenav': 'Home','foodnav':'Food','loginnav':'LOGIN'}))
    
app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/index.html', IndexHandler),
    ('/reviews.html', FamilyHandler),
    ('/food.html', FoodHandler),
    ('/log.*',LoginHandler)
], debug=True)

