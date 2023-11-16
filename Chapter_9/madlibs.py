import re

file=open('madlibs.txt','r')
file_rd=file.read()
adjective=re.compile(r'ADJECTIVE')
noun=re.compile(r'NOUN')
verb=re.compile(r'VERB')
adj=input("Enter an adjective: ")
a=adjective.sub(adj,file_rd)
nun=input("Enter a noun: ")
b=noun.sub(nun,a)
vrb=input("Enter a verb: ")
c=verb.sub(vrb,b)
print(c)