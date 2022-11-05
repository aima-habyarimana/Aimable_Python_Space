'''
Dictionaries allow you to connect pieces of information, but they don’t
keep track of the order in which you add key-value pairs. If you’re creating
a dictionary and want to keep track of the order in which key-value pairs
are added, you can use the OrderedDict class from the collections module.
'''

from collections import OrderedDict
favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
 print(name.title() + "'s favorite language is " +
 language.title() + ".")

 '''
Notice there are no curly brackets; the call to OrderedDict() creates an empty ordered dictionary
for us and stores it in favorite_languages.
 '''

 