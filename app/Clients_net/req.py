from proxy_requests import ProxyRequests

h = {'User-Agent': 'NCSA Mosaic/3.0'}
r = ProxyRequests('http://127.0.0.1:8000/')
r.set_headers(h)
r.get_with_headers()

