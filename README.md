### Sonnet Maker
*****

Builds sonnets from 2of12.txt ~~supplied text file~~ using nltk

### Goals
The main goal of this project is becoming more familiar with python and the functionality of nltk.

The secondary goal has been to frustrate myself with how bad computers are at poetry.


### Challenges
  1.  minor existential crises at my program being mean to me. It was an easy bugfix but an entire sonnet composed of 'you should die.' was very disconcerting

  2.  Grammar, wow, grammar is hard. Ended up using many MANY dicts as sets for the variety of ways that english verb conjugations behave illogically

  3.  Tuples vs Lists, hugely helpful when I finally read the description of Tuples ~= structs and Lists ~= arrays. Really needed that.


*****

### Setup:
  >python3 (I used [brew](https://brew.sh/) but you are welcome to use whatever you would like)

  >you'll need to install nltk and its dependency numPy
  (pip3)

  >accessing the books for nltk is a little bit of a mess due to some SSL problems so I would recommend downloading the individual books [here](http://www.nltk.org/nltk_data/) and following the instructions in [this](http://stackoverflow.com/questions/38916452/nltk-download-ssl-certificate-verify-failed) stackoverflow thread

  >you need to download

    1.  **The Carnegie Mellon Pronouncing Dictionary** _(for counting syllables)_

    2.  **Treebank Part of Speech Tagger Maximum entropy** _(for constructing syntactically sensible sentences)_

    3. **Punkt Tokenizer Models** _(for formating words so they can be Part of Speech Tagged)_

  >Place them unzipped in the appropriate folder _(as seen in the StackOverflow article [link](http://stackoverflow.com/questions/38916452/nltk-download-ssl-certificate-verify-failed) once again)_

  >And inside the appropriate subfolder both of which you will probably have to create

    1.  Punkt goes in:

      /usr/local/share/nltk_data/tokenizers/

    2.  Treebank goes in:

      /usr/local/share/nltk_data/taggers/

    3.  CMU_dict goes in:

      /usr/local/share/nltk_data/corpora/

  >Then you will need to modify nltk's default preferences to use the appropriate Part of Speech Tagger

    ###Pos_tagging (MAC)
****

    1. cd /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/nltk/tag

    2.  open __init__.py

    3. Comment out the RUS_PICKLE path variable

    4. Set a new variable

      > _TREEBANK_PICKLE = 'taggers/maxent_treebank_pos_tagger/english.pickle'

    5. Go inside the _get_tagger() function (**Not the get_tagger**)

    6. Comment out everything inside it

    7. Add these two lines

        >tagger = load(_TREEBANK_PICKLE)

        >return tagger

See that wasn't a nightmare right?

****

###Set up the application

  Run each of these with python3

  1.  > grammar_dictionary_builder.py

  *builds the file system in 'grammar_dict'*

  2.  > grammar_dictionary_sorter.py 

  *Takes all of the words in 2of12.txt and sorts them into the POS associated txt file(will take a little while)*

  3.  Add any of your favorite words into the associated files! 

  *In grammar_dictionary_sorter.py there are comments next to each of the Treebank codes explaining what they represent*

  
### To Run:
  >sonnet.py


### Coming soon:
  * ~~Subjects to go with those predicates haha~~
  * Actual Rhyming haha
  * Adjectives! Wow!
  * Adverbs! oOo!
  * Dependent clauses! Magestic!

### Never Coming:
  * Decent poetry
  

