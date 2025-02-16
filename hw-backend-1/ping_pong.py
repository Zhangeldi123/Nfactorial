def application(environ, start_response):
    path = environ.get('PATH_INFO', '/')
    method = environ.get('REQUEST_METHOD', '')

    if path == '/ping' and method == 'GET':
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return [b'pong']
    else:
        start_response('404 Not Found', [('Content-Type', 'text/plain')])
        return [b'Not Found']
