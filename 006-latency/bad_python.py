from sys import *
from numpy import *
from sympy import *
from numpy import array

newversion = False

n = 0
# STDOUT = open('test.txt', 'w')
STDOUT = None # so i switch to file
def a(t, b):
 global n
 n += 1
 print(str(n).strip()+": ",t(b))
def print(a,something, close=0):
  global STDOUT
  if STDOUT is None:
      # STDOUT = open(stdout, 'w')
          STDOUT = stdout
  STDOUT.write(str(a).strip()+str(something))
  if close:
   if STDOUT != stdout: STDOUT.close()
def str(s):
    return s.__str__() + '\n'
xa = array([1])
a(str,"PRINTING VALUES")
for x in range(2, 10):
 xa = list(xa)
 xa.append(x)
 xarray = array(xa)
x = Symbol("x") # sympy.Symbol I hope
os = ""
function = sin(x)
for y in xa:
    a(float,(function.subs({'x': y})))
print("", "", 1)
