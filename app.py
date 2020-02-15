from bottle import route, run, template

def parse_file(input):
  f = open(input, "r")
  keywords = ('Package:', 'Description:', "Depends:")
  lines = []

  for line in f.readlines():
    if line.startswith(keywords):
      lines.append('<p>{}</p>'.format(line))

  f.close()
  return lines

@route('/')
def index():
  return parse_file("statusfile.txt")

run(host='localhost', port=8080, debug=True, reloader=True)
