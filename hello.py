def app(environ, start_response):
  start_response('200 OK', [('Content-Type', 'text/plain')])
  qs = environ['QUERY_STRING'].split('&')
  response = ''
  for i in qs:
    response += i+'\n'
  return response
