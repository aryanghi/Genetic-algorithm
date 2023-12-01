import random
num_crossover=random.randint(1,7)


#fitness function

def fitness(A):
    x=0
    for i in range(len(A)):
        for j in range(i):
            if (abs(A[j]-A[i])==i-j):
                x=x+1
            if(A[j]==A[i]):
                x=x+1
    return(x)


#this function select 5 random candidate for parent

def parent_selection(A):
    random_from_random=[]
    for i in range(5):
        parent=random.choice(A)
        random_from_random.append(parent)
    return(random_from_random)


#this function select 2 best parent

def fitest_parent(A):
    fit=[]
    for i in range(len(A)):
        x=fitness(A[i])
        fit.append((x,A[i]))
    fit=sorted(fit)
    return(fit[0][1],fit[1][1])


#this function skips similar genes in offspring

def skipping(A):
    for i in range(num_crossover):
        for j in range(num_crossover,len(A)):
            if A[i]==A[j]:
                tmp=A[j+1:]
                A=A[:j]
                A[j:]=tmp
                break
    for i in range(8):
        x=0
        for j in range(len(A)):
            if i==A[j]:
                x=1
        if x==0:
            A.append(i)
    return(A)


#mutation function

def mutation(A):
    x1=random.randint(0,7)
    x2=random.randint(0,7)
    tmp=A[x1]
    A[x1]=A[x2]
    A[x2]=tmp
    return(A)


#survival selection function

def survival_selection(A):
    fit=[]
    for i in range(len(A)):
        x=fitness(A[i])
        fit.append((x,A[i]))
    fit=sorted(fit)
    A=fit[:-2]

    tmp=A
    A=[]
    for i in range(len(tmp)):
        A.append(tmp[i][1])
    return(A)


#this function sorted population

def fitness_ga(A):
    fit=[]
    for i in range(len(A)):
        x=fitness(A[i])
        fit.append((x,A[i]))
    fit=sorted(fit)
    return(fit)


#initialization

ga_list=[]
for i in range(100):
    random_list=random.sample(range(0,8),8)
    ga_list.append(random_list)

end=0
round=0
while(end==0):
    parents=parent_selection(ga_list)
    parent=fitest_parent(parents)

    parent_1=parent[0]
    parent_2=parent[1]
    
    
    #cross over
    
    tmp=parent_1[num_crossover:]
    parent_1[num_crossover:]=parent_2[num_crossover:]
    parent_2[num_crossover:]=tmp

    off_spring_1=skipping(parent_1)
    off_spring_2=skipping(parent_2)

    off_spring_1=mutation(off_spring_1)
    off_spring_2=mutation(off_spring_2)

    ga_list.append(off_spring_1)
    ga_list.append(off_spring_2)

    ga_list=survival_selection(ga_list)
    
    x=fitness_ga(ga_list)
    if(x[0][0]==0):
        end=1
        print(x[0][1],round)
    else:
        end=0
    
    round=round+1






