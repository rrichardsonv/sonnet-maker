import sys
import nltk

extension = '.txt'
path = './grammar_dict/'
oe_dict = {
  'CC':[],#Coordinating conjunction
  'CD':[],#Cardinal number
  'DT':[],#Determiner
  'EX':[],#Existential there
  'FW':[],#Foreign word
  'IN':[],#Preposition or subordinating conjunction
  'JJ':[],#Adjective
  'JJR':[],#Adjective, comparative
  'JJS':[],#Adjective, superlative
  'LS':[],#List item marker
  'MD':[],#Modal
  'NN':[],#Noun, singular or mass
  'NNS':[],#Noun, plural
  'NNP':[],#Proper noun, singular
  'NNPS':[],  #Proper noun, plural
  'PDT':[],#Predeterminer
  'POS':[],#Possessive ending
  'PRP':[],#Personal pronoun
  'PRP$':[],  #Possessive pronoun
  'RB':[],#Adverb
  'RBR':[],#Adverb, comparative
  'RBS':[],#Adverb, superlative
  'RP':[],#Particle
  'SYM':[],#Symbol
  'TO':[],#to
  'UH':[],#Interjection
  'VB':[],#Verb, base form
  'VBD':[],#Verb, past tense
  'VBG':[],#Verb, gerund or present participle
  'VBN':[],#Verb, past participle
  'VBP':[],#Verb, non-3rd person singular present
  'VBZ':[],#Verb, 3rd person singular present
  'WDT':[],#Wh-determiner
  'WP':[],#Wh-pronoun
  'WP$':[],#Possessive wh-pronoun
  'WRB':[]#Wh-adverb
}


def get_pos(word):
  word_soup = nltk.word_tokenize(word)
  return nltk.pos_tag(word_soup)

def get_txt(file_name):
  with open(file_name,'r') as f:
    d = f.readlines()
    for word in d:
      coded_word = get_pos(word)
      oe_dict[coded_word[0][1]].append(coded_word[0][0])

def file_flight_control():
  for code in oe_dict:
    # print(''.join([path,code,extension]))
    with open(''.join([path,code,extension]),'w') as f:
      #write into the file do I need newlines?
      # '\n'.join(oe_dict[code])



def main():
  # get_txt('2of12.txt')
  file_flight_control()


if __name__ == '__main__':
  main()