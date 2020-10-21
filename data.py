# unicode strings

mystery = '\U0001f4a9'
def mystery_name():
    import unicodedata
    name = unicodedata.name(mystery)
    print("{}'s Unicode name is {}".format(mystery, name))
    encoded = mystery.encode('utf-8')
    decoded = encoded.decode('utf-8')
    print("{} encoded to bytes via utf-8: {}; and decoded back: {}".format(mystery, encoded, decoded))

# old style formatting
def print_old():
    print("My kitty cat like %s, \nMy kitty cat likes %s, \nMy kitty cat fell on his %s, \nAnd now thinks he's a %s."
        % ('roast beef', 'ham', 'head', 'clam'))

# new style formatting
def print_new():
    letter = """Dear {0[salutation]} {0[name]},
    Thank you for your letter. We are sorry that our {0[product]} {0[verbed]} in your {0[room]}. Please note that
    it should never be used in a {0[room]}, especially near any {0[animals]}.
    Send us your receipt and {0[amount]}$ for shipping and handling. We will send you another {0[product]} that,
    in our tests, is {0[percent]}%% less likely to have {0[verbed]}.
    Thank you for your support.
    Sincerely,
    {0[spokesman]}
    {0[job_title]}"""
    response = {'salutation': 'Henry', 'name': 'Finn', 'product': 'vacuum', 'verbed': 'beeped', 'room': 'bedroom', \
        'animals': 'flies', 'amount': 19, 'percent': 23, 'spokesman': 'Alona', 'job_title': 'unemployed'}
    print(letter.format(response))

# regular expressions
def reg_exp():
    import re
    mammoth = """We have seen thee, queen of cheese,
    Lying quietly at your ease,
    Gently fanned by evening breeze,
    Thy fair form no flies dare seize.
    All gaily dressed soon you'll go
    To the great Provincial show,
    To be admired by many a beau
    In the city of Toronto.
    Cows numerous as a swarm of bees,
    Or as the leaves upon the trees,
    It did require to make thee please,
    And stand unrivalled, queen of cheese.
    May you not receive a scar as
    We have heard that Mr. Harris
    Intends to send you off as far as
    The great world's show at Paris.
    Of the youth beware of these,
    For some of them might rudely squeeze
    And bite your cheek, then songs or glees
    We could not sing, oh! queen of cheese.
    We'rt thou suspended from balloon,
    You'd cast a shade even at noon,
    Folks would think it was the moon
    About to fall and crush them soon."""
    print("All the words that start with 'c': {}".format(re.findall(r'\bc\w*', mammoth)))
    print("All the 4-letter words that start with 'c': {}".format(re.findall(r'\bc\w{3}\b', mammoth)))
    print("All the words that end with 'r': {}".format(re.findall(r'\b\w{3}r\b', mammoth)))
    print("All the words that have 3 vowels in a row: {}".format(re.findall(r'\b\w*[aeoui]{3}[^aeoui\s]*\w*\b', mammoth)))