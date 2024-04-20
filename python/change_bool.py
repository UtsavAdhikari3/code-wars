# Task

# Create a function that always returns True/true for every item in a given list.
# However, if an element is the word 'flick', switch to always returning the opposite boolean value.
# Examples

# ['codewars', 'flick', 'code', 'wars'] ➞ [True, False, False, False]

# ['flick', 'chocolate', 'adventure', 'sunshine'] ➞ [False, False, False, False]

# ['bicycle', 'jarmony', 'flick', 'sheep', 'flick'] ➞ [True, True, False, False, True]


def flick_switch(lst):
	res, state = [], True
	for i in lst:
		if i == 'flick':
			state = not state
		res.append(state)
	return res




#     print(f_half)

#     f_half = [True for s in f_half]

#     print(f_half)

#     s_half = [False for j in s_half]

#     print(s_half)

#     final_list = f_half + s_half

#     return final_list

    

a = ['bicycle', 'jarmony', 'flick', 'sheep', 'flick']

print(flick_switch(a))
        

   

