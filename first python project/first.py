def perimeter_rectangle(length, breadth):
	p = 2 * (length + breadth)
	return p
    
def area_rectangle(length, breadth):
    a = length * breadth
    return a
    
 l = input("Enter the Length: ")
 b = input("Enter the Breadth: ")
 
 print(perimeter_rectangle(l,b))
 print(area_rectangle(l,b))
 