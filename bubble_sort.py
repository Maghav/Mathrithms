# I am using Python for bubble sort. Below is the working of the code

# In first iteration, Starting from the first index, compare the first and the second elements. If the first element is greater than the second element, they are swapped
# Now, compare the second and the third elements. Swap them if they are not in order
# The above process goes on until the last element and the same process goes on for the remaining iterations
# After each iteration, the largest element among the unsorted elements is placed at the end.
# Below is the code

def func(a):
    # loop to access each array element
    for i in range(len(a)):

        # loop to compare array elements
        for j in range(0, len(a) - i - 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
            if a[j] > a[j + 1]:
                # swapping elements if elements
                # are not in the intended order
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp


b = [5,6,1,2,8,2,0,12,6,7]

func(b)

print(b)
