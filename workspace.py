def least_occuring_elements(arr):
    # Step 1: Count frequencies of each element using a dictionary
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    # Step 2: Find the minimum frequency among all elements
    min_freq = min(freq.values())
    
    # Step 3: Collect elements with the minimum frequency
    least_occuring = []
    for num, count in freq.items():
        if count == min_freq:
            least_occuring.append(num)
    
    # Step 4: Sort the least occurring elements in decreasing order of their values
    least_occuring.sort(reverse=True)
    
    # Step 5: Print the result
    print(" ".join(map(str, least_occuring)))

# Input reading and processing
n = int(input().strip())  # Read the size of the array
arr = list(map(int, input().strip().split()))  # Read the array elements
least_occuring_elements(arr)  # Call the function to find and print the least occurring elements
