from bottle import route, run, template

def parse_file(input):
  f = open(input, "r")
  lines = []

  for line in f.readlines(100000):
    lines.append('<p>{}</p>'.format(line))

  f.close()
  return lines

@route('/')
def index():
  return parse_file("statusfile.txt")

run(host='localhost', port=8080, debug=True, reloader=True)