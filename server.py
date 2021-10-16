import http.server


def header_printer(headers):
    print("\n----------")
    for k, v in headers.items():
        print(k + ": " + v)


def main(*, port):
    class OpCheckSimpleHTTPServer(http.server.SimpleHTTPRequestHandler):

        def end_headers(self):
            # self.send_header([HEADER_NAME], [HEADER_VALUE])
            self.send_header("received-headers", dict(self.headers))
            super().end_headers()

        def do_GET(self):
            header_printer(dict(self.headers))
            http.server.SimpleHTTPRequestHandler.do_GET(self)

    httpServer = http.server.HTTPServer(('', port), OpCheckSimpleHTTPServer)
    httpServer.serve_forever()


if "__main__" == __name__:
    main(port=80)
