

import tornado.ioloop
import tornado.web

class MainHanlder(tornado.web.RequestHandler):
    def get(self):
        title = "danger!"
        bgcolor = "darkred"
        self.render("template.html", title=title, bgcolor=bgcolor)

        print(self.request)


def make_app():
    return tornado.web.Application([
        (r"/", MainHanlder),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
