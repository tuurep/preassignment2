from bottle import route, run
import numpy as np

@route('/hello')
def hello():
  return "Hello World!"

@route('/file_dump')
def file_dump():
  f = open("statusfile.txt", "r")
  lines = f.readlines()
  return lines

run(host='localhost', port=8080, debug=True)