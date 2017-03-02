import random

verb_bases = (['VBG'], ['VBN'], ['VB'], ['VBD'], ['VBZ'])
def sample_tupple(tupple):
    return tupple[random.randrange(0,len(tupple),1)]

coin = (False,True)

subject_type_dep = {
  'i':{
    'PC': 'am',
    'DC': 'was'
  },
  'we':{
    'PC': 'are',
    'DC': 'were'
  },
  'you':{
    'PC': 'are',
    'DC': 'were'
  }
}


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

def v_is_for_verb():
  #first pick a verb
  # verb = sample_tupple(verb_bases)
  verb = sample_tupple(verb_bases)
  #second determine if it can be conjugated
  if case_jank.get(verb[0], False):
    #third flip a coin
    if sample_tupple(coin):
      #fourth get conjugation options
      conj_tupple = conj_helpers[verb[0]]
      #check for edge case -_-
      if len(conj_tupple) > 1:
      #sample options
        helper_list = sample_tupple(conj_tupple)
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
  return v_is_for_verb()





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