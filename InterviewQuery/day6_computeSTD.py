import numpy as np

#Problem https://www.interviewquery.com/questions/compute-deviation

def compute_deviation(list_numbers):
    
    output_dict = {}
    for dict in list_numbers:
        output_dict[dict.get('key')] = np.std(dict.get('values'))
    return output_dict


if __name__== "__main__":
    
    list_numbers = [
    {
        'key': 'list1',
        'values': [4,5,2,3,4,5,2,3],
    },
    {
        'key': 'list2',
        'values': [1,1,34,12,40,3,9,7],
    }
    ]
    
    output = compute_deviation(list_numbers)
    print(output)

