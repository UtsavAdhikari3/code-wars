def reverse_words(text):
    split_list = text.split()
    list1 = []
    # if ' ' or '' in text:
    #     for i in split_list:
    #         rev_list = i[::-1]
    #         list1.append(rev_list)
        
    #     a = ' '.join(list1)
        
    # elif '  ' in text:
    #     for i in split_list:
    #         rev_list = i[::-1]
    #         list1.append(rev_list)
    #     a = '  '.join(list1)
    
    # return a
    
    a = text.count('  ')
    
    if a > 1 or a == 1:
        for i in split_list:
            rev_list = i[::-1]
            list1.append(rev_list)
        b = '  '.join(list1)
        # print('hello')
    else:
        for i in split_list:
            rev_list = i[::-1]
            list1.append(rev_list)
        
        b = ' '.join(list1)
        
    return b