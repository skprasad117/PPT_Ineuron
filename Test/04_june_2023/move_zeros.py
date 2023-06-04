class MoveZeros:
    def find(self,array):
        count_zeros = len([zero for zero in array if zero==0])
        while(count_zeros>0):
            zero = array.pop(array.index(0))
            array.append(zero)
            count_zeros -=1
        return array
    
obj = MoveZeros()
array = [int(num )for num in list(input("enter numbers seprated by comma : ").split(","))]
print(f"Input array is : {array}")
print(f"Output : {obj.find(array)}")