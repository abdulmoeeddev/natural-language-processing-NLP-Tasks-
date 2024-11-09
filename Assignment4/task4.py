from phonetics import soundex, metaphone

def phonetic_edit_distance(str1, str2, phonetic_func=soundex):
    # Convert strings to their phonetic representations
    phonetic_str1 = phonetic_func(str1)
    phonetic_str2 = phonetic_func(str2)
    
    # Calculate the edit distance between the phonetic representations
    distance, _ = min_edit_distance(phonetic_str1, phonetic_str2)
    
    return distance

# Test the function
str1 = "kitten"
str2 = "sitting"
distance = phonetic_edit_distance(str1, str2)
print(f"Phonetic Edit Distance: {distance}")