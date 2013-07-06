from boiler import application


class IndexPage(application.TemplateRequestHandler):
    def get(self):
        self.render_to_response("index.html")


def say_hello(handler):
    return 'Hello world!'


def say_hi(handler):
    handler.response.write('Hi world!')


def index_page(handler):
    handler.render_to_response("index.html")


app = application.WSGIApplication([
    ('/say-hello', application.view(say_hello)),
    ('/say-hi', application.view(say_hi)),
    ('/index.html', application.view(
        index_page, handler_class=application.TemplateRequestHandler)),
    ('/', IndexPage)
])
