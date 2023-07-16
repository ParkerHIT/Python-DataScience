
#https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    listArr = []
    for i in range(n):
        name , *line = input().split()
        index = list(map(int,line))
        #print (name,*index)
        if name == 'insert' :
            listArr.insert(int(index[0]),index[1])
        elif name == 'append':
            listArr.append(index[0])
        elif name == 'print':
            print(listArr)
        elif name == 'sort':
            listArr.sort()
        elif name == 'pop':
            listArr.pop()
        elif name == 'reverse':
            listArr.reverse()
        elif name == 'remove':
            listArr.remove(index[0])