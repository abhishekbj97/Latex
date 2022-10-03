# -*- coding: utf-8 -*-
"""latex.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NWvnoxcjOFpXGm0Ev3bEapFymNyUcvqG
"""

pip install latexify-py

import math
import latexify

@latexify.with_latex
def solve(a,b,c):
  return (-b + math.sqrt(b**2 -4*a*c)) / (2*a)

solve

