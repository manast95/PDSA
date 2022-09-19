#python
def findLargest(L):
  left = 0
  s = len(L)
  right = s-1
  
  # If list has only one element, that is the max.
  if (s==1):
    return L[0]
    
  while (left<=right):
    mid=(left+right)//2
    
    # if mid is at last index, next element to compare will be at index 0
    if (mid == s-1):
      nextToMid = 0
    else:
      nextToMid = mid+1

    if (L[mid] > L[nextToMid]):
      return L[mid]
    elif (L[mid] < L[0]):
      # our element is in left of mid
      right = mid-1
    else:
      # our element is in right of mid
      left = mid+1