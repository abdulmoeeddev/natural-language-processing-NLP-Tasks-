def needleman_wunsch_alignment(seq1, seq2, match_score=1, mismatch_score=-1, gap_penalty=-1):
    # Initialize the alignment matrix
    len1, len2 = len(seq1), len(seq2)
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    
    # Initialize the first row and column with gap penalties
    for i in range(1, len1 + 1):
        dp[i][0] = i * gap_penalty
    for j in range(1, len2 + 1):
        dp[0][j] = j * gap_penalty
    
    # Fill the alignment matrix
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            match = dp[i - 1][j - 1] + (match_score if seq1[i - 1] == seq2[j - 1] else mismatch_score)
            delete = dp[i - 1][j] + gap_penalty
            insert = dp[i][j - 1] + gap_penalty
            dp[i][j] = max(match, delete, insert)
    
    return dp[len1][len2], dp

# Test the function
seq1 = "GATTACA"
seq2 = "GCATGCU"
alignment_score, table = needleman_wunsch_alignment(seq1, seq2)
print(f"Alignment Score: {alignment_score}")
for row in table:
    print(row)