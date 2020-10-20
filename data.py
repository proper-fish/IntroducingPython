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