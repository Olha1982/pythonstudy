data=[]
with open ("data.txt") as f:
    for line in f:
        data.append ([int(x) for x in line.split()])
        for nums in data:
            for num in range(1, nums[2]+1):
                if num % nums[0]==0 and num % nums[1]==0:
                    print ('FB')
                elif num % nums[0]==0:
                    print ('F')
                elif num % nums[1]==0:
                    print ('B')
                else:
                    print (num)