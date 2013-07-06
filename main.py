from boiler.application import TemplateRequestHandler, view, WSGIApplication


class IndexPage(TemplateRequestHandler):
    def get(self):
        self.render_to_response("index.html")


def say_hello(handler):
    return 'Hello world! <a href="index.html">Visit main page</a>'


app = WSGIApplication([
    ('/', view(say_hello)),
    ('/index.html', IndexPage)
])
