from bottle import route, run, template

def add_reverse_dependencies(pkgs):
  for pkg in pkgs:
    for dep in pkgs[pkg]["dependencies"]:
      if dep in pkgs:
        pkgs[dep]["reverse_dependencies"].append(pkg)

def without_field_header(line):
  # Returns line without the first word
  return line.split(' ', 1)[1].strip()

def cut_version_numbers(dep_list):
  without_ver = []

  for dep in dep_list:
    without_ver.append(str.split(dep)[0])

  return without_ver

def file_to_dict(input):
  pkgs = {}

  # Loop variables
  concat_multiliner = False
  d_paragraph = ''
  current_key = ''

  f = open(input, "r")
  
  for line in f.readlines():
    if line.startswith('Package:'):
      current_key = without_field_header(line)
      pkgs[current_key] = {
                            "description": [],
                            "dependencies": [],
                            "reverse_dependencies": []
                          }

    if line.startswith('Depends:'):
      list_as_str = without_field_header(line)
      dep_list = list_as_str.split(', ')
      dep_list = cut_version_numbers(dep_list)
      pkgs[current_key]["dependencies"] = dep_list

    if concat_multiliner:
      if line.startswith(' .'):
        pkgs[current_key]["description"].append(d_paragraph)
        d_paragraph = ''
      
      elif line.startswith(('Original-Maintainer', 'Homepage:')):
        pkgs[current_key]["description"].append(d_paragraph)
        d_paragraph = ''
        concat_multiliner = False
      
      else:
        d_paragraph += line
        
    if line.startswith('Description:'):
      d_paragraph = without_field_header(line)
      concat_multiliner = True
  
  f.close()

  add_reverse_dependencies(pkgs)

  return pkgs

@route('/')
def index():
  return file_to_dict('statusfile.txt')
  # return template('index', packages=file_to_dict('statusfile.txt'))

@route('/<pkg_name>')
def info(pkg_name):
  return template('pkg_info', pkg_name=pkg_name)

run(host='localhost', port=8080, debug=True, reloader=True)
