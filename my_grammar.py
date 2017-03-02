import random
import string

extension = '.txt'
path = './grammar_dict/'
verb_bases = (['VBG'], ['VBN'], ['VB'], ['VBD'], ['VBZ'])
coin = (False,True)

first_second_pronouns = (['i'],['you'],['we'])

pos_categories = (['NN'],['NNS'],['NNP'],['NNPS'],['PRP'],['VBG'])

conj_helpers = {
  'VBG':(
    ['VBP'], ['has', 'been'], ['MD','be'], ['VBD'], ['had', 'been']
    ),
  'VBN':(
    ['has'], ['MD', 'have'], ['had'] ),
  'VB':(
    ['MD']
  )
}

helper_exceptions = {
'have':True, 'had':True, 'been':True, 'be':True, 'has':True 
}

case_jank = {
  'VBN':True, 'VB':True, 'VBG':True }

case_jank_mk_two = {
  'VBZ':True, 'VBD':True, 'MD':True }

ok_verbs = {
  'have':True, 'be':True, 'had':True }

not_ok_verbs = {
  'keep':True
}

not_actually_verbs = { #sigh
  'nosebleed': True, 'not a verb': True, 'timid': True, 'vivid': True }

en_pronoun_exceptions = {
  'we':True, 'you':True, 'they':True }

subject_tense = {
'plural':(
  ['are'],['were']
  ),
'first_person':(
  ['am'], ['was']
  ),
'third_person':(
  ['is'],['was']
  )
}

nom_pronoun = {
  'i': True, 'he': True, 'she': True, 'they': True, 'we': True }

acc_pronoun = {
  'i': ['me'], 'he': ['him'], 'she': ['her'], 'they': ['them'], 'we': ['us'] }

proper_noun_case = {
  'NNP': False, 'NNPS': False }

def sample_list(list_of_something):
    return list_of_something[random.randrange(0,len(list_of_something),1)]



def get_obj():
  obj_code = 'PRP'
  while obj_code == 'PRP':
    obj_code = sample_list(pos_categories)
  # print(obj_code)
  # print(proper_noun_case.get(obj_code[0],True))
  if proper_noun_case.get(obj_code[0],True):
    obj = [get_words(obj_code)[0].lower()]
    if nom_pronoun.get(obj[0], False):
      return acc_pronoun[obj[0]]
    else:
      return obj
  else:
    obj = get_words(obj_code)
    return obj


def only_cap_no_lower(sentence):
  sentence_list = sentence.split(' ')
  first_word = sentence_list[0].capitalize()
  sentence_list[0] = first_word
  return ' '.join(sentence_list)

def english_makes_no_sense(subject, verb, flag_for_check):
  if flag_for_check == -1:
    return verb
  else:
    verb_in_question = verb[flag_for_check]
    if (verb_in_question.find('en') != -1 and verb_in_question != 'been'):
      if en_pronoun_exceptions.get(subject[0],False):
        return sample_list(subject_tense['plural']) + verb
      else:
        if subject[0] == 'i':
          return sample_list(subject_tense['first_person']) + verb
        else:
          return sample_list(subject_tense['third_person']) + verb
    else:
      return verb


def determine_subj(first_verb_code,first_verb):
  subj = ['']
  while subj[0] == '':
    if case_jank_mk_two.get(first_verb_code,False):
      choice = [first_verb_code]
      # print(choice)
      while (choice[0] == first_verb_code or not_ok_verbs.get(choice[0],False)):
        choice = sample_list(pos_categories)
      subj = get_words(choice)
    else:
      # print('We need first or second person')
      if ok_verbs.get(first_verb,False):
        subj = sample_list(first_second_pronouns)
      else:
        subj = get_words(sample_list(pos_categories))
  return subj


def get_words(word_list):
  result = []
  for word in word_list:
    if helper_exceptions.get(word,False):
      result.append(word)
    else:
      with open(''.join([path,word,extension]),'r') as f:
        d = f.readlines()
        if word.find('V') == 0:
          word_choice = 'not a verb'
          while not_actually_verbs.get(word_choice, False):
            word_choice = sample_list(d)
        else:
          word_choice = ['']
          while word_choice[0].strip() == '':
            word_choice = sample_list(d)
        result.append(''.join(word_choice).strip())
  return result

def v_is_for_verb():
  #first pick a verb
  # verb = sample_list(verb_bases)
  verb = sample_list(verb_bases)
  #second determine if it can be conjugated
  if case_jank.get(verb[0], False):
    #third flip a coin
    if sample_list(coin):
      #fourth get conjugation options
      conj_tupple = conj_helpers[verb[0]]
      # print(conj_tupple)
      #check for edge case -_-
      if len(conj_tupple) > 1:
      #sample options
        helper_list = sample_list(conj_tupple)
      else:
        helper_list = conj_tupple
      # combine helpers and base verb
      # if verb[0] == 'VB':
        # print(helper_list)
      # += is DANGEROUS wow haha
      return helper_list + verb
    else:
      return verb
  else:
    return verb

def check_for_obj(verb):
  # print(verb)
  obj_bool = (len(verb) > 1 and (verb[-1].find('ing') != -1 and verb[-2].find('ed') != -1))
  # print(obj_bool)
  return obj_bool

def build_indepedent_clause(svo_list):
  clause = ' '.join(svo_list) + sample_list(['.','?','!','...','.'])
  return only_cap_no_lower(clause)

def create_line():
  # test_for_check_for_obj()
  random_verbage = v_is_for_verb()
  flag_for_check = -1

  if random_verbage[0].count('VBG') == 1:
    flag_for_check = random_verbage.index('VBG')
  if random_verbage[0].count('VBN') == 1:
    flag_for_check = random_verbage.index('VBN')

  all_verbs = get_words(random_verbage)
  subj = determine_subj(random_verbage[0], all_verbs[0])

  all_verbs = english_makes_no_sense(subj,all_verbs, flag_for_check)

  if check_for_obj(all_verbs):
    return build_indepedent_clause(subj + all_verbs)
  else:
    return build_indepedent_clause(subj + all_verbs + get_obj())





if __name__ == '__main__':
  print(create_line())


# conj_helper_dependencies = {
# 'PC': ('VBP', 'VBG'),
# 'PPC': ('VBP','VBN', 'VBG'),
# 'FC': ('MD', 'VB', 'VBG'),
# 'DC': ('VBD', 'VBG'),
# 'FPC': ('MD', 'VBG')
# 'DPC': ('VBD','VBN','VBG')
# 'PP': ('VBP', 'VBN'),
# 'FP': ('MD', 'VB','VBN'),
# 'DP': ('VBD','VBN'),
# 'F': ('MD', 'VB'),
# }


# clause_type = {
#   #independent
#   'I': {
#     'add': 
#     'seq':
#     'cont':
#     'res':
#     'alt':
#     'emp':
#     'ex':
#     'sum':
#   }
#   #dependent
#   'D': {
#     'noun':
#     'adj':
#     'adv':
#   }
# }
# def test_for_check_for_obj():
  # test_one = ['is', 'uncorroborated', 'screenwriting']
  # test_two = ['has', 'screenwriting']

  # if check_for_obj(test_one):
  #   print('positive case works')

  # if check_for_obj(test_two):
  #   print('negative case does not work')
  # else:
  #   print('negative case works')