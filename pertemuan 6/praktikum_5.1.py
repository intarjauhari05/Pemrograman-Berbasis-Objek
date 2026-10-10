class Hewan:
    pass

class Invertebrata(Hewan):
    pass

class Molusca(Invertebrata):
    pass

class Vertebrata(Hewan):
    pass

class Mamalia(Vertebrata):
    pass

class Kucing(Mamalia):
    pass

print('Apakah','Kucing','Subclass dari',
'Mamalia','?', isubclass(Kucing, Mamalia))
print('Apakah','Kucing','Subclass dari',
'Vertebrata','?', isubclass(Kucing, Vertebrata))
print('Apakah','Kucing','Subclass dari',
'Invertebrata','?', isubclass(Kucing, Invertebrata))

kucing = Kucing()
mamalia = Mamalia()
vertebrata = Vertebrata()
invertebrata = Invertebrata()

print('Apakah', 'kucing', 'instance dari ', 'Kucing',
'?', isinstance(kucing, Kucing))
print('Apakah', 'kucing', 'instance dari ', 'Mamalia',
'?', isinstance(kucing, Mamalia))
print('Apakah', 'kucing', 'instance dari ',
'Vertebrata', '?', isinstance(kucing, Vertebrata))
print('Apakah','kucing', 'instance dari ',
'Invertebrata', '?', isinstance(kucing, Invertebrata))
