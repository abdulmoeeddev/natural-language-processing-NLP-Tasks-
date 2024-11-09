def edit_operations_traceback(str1, str2, dp):
    i, j = len(str1), len(str2)
    operations = []
    
    while i > 0 or j > 0:
        if i > 0 and j > 0 and str1[i - 1] == str2[j - 1]:
            operations.append(f"No operation: {str1[i - 1]}")
            i -= 1
            j -= 1
        elif i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + 1:
            operations.append(f"Substitution: {str1[i - 1]} -> {str2[j - 1]}")
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i - 1][j] + 1:
            operations.append(f"Deletion: {str1[i - 1]}")
            i -= 1
        else:
            operations.append(f"Insertion: {str2[j - 1]}")
            j -= 1
    
    return operations[::-1]

# Test the function
str1 = "kitten"
str2 = "sitting"
distance, table = min_edit_distance(str1, str2)
operations = edit_operations_traceback(str1, str2, table)
print("Edit Operations:")
for op in operations:
    print(op)