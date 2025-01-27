import sys
 
# function to read the file 
def readfile(filename):
    with open(filename, 'r') as file:
        numbers = [] #creates the variable to hold list of numbers from file
        for line in file.readlines():
            numbers.append(int(line.strip())) #removes the whitespaces
    return numbers
        
#function to sort the list of numbers
def numberSort205(p, r, A):
    if p < r:
        q = divide(p, r, A)
        numberSort205(p, q-1, A) #sorts the numbers from the left side of pivot
        numberSort205(q+1, r, A) #sorts the numbers on the right side of the pivot

#function that swaps numbers 
def divide(p, r, A):
    x = A[r] #this selects the pivot element
    i = p - 1 #variable  will track the last element where swap happens
    for j in range(p, r): #loop to compare element to pivot 
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]  # Swap elements
    A[i+1], A[r] = A[r], A[i+1]  # Swap with pivot
    return i + 1



def main():
    # Check if the file name is provided
    if len(sys.argv) < 2:
        print("Usage: python numberSort.py filename/path")
        sys.exit(1)

    filename = sys.argv[1]

    A = readfile(filename)
    numberSort205(0, len(A)-1 , A)
    for number in A:
        print(number)


main()