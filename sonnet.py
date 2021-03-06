# abab cdcd efef gg
import sys
import re
import nltk
import string
import random
import my_grammar
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
  return count_syl(result)

def count_syl(words_with_syl):
  syl_sum = 0
  for word in words_with_syl:
    syl_sum += word[1]
  return syl_sum

def main():
  # stuff = get_txt(_file_name)
  # test_text_list = word_soup(stuff)
  # max_range = len(test_text_list)
  # word_index = random.randrange(0,max_range,1)
  sonnet_lines = []
  line_len = 0
  # i = 0
  while len(sonnet_lines) < 14:
    line_len = 0
    while line_len != 10:
      current_line = my_grammar.create_line()
      # print(''.join(['{}'.format(i),': ',current_line]))
      line_len = word_soup(current_line)
      # i += 1
    sonnet_lines.append(current_line)

  # print(sonnet_lines)
  # print(current_line)
  # print(line_length)

  sonnet = '''
          {}
          {}
          {}
          {}

          {}
          {}
          {}
          {}

          {}
          {}
          {}
          {}

          {}
          {}

        '''.format(*tuple(sonnet_lines))
  print(sonnet)

# This is the standard boilerplate that calls the main() function.

if __name__ == '__main__':
  main()

