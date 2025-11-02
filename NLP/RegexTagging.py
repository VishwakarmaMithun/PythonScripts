patterns = [(r'.*ing$', 'VBG'), (r'.*ed$', 'VBD')] 
regex_tagger = RegexpTagger (patterns)
regex_tagger. tag (tokens) 