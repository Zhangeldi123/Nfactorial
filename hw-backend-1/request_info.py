import json

def application(environ, start_response):
    path = environ.get('PATH_INFO', '/')
    method = environ.get('REQUEST_METHOD', '')
    protocol = environ.get('SERVER_PROTOCOL', '')

    if path == '/info' and method == 'GET':
        start_response('200 OK', [('Content-Type', 'application/json')])
        response = {
            "method": method,
            "url": path,
            "protocol": protocol
        }
        return [json.dumps(response).encode()]
    else:
        start_response('404 Not Found', [('Content-Type', 'text/plain')])
        return [b'Not Found']
