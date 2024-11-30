#------------------ debugging file calendar1.py

1) from typing import Optional  
   we have to import this above package 
2) check for overlap: The original code did not properly check for event overlap.

3) Error Handling in book(): When a new event was passed to insert, the parameter was incorrectly named node=Node(start, end). This is inconsistent with the method signature in Node.insert().

4) logical error in class node in insert function:
   
   #-------before debugging  
   if node.start <= self.end:  
   #-------after debugging  
   if node.start >= self.end:
   
   #------before debugging  
   elif node.end >= self.start:  
   #------after debugging  
   if node.end <= self.start:
   
   #----------error in return statement of right node-----  
   
   #------before debugging---------------  
   return self.left_child.insert(node)  
   #------after debugging---------------  
   return self.right_child.insert(node)  

#------run python files-------  
python time1.py

python calendar1.py

python fuel.py



