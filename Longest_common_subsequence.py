# Importing the necessary libraries
import time
import math
from itertools import combinations

#Define function for dynamic programming
def lcs_dp(S_1, S_2):
    # To find the length of the strings
    m = len(S_1) #length of 1st string 
    n = len(S_2) #length of 2nd string

    # to store the dp values, we can declare an array 
    L = [[0 for i in range(n+1)] for j in range(m+1)]
    
    # L[m+1][n+1], a matrix is built in a bottom up approach
    # L[i][j] contains length of Longest Common Subsequence of S_1[0 to i-1] and S_2[0 to j-1]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0  
            #when current row and current row matches, add 1 to the diagonal element
            elif S_1[i-1] == S_2[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            #pick maximum value from the element in the previous column or element in the previous row  
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1]) #compares the 2 values and returns maximum length 
 


    # Create a string variable to store the lcs string
    lcs = ""
 
    # We are required to begin from the right-most-bottom-most corner and store characters consecutively in lcs[]
    i = m
    j = n
    count = 0
    while i > 0 and j > 0:
 
        # If current character present in S_1[] and S_2 are same, then character present currently is part of Longest Common Subsequence
        if S_1[i-1] == S_2[j-1]:
            lcs += S_1[i-1]
            i -= 1
            j -= 1
        # If it is not the same, we need to identify the larger of two and move in the direction of greater value
        elif L[i-1][j] > L[i][j-1]:
            i -= 1     
        else:
            j -= 1
        count += 1
 
    # traversing the table in reverse order, LCS is the reverse of what is obtained
    lcs = lcs[::-1]
    return lcs, count
     

# Driver code
if __name__ == "__main__": 
    # Opening the input file
    try:
        f = open('DynamicLab2Input.txt', 'r')
    except:
        print('Input file not found')#displayed if input file is not found
    
    # Read data from file
    data = f.readlines()

    # Intializing a new list called n_data 
    n_data = []


    # Program to accept only characters 'A','T','G' and 'C'
    acc_chars = ['A', 'T', 'G', 'C']
    for i in data:
        flag = 0
        i = i.split()[-1].strip()
        for j in i:
            if j not in acc_chars:
                flag = 1
                break
        if not flag:
            n_data.append(i.split()[-1].strip())
        else:
            print('Invalid Characters in input')
    

    # Create pairs of sequences for pairwise comparisons
    combs = list(combinations(list(range(len(n_data))), 2))
    

    try:
        with open('Output_Dynamic.txt', 'w') as f:
            #list out the number of sequences, sequences and length of the given sequences
            #display the number of sequences in the file
            cnt=0
            for num_lines in n_data:
                cnt +=1

            f.write(f'Number of valid sequences given: {cnt} \n')
            f.write(f'\n')
            #placing a counter for displaying sequence length and sequence number
            a = 0
            for lines in n_data:
                sequence_length = len(lines)
                a = a + 1

                
                #printing the sequence number and the length of the sequence
                f.write(f'Sequence #{a} | Length:{sequence_length} \n')
                #listing the nucleotides in the sequence
                f.write(f'{lines}\n')
                f.write(f'\n')
            f.write(f'*************************************************************************\n')
                #starting the timer for the total time taken for entire file execution
            start_1 = time.time()
            # Loop through each combination
            for i,comb in enumerate(combs):
        
                # Set timer to calculate time of execution
                start=time.time()

                # Get the first sequence
                s1 = n_data[comb[0]]
                
                # Get the second sequence
                s2 = n_data[comb[1]]
                
                # Call the LCS function to calculate the longest common subsequence
                lcs, count = lcs_dp(s1,s2)
            
                # Record end time to calculate time of execution
                end=time.time()

                
                #Display the comparison number and sequence number between which longest common subsequence is found
                f.write(f"Comparisons #{i+1}: sequences {comb[0]+1} and {comb[1]+1} \n" )
                #Print the sequence of the longest common Subsequence
                f.write(f"Longest Common Subsequence:\n")
                f.write(f"{lcs} \n")
                #Print the length of the longest common subsequence
                f.write(f"Length of the LCS: {len(lcs)} \n")
                #Printing the execution time for each of the 2 sequences
                f.write(f"Execution time: {(end-start)*10**9} ns \n")
                #print the number of comparisons while creating the table
                f.write(f"Comparisons done while creating the table:{((len(s1)+1) * (len(s2)+1))}\n")
                #print the comparisons while retrieving the LCS
                f.write(f"Comparisons done while retrieving the LCS: {count}\n")
                f.write("************************************************************************* \n")
            
            #Record the end time to calculate the total execution time of the entire file
            end_1 = time.time()
            #Displaying the number of successful pairwise comparisons
            f.write(f'There were {math.comb(len(n_data),2)} successful pairwise comparisons \n')
            #Displaying the total execution time for th entire file
            f.write(f'Total execution time: {(end_1-start_1)} s')
        f.close()
    except:
        print('Error in writing to output file.')#displayed if there is an error while writing to output
