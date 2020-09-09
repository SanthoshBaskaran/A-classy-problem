test_cases=int(input())
main_result=[]
for i in range(test_cases):
  before_sort=[]
  answer=[]
  name=[]
  classes=int(input())
  for j in range(classes):
    a=input()
    before_sort.append(a)
  before_sort=sorted(before_sort)
  for k in before_sort:
    number=''
    after_sort1=k.split()
    withcolon=after_sort1[0]
    withcolon=withcolon[0:-1]
    name.append(withcolon)
    x=(after_sort1[1].split('-'))
    x=x[::-1]
    for l in x:
      if(l=='upper'):
        number=number+'0'
      elif(l=='middle'):
        number=number+'1'
      elif(l=='lower'):
        number=number+'2'
    length=len(number)
    diff=10-length
    if(diff>0):
        r=diff*'1'
        number=number+r
    answer.append(number)
  sorting1=[]
  for m in answer:
    index1=answer.index(min(answer))
    sorting1.append(name[index1])
    answer[index1]='x'
  for n in sorting1:
    main_result.append(n)
  equal='='*30
  main_result.append(equal)
for o in main_result:
  print(o)
