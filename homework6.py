my_dict = {'Taerrean': 15, 'Niki': 18, 'TshB': 16, 'Yukine': 14} # Это ники моих друзей в дискорде, если вам интересно (и мой на первом месте)
print('Dict:', my_dict)
print('Existing value:', my_dict['Taerrean'])
print('Non-Existing value:', my_dict.get('helheim'))
my_dict.update({'helheim': 27,
                'hydrasung': 25})
print('Deleted value:', my_dict.pop('hydrasung'))
print('Modified dictionary:', my_dict)
my_set = {52, 52, '52', 1488, 'Terrarium', False, 'Terrarium'}
print('Set:', my_set)
my_set.add('St.Petersburg')
my_set.add('Moscow')
my_set.discard('52')
print('Modified set:', my_set)
