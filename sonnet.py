# abab cdcd efef gg
import sys
import re
import nltk

_file_name = 'words.txt'

def get_txt(file_name):
  with open(file_name,'r') as f:
    data = ''.join(f.readlines())
    return data

def word_soup(data):
  raw_soup = nltk.word_tokenize(data)
  for drop in raw_soup:
    print(drop)


def main():
  # Get the name from the command line, using 'World' as a fallback.
  # lines_tupple = ()
  # sonnet = '''
  #         {}
  #         {}
  #         {}
  #         {}

  #         {}
  #         {}
  #         {}
  #         {}

  #         {}
  #         {}
  #         {}
  #         {}

  #         {}
  #         {}

  #       '''.format(*lines_tupple)
  stuff = get_txt(_file_name)
  word_soup(stuff)

# This is the standard boilerplate that calls the main() function.


if __name__ == '__main__':
  main()

