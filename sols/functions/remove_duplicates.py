#!/usr/bin/env python3

list=['hello','world','how','are','you','world','people','how']


def remove_duplicates(a_list):
    print('Cleaning: ',list)
    clean_list=[]
    for word in a_list:
        if word not in clean_list:
            clean_list.append(word)
    return clean_list


ans=remove_duplicates(list)
print('Result: ',ans)