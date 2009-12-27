#!/usr/bin/env python
if __name__ == '__main__':
      from flup.server.fcgi_fork import WSGIServer
      from django.core.handlers.wsgi import WSGIHandler
      WSGIServer(WSGIHandler()).run()


