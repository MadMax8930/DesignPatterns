#Structural Pattern

class Array:
   def __init__(self):
      self.capacity = 2
      self.length = 0
      self.arr = [0] * 2  #Array of capacity = 2
      
   # Insert n in the last position of the array
   def pushBack(self, n):
      if self.length == self.capacity:
         self.resize()
         
      # Insert at next empty position
      self.arr[self.length] = n
      self.length += 1
         
   def resize(self):
      # Create new array of double capacity
      self.capacity = 2 * self.capacity
      newArr = [0] * self.capacity
      
      # Copy elements to newArr
      for i in range(self.length):
         newArr[i] = self.arr[i]
      
      # Update reference to the new array
      self.arr = newArr
      
      # Print the new array
      print("New array after resizing:", self.arr)  #[1, 2, 0, 0]
      
# Testing the code
array = Array()
array.pushBack(1)
array.pushBack(2)
array.pushBack(3) 
      
         
