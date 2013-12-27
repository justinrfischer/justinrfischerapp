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
import os
import webapp2
import jinja2
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
			 autoescape = False)


class Handler(webapp2.RequestHandler):
		def write(self, *a, **kw):
			self.response.out.write( *a, **kw)

		def render_str(self, template, **params):
			t = jinja_env.get_template(template)
			return t.render(params)

		def render(self, template, **kw):
			self.write(self.render_str(template, **kw))

class ExtrasPage(Handler):

	def get(self):
		
		self.render("header.html", info="")
		
		self.render("extrasbody.html", info="")

		extrasEntries = db.GqlQuery("SELECT * FROM ExtrasEntry ORDER BY created DESC ")

		links={}
		for entry in extrasEntries:
			links['id'] = str(entry.key().id())

		self.render("extraspost.html", extrasEntries=extrasEntries, links=links)

		self.render("footer.html", info="")

class ExtrasPostPage(Handler):

	def get(self):

		self.render("header.html", info="")

		self.render("extrasnewpost.html", info="")

		self.render("footer.html", info="")

	def post(self):
		subject = self.request.get("subject")
		content = self.request.get("content")
		contentUrl = self.request.get("contentUrl")
		summary = self.request.get("summary")
		titleImageUrl = self.request.get("titleimageurl")

		if subject and content and summary and titleImageUrl:
			eEntry= ExtrasEntry(subject=subject, content=content, contentUrl=contentUrl, summary=summary, titleImageUrl=titleImageUrl)
			eEntry.put()

			self.redirect("/extras")
		else:
			error = "We need both a subject and some content."
			#ExtrasPostPage().get()
			self.redirect("/extrasnewpost")

class ExtraslinkPage(Handler):

	def get(self, entryId):

		self.render("header.html", info="")

		entry = ExtrasEntry.get_by_id(int(entryId))

		if entry:
			self.render(entry.contentUrl, info="")

		self.render("footer.html", info="")

class DemoReelPage(Handler):

	def get(self):
		
		self.render("header.html", info="")

		self.render("demoreelbody.html", info="")

		self.render("footer.html", info="")

class ResumePage(Handler):

	def get(self):

		self.render("header.html", info="")

		self.render("resumebody.html", info="")

		self.render("footer.html", info="")

class MainPage(Handler):

	def get(self):

		self.render("header.html", info="")

		self.render("body.html", info="")

		self.render("footer.html", info="")

class ExtrasEntry(db.Model):
	subject = db.StringProperty(required=True)
	content = db.TextProperty(required=True)
	contentUrl = db.TextProperty(required=True)
	summary = db.TextProperty(required=True)
	titleImageUrl = db.TextProperty(required=True)
	created = db.DateTimeProperty(auto_now_add=True)



	
app = webapp2.WSGIApplication([('/', MainPage), ('/resume', ResumePage), ('/demoreel', DemoReelPage), ('/extras', ExtrasPage), ('/extrasnewpost', ExtrasPostPage),  ('/([0-9]+)', ExtraslinkPage)], debug=True)

