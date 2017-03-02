import random

extension = '.txt'
path = './grammar_dict/'

verb_bases = (['VBG'], ['VBN'], ['VB'], ['VBD'], ['VBZ'])
def sample_list(list_of_something):
    return list_of_something[random.randrange(0,len(list_of_something),1)]

coin = (False,True)

# subject_type_dep = {
#   'i':{
#     'PC': 'am',
#     'DC': 'was'
#   },
#   'we':{
#     'PC': 'are',
#     'DC': 'were'
#   },
#   'you':{
#     'PC': 'are',
#     'DC': 'were'
#   }
# }

first_second_pronouns = (['i','am'],['i','was'],['you', 'are'],['you','were'],['we','are'],['we','were'])

pos_categories = (['NN'],['NNS'],['NNP'],['NNPS'],['PRP'],['VBG'])

conj_helpers = {
  'VBG':(
    ['VBP'],
    ['VBP', 'VBN'],
    ['MD','VB'],
    ['VBD'],
    ['MD'],
    ['VBD', 'VBN']
  ),
  'VBN':(
    ['VBP'],
    ['MD', 'VB'],
    ['VBD']
  ),
  'VB':(
    ['MD']
  )
}

case_jank = {
  'VBN':True,
  'VB':True,
  'VBG':True
}

case_jank_mk_two = {
  'VBZ':True,
  'VBD':True,
  'MD':True
}

ok_verbs = {
  'have':True,
  'be':True
}

def determine_subj(first_verb_code,first_verb):
  if case_jank_mk_two.get(first_verb_code,False):
    subj = get_words(sample_list(pos_categories))
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
    with open(''.join([path,word,extension]),'r') as f:
      #note: bug which returns empty string for subj ~1 in 30
      d = f.readlines()
      result.append(''.join(sample_list(d)).strip())
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
      #check for edge case -_-
      if len(conj_tupple) > 1:
      #sample options
        helper_list = sample_list(conj_tupple)
      else:
        helper_list = conj_tupple
      # combine helpers and base verb
      helper_list += verb
      return helper_list
    else:
      return verb
  else:
    return verb


def main():
  random_verbage = v_is_for_verb() 
  all_verbs = get_words(random_verbage)
  subj = determine_subj(random_verbage[0], all_verbs[0])
  print(subj + all_verbs)





if __name__ == '__main__':
  print(main())


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