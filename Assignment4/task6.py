def traceback_alignment(seq1, seq2, dp, match_score=1, mismatch_score=-1, gap_penalty=-1):
    i, j = len(seq1), len(seq2)
    aligned_seq1, aligned_seq2 = [], []
    
    while i > 0 or j > 0:
        if i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + (match_score if seq1[i - 1] == seq2[j - 1] else mismatch_score):
            aligned_seq1.append(seq1[i - 1])
            aligned_seq2.append(seq2[j - 1])
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i - 1][j] + gap_penalty:
            aligned_seq1.append(seq1[i - 1])
            aligned_seq2.append('-')
            i -= 1
        else:
            aligned_seq1.append('-')
            aligned_seq2.append(seq2[j - 1])
            j -= 1
    
    return ''.join(reversed(aligned_seq1)), ''.join(reversed(aligned_seq2))

# Test the function
seq1 = "GATTACA"
seq2 = "GCATGCU"
alignment_score, table = needleman_wunsch_alignment(seq1, seq2)
aligned_seq1, aligned_seq2 = traceback_alignment(seq1, seq2, table)
print("Optimal Alignment:")
print(aligned_seq1)
print(aligned_seq2)