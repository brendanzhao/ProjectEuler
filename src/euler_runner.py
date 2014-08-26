import itertools
import os
import re
import subprocess
import sys
from time import time

def timer(f):
  def wrap(*args):
    start = time()
    result = f(*args)
    end = time()
    print '%s: %s, solved in %0.3fms' % (args[1], result, (end - start) * 1000)
  return wrap

def get_python_files():
  euler_regex = re.compile(r'^P[0-9]+\.py')
  euler_files = [file_name for file_name in os.listdir('.') if euler_regex.match(file_name)]
  return euler_files

def get_java_files():
  euler_regex = re.compile(r'^P[0-9]+\.java')
  euler_files = [file_name for file_name in os.listdir('.') if euler_regex.match(file_name)]
  return euler_files

def compile_java_files(java_files):
  for java_file in java_files:
    subprocess.call(['javac', java_file])

def run_all_euler(java_files, python_files):
  print 'Evaluating all Euler problems!'

  for java_file in java_files:
    run_script('java', java_file[:-5], java_file)

  for python_file in python_files:
    run_script('python', python_file, python_file)

def remove_java_classes(java_files):
  for java_file in java_files:
    os.remove('%s.class' % java_file[:-5])

@timer
def run_script(command, *args):
  return subprocess.check_output([command, args[0]]).strip()

if __name__ == '__main__':
  java_files = get_java_files()
  python_files = get_python_files()
  compile_java_files(java_files)
  run_all_euler(java_files, python_files)
  remove_java_classes(java_files)
