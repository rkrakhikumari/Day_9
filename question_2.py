def reverse_word(string):
    words = string.split()
    reversed_word = words[::-1]
    reversed_string = " ".join(reversed_word)
    return reversed_string

input_string = "HELLO WORLD"
output_string = reverse_word(input_string)
print(output_string)
