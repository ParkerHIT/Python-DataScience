#https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    
    dict = {}
    for i in range(int(input())):
        name = input()
        score = float(input())
        dict[name]=score
    sortedDict =  sorted(set(dict.values()))
    #print(sortedDict)
    toPrint = sorted([k for k,v in dict.items() if v == sortedDict[1]])
    print(*toPrint,sep='\n')