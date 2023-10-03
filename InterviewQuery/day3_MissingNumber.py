
#Problem : https://www.interviewquery.com/questions/find-the-missing-number

#Solution
def missing_number(nums):
  nums.sort()
  print(nums)

  count = 0
  for i in nums:
    #print(count)
    #print(nums[i])
    if count ==i:
       count = count+1
    else:
        return count
      

if __name__ == "__main__":
    nums = [0,1,2,3,5]
    value = missing_number(nums)
    print("Missing number is", value)
    