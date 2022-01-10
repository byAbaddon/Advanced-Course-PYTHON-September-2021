def age_assignment(*args, **kwargs):
    info_dict = {}
    for name in args:
        info_dict[name] = kwargs[name[0:1]]
    return info_dict    


'''
print(age_assignment("Peter", "George", G=26, P=19))
------------
{'Peter': 19, 'George': 26}
'''