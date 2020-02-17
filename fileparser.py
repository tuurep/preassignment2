def add_reverse_dependencies(pkgs):
  for pkg in pkgs:
    for dep in pkgs[pkg]["dependencies"]:
      if dep in pkgs:
        pkgs[dep]["reverse_dependencies"].append(pkg)

def without_field_header(line):
  # Returns line without the first word
  # Remove trailing whitespace (package name always has it)
  return line.split(' ', 1)[1].strip()

def without_version_numbers(dep):
  return str.split(dep)[0]

def clean_dependencies(dep_list):
  cleaned = []

  for dep in dep_list:
    dep_alternatives = dep.split('|')
    for alt in dep_alternatives:
      alt = without_version_numbers(alt)
      if not alt in cleaned:
        cleaned.append(alt)

  return cleaned

def file_to_dict(input):
  pkgs = {}

  concat_multiliner = False
  d_paragraph = ''
  current_key = ''

  f = open(input, "r")
  
  for line in f.readlines():
    if concat_multiliner:
      if line.startswith(' .'):
        pkgs[current_key]["description"].append(d_paragraph)
        d_paragraph = ''
      
      elif line.startswith(('Original-Maintainer', 'Homepage:', 'Package:')):
        pkgs[current_key]["description"].append(d_paragraph)
        d_paragraph = ''
        concat_multiliner = False
      
      else:
        d_paragraph += line

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
      dep_list = clean_dependencies(dep_list)
      pkgs[current_key]["dependencies"] = dep_list
        
    if line.startswith('Description:'):
      description_firstline = without_field_header(line)
      pkgs[current_key]["description"].append(description_firstline)
      concat_multiliner = True
  
  f.close()

  add_reverse_dependencies(pkgs)

  return pkgs

