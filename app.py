from bottle import route, run, template

def parse_file(input):
  f = open(input, "r")
  lines = []

  for line in f.readlines():
    if line.startswith('Package:'):
      lines.append(str.split(line)[1])

  f.close()

  return sorted(lines)

@route('/')
def index():
  return template('index', pkg_names=parse_file('statusfile.txt'))

@route('/<pkg_name>')
def info(pkg_name):
  return template('pkg_info', pkg_name=pkg_name)

run(host='localhost', port=8080, debug=True, reloader=True)
