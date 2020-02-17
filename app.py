from bottle import route, run, template
from fileparser import file_to_dict

input_file = 'statusfile.txt'
  # The file is a copy of /var/lib/dpkg/status
  # Copied 16.2.2020 on my Ubuntu

@route('/')
def index():
  pkgs = file_to_dict(input_file)

  pkgs_arr = []
  for pkg in pkgs:
    pkgs_arr.append(pkg)

  return template('index', pkgs_ordered=sorted(pkgs_arr))

@route('/<pkg_name>')
def info(pkg_name):
  pkgs = file_to_dict(input_file)

  if pkg_name not in pkgs:
    return '''<h3>Package {} was not found</h3>
              <a href="/">Back to index</a>'''.format(pkg_name)

  return template('pkg_info', pkg_name=pkg_name, pkg=pkgs[pkg_name])

run(host='localhost', port=8080, debug=True, reloader=True)
