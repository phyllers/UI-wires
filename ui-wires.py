import os
import urllib

import webapp2
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render())

class UserDashboardPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/user-dashboard.html')
        self.response.write(template.render())

class ExplorePage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/explore.html')
        self.response.write(template.render())

class ExploreAltPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/explore-alt.html')
        self.response.write(template.render())

class VisListPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/vis-list.html')
        self.response.write(template.render())

class VisItemPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/vis-item.html')
        self.response.write(template.render())

class LoggedInExplorePage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/loggedin-explore.html')
        self.response.write(template.render())

class LoggedInVisListPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/loggedin-vis-list.html')
        self.response.write(template.render())

class LoggedInVisItemPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/loggedin-vis-item.html')
        self.response.write(template.render())

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/signin', UserDashboardPage),
    ('/explore', ExplorePage),
    ('/explore-alt', ExploreAltPage),
    ('/vis', VisListPage),
    ('/vis-item', VisItemPage),
    ('/loggedin-explore', LoggedInExplorePage),
    ('/loggedin-vis', LoggedInVisListPage),
    ('/loggedin-vis-item', LoggedInVisItemPage),
], debug=True)