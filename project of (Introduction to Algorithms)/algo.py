def analyze_sentence(sentence):
    # Initialize counters
    sentence_length = 0
    word_count = 0
    vowel_count = 0
    
    # Iterate through each character in the sentence
    for char in sentence:
        # Increment sentence length for each character
        sentence_length += 1
        
        # Check if the character is a space to count words
        if char == ' ':
            word_count += 1
        
        # Check if the character is a vowel (both lower and upper case)
        if char in "AEIOUaeiou":
            vowel_count += 1
    
    # Add 1 to word_count for the last word after the final space
    word_count += 1
    
    # Print the results
    print("Length of the sentence:", sentence_length)
    print("Number of words in the sentence:", word_count)
    print("Number of vowels in the sentence:", vowel_count)
