def perimeter(length, breadth):
	p = 2 * (length + breadth)
	return p
    
def area(length, breadth):
    a = length * breadth
    return a
    
 l = input("Enter the Length: ")
 b = input("Enter the Breadth: ")
 
 print(perimeter(l,b))
 print(area(l,b))
 