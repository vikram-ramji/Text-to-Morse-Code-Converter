# TODO 1: Get Morse code Alphabets, Numbers and Characters
with open("morse.csv") as morse_data_file:
    morse_data = {s.split(',')[0]: s.split(',')[1].strip('\n') + " " for s in morse_data_file.readlines()}
    morse_data[','] = '__..__ '


# TODO 2: Create function that converts text to morse code
def text_to_morse_converter(text: str):
    morse_code = ""
    for a in text.upper():
        morse_code += morse_data[a]
    return morse_code


print("Hi! Welcome to text to morse code converter.\nTo get started, enter the text you wish to convert below(Note: "
      "Underscore character (_) is not accepted).")
input_text = input("Text: ")
print(f"Morse Code: {text_to_morse_converter(input_text)}")
