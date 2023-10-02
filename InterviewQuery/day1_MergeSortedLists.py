#Problem
https://www.interviewquery.com/questions/merge-sorted-lists

#Solution

def merge_list(test_input_list1, test_input_list2):
    
    merged_list = test_input_list1 + test_input_list2
    merged_list.sort()
    
    return merged_list

if __name__ == "__main__":
    a =[1,2,3]
    b=[2,3,4]
    c = merge_list(a,b)
    print(c)



