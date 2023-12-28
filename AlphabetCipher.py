

alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_lower = alphabet_upper.lower()
message = 'xmarksthespot'
keyword = 'pine'
message_length = len(message)

def create_substitution_chart():
    
    substitution_chart = []

    for i in range(26):
        rotated_alphabet = alphabet_lower[i:] + alphabet_lower[:i]
       # print(rotated_alphabet)
        substitution_chart.append(rotated_alphabet.lower())
    return substitution_chart

def generating_repeated_keyword(length, key):

    repeated_keyword = []
    keyword_idx = 0

    for message_idx in range(message_length):
        repeated_keyword.append(keyword[keyword_idx])
        keyword_idx += 1
        if keyword_idx >= len(keyword):
            keyword_idx = 0


    return repeated_keyword    

def encode_message(message, repeated_keyword):
    column_index = []
    row_index = []
    encoded_message = []
    for letter in message:
        for column_letter in range(len(alphabet_lower)):
            if letter == alphabet_lower[column_letter]:
                column_index.append(column_letter)
                print(column_index)
                continue
    
    for letter in repeated_keyword:
        for row_letter in range(len(alphabet_lower)):
            if letter == alphabet_lower[row_letter]:
                row_index.append(row_letter)
                print(row_index)
                continue

    for i in range(len(column_index)):
        encoded_message.append(substition_chart[column_index[i]][row_index[i]])
    return encoded_message


substition_chart = create_substitution_chart()
repeated_keyword = generating_repeated_keyword(message_length, keyword)
print(encode_message(message, repeated_keyword))
