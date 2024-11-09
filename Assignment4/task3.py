def weighted_min_edit_distance(str1, str2, insertion_cost=1, deletion_cost=1, substitution_cost=1):
    # Initialize the distance matrix
    len1, len2 = len(str1), len(str2)
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    
    # Fill the distance matrix
    for i in range(len1 + 1):
        for j in range(len2 + 1):
            if i == 0:
                dp[i][j] = j * insertion_cost  # Insertion
            elif j == 0:
                dp[i][j] = i * deletion_cost  # Deletion
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No operation needed
            else:
                dp[i][j] = min(dp[i - 1][j] + deletion_cost,    # Deletion
                               dp[i][j - 1] + insertion_cost,    # Insertion
                               dp[i - 1][j - 1] + substitution_cost)  # Substitution
    
    return dp[len1][len2], dp

# Test the function
str1 = "kitten"
str2 = "sitting"
insertion_cost = 1
deletion_cost = 1
substitution_cost = 2
distance, table = weighted_min_edit_distance(str1, str2, insertion_cost, deletion_cost, substitution_cost)
print(f"Weighted Minimum Edit Distance: {distance}")
for row in table:
    print(row)