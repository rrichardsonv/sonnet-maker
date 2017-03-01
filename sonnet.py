# abab cdcd efef gg
import sys
import re
import nltk
import string
import random
from nltk.corpus import cmudict

d = cmudict.dict()
def nsyl(word):
  return [len(list(y for y in x if y[-1].isdigit())) for x in d.get(word.lower(),'')]

_file_name = 'words.txt'

def get_txt(file_name):
  with open(file_name,'r') as f:
    s = ''.join(f.readlines())
    data = re.sub(r'[^\w\s\']','',s)
    return data

def word_soup(data):
  result = []
  raw_soup = nltk.word_tokenize(data)
  for noodle in raw_soup:
    syllables = nsyl(noodle)
    if len(syllables) == 0:
      syllables = 0
    else:
      syllables = syllables.pop()
    entry = [(noodle, syllables)]
    if result.count(entry) == 0:
      result = result + entry
  return result

def main():
  stuff = get_txt(_file_name)
  test_text_list = word_soup(stuff)
  max_range = len(test_text_list)
  word_index = random.randrange(0,max_range,1)
  lines_tupple = ()

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


# This is the standard boilerplate that calls the main() function.

if __name__ == '__main__':
  main()

