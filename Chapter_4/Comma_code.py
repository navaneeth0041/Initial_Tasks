def cc(list):
    len_list=len(list)
    ending=list[-1]
    words=''
    l_new=list[0:len_list-1]
    for i in l_new :
        words+=i+','
    print(words+' and '+ending)

spam=['apples','bananas','tofu','cats']
cc(spam)