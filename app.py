from bottle import route, run, template

def filter_fields(input):
  fields_as_str = []

  oneliner = ('Package:', 'Depends:')
  multiliner = ('Description:')
  description_end = ('Original-Maintainer', 'Homepage:')
  concat_multiliner = False
  multiline_str = ''

  f = open(input, "r")
  
  for line in f.readlines():
    if line.startswith(oneliner):
      fields_as_str.append('<p>{}</p>'.format(line))

    if line.startswith(multiliner):
      multiline_str = '<p>'
      concat_multiliner = True

    if concat_multiliner:
      if line.startswith(' .'):
        multiline_str += '</p><p>'
      
      elif not line.startswith(description_end):
        multiline_str += line
        
      else:
        fields_as_str.append(multiline_str + '</p>')
        multiline_str = ''
        concat_multiliner = False

  f.close()

  return fields_as_str

def file_to_dict(input):
  packages = {}

  for field in filter_fields(input):
    pass

  return packages

@route('/')
def index():
  return filter_fields('statusfile.txt')
  # return template('index', packages=file_to_dict('statusfile.txt'))

@route('/<pkg_name>')
def info(pkg_name):
  return template('pkg_info', pkg_name=pkg_name)

run(host='localhost', port=8080, debug=True, reloader=True)
