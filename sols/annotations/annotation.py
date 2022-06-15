#!/usr/bin/env python3

def an_annotation(original_function):
  def new_function(*args, **kw):
    print('Showing original_function args: ',*args, **kw)
    original_function(*args, **kw)
  return new_function

@an_annotation
def hello(targetName=None):
    if targetName:
        print("Hello, " + targetName + "!")
    else:
        print("Hello, world!")


hello('Ric')