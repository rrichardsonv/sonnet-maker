import sys
import os

#builds the separate text files for the various gramatic word types

extension = '.txt'
path = './grammar_dict/'
treebank_classifications =[
  'CC',#Coordinating conjunction
  'CD',#Cardinal number
  'DT',#Determiner
  'EX',#Existential there
  'FW',#Foreign word
  'IN',#Preposition or subordinating conjunction
  'JJ',#Adjective
  'JJR',#Adjective, comparative
  'JJS',#Adjective, superlative
  'LS',#List item marker
  'MD',#Modal
  'NN',#Noun, singular or mass
  'NNS',#Noun, plural
  'NNP',#Proper noun, singular
  'NNPS',  #Proper noun, plural
  'PDT',#Predeterminer
  'POS',#Possessive ending
  'PRP',#Personal pronoun
  'PRP$',  #Possessive pronoun
  'RB',#Adverb
  'RBR',#Adverb, comparative
  'RBS',#Adverb, superlative
  'RP',#Particle
  'SYM',#Symbol
  'TO',#to
  'UH',#Interjection
  'VB',#Verb, base form
  'VBD',#Verb, past tense
  'VBG',#Verb, gerund or present participle
  'VBN',#Verb, past participle
  'VBP',#Verb, non-3rd person singular present
  'VBZ',#Verb, 3rd person singular present
  'WDT',#Wh-determiner
  'WP',#Wh-pronoun
  'WP$',#Possessive wh-pronoun
  'WRB']#Wh-adverb

# def make_the_dir():
#   os.makedirs('grammar_dict')

def make_all_the_files():
  for code in treebank_classifications:
    file = ''.join([path, code, extension])
    print(''.join(["Creating ",file]))
    new = open(file, 'w')
    new.close()

def main():
  make_all_the_files()


if __name__ == '__main__':
  main()
