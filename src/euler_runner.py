import itertools
import os
import re
import subprocess
import sys
from time import time

def run_all_euler():
  java_euler_regex = re.compile(r'^P[0-9]+\.java')
  java_euler_files = [file_name for file_name in os.listdir('.') if java_euler_regex.match(file_name)]
  java_euler_class_names = [file_name[:-5] for file_name in java_euler_files]

  python_euler_regex = re.compile(r'^P[0-9]+\.py')
  python_euler_scripts = [file_name for file_name in os.listdir('.') if python_euler_regex.match(file_name)]

  print 'Evaluating all Euler problems!'

  for java_euler_script, java_euler_class in itertools.izip(java_euler_files, java_euler_class_names):
    subprocess.call(['javac', java_euler_script])
    start = time()
    result = subprocess.check_output(['java', java_euler_class]).strip()
    end = time()
    os.remove('%s.class' % java_euler_class)
    print '%s: %s, solved in %0.3fms' % (java_euler_script, result, (end - start) * 1000)

  for python_euler_script in python_euler_scripts:
    start = time()
    result = subprocess.check_output(['python', python_euler_script]).strip()
    end = time()
    print '%s: %s, solved in %0.3fms' % (python_euler_script, result, (end - start) * 1000)

if __name__ == '__main__':
  run_all_euler()
