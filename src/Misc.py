# Misc functions:
from .str_util import *
import math
import sys
import re


def settings(s):
  t = {}
  for k, v in re.findall('\n [\s]+[-][^\s]+[\s]+[-][-]([^\s]+)[^\n]+= ([^\s]+)', s):
    t[k] = coerce(v)
   
  return t

def cli(options):
    args = sys.argv
    for k, v in options.items():
        v = str(v)
        for i in range(1, len(args)):
            if args[i] == '-' + k[0:1] or args[i] == '--' + k:
              if v == "False":
                v = "true"
              elif v == "True":
                v = "false"
              else:
                v = args[i + 1]
        options[k] = coerce(v)
    return options

global Seed

def rand(lo, hi):
  Seed =  93716211
  lo = lo or 0
  hi = hi or 1
  Seed = (16807 * Seed) % 2147483647
  return lo + (hi - lo) * Seed / 2147483647

def rint(lo, hi):
  return math.floor(0.5 + rand(lo, hi))

def rnd(n, nPlaces):
  x = nPlaces or 3
  mult = 10**x
  return math.floor(n * mult + 0.5) / mult



