def app(environ, start_response):
  start_response('200 OK', [('Content-Type', 'text/plain')]
  qs = parse_qs(eviron['QUERY_STRING'])
  return ["%s=%s<br>' % (k, qs[k][0]) for k in qs]
