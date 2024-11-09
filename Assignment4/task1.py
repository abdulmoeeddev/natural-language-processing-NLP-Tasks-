def min_edit_distance(str1, str2):
    # Initialize the distance matrix
    len1, len2 = len(str1), len(str2)
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    
    # Fill the distance matrix
    for i in range(len1 + 1):
        for j in range(len2 + 1):
            if i == 0:
                dp[i][j] = j  # Insertion
            elif j == 0:
                dp[i][j] = i  # Deletion
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No operation needed
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],    # Deletion
                                   dp[i][j - 1],    # Insertion
                                   dp[i - 1][j - 1])  # Substitution
    
    return dp[len1][len2], dp

# Test the function
str1 = "kitten"
str2 = "sitting"
distance, table = min_edit_distance(str1, str2)
print(f"Minimum Edit Distance: {distance}")
for row in table:
    print(row)