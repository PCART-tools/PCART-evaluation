import tornado.httpclient
request = tornado.httpclient.HTTPRequest('http://httpbin.org/get', 'GET', {'Content-Type': 'application/json'}, None, None, None, 20, 20, None, True, 5, 'MyUserAgent', True, None, None, None, None, None, proxy_port=None, proxy_username=None, auth_mode=None)
