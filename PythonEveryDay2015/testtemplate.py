#!/usr/bin/python -tt
# Copyright 2010 Google Inc.http://www.apache.org/licenses/LICENSE-2.0
# http://code.google.com/edu/languages/google-python-class/

# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
# This is useful for future work and should be reused often 
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print( '%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
  print( 'donuts')
  # Each line calls donuts, compares its result to the expected for that call.
  # test(functionName(values, expectedValue ))
  # test(donuts(4), 'Number of donuts: 4')

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
