import typing
def main(numbers: typing.List[int], target_sum: int):
    # START WRITING CODE HERE
    lenoflist = len(numbers)
    # Sort the elements
    numbers.sort() 
    
    numbers.sort() 
  
    # Now fix the first element  
    # one by one and find the 
    # other two elements  
    for i in range(0, lenoflist-2): 
      
  
        # To find the other two elements, 
        # start two index variables from 
        # two corners of the list and 
        # move them toward each other 
          
        # index of the first element 
        # in the remaining elements 
        l = i + 1 
          
        # index of the last element 
        r = lenoflist-1 
        while (l < r): 
          
            if( numbers[i] + numbers[l] + numbers[r] == target_sum): 
                print("Triplet is", numbers[i],  
                     ', ', numbers[l], ', ', numbers[r]); 
                return True
              
            elif (numbers[i] + numbers[l] + numbers[r] < target_sum): 
                l += 1
            else: # numbers[i] + numbers[l] + numbers[r] > target_sum 
                r -= 1
  
    # If we reach here, then 
    # no triplet was found 
    print("not found")
    return False


if __name__ == "__main__":
    assert (main([5, 4, 10, 7, 1, 9], 13) is True), "Triplet exists"
    assert (main([4, 2, 5, 9, 11, 23], 9) is False), "Triple does not exist"
