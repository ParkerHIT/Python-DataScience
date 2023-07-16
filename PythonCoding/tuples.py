#https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    
    my_list = list()
    for _ in integer_list:
        my_list.append(_)
    
    print(hash(tuple(my_list)))