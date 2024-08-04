# giving all the words for numbers
num_words = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
    "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
    "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
    "seventy": 70, "eighty": 80, "ninety": 90, "hundred": 100,
    "thousand": 1000, "million": 1000000, "billion": 1000000000
}

# converting text to number
def text_to_num(text):
        text = text.strip().lower()
        words = text.split()
        number = 0
        current_number = 0
        last_scale = 1
        for word in words:
            if word in num_words:
                scale = num_words[word]
                if scale == 100:
                    if current_number == 0:
                        current_number = 1
                    current_number *= scale
                elif scale >= 1000:
                    number += current_number * scale
                    current_number = 0
                else:
                    if last_scale >= 100 and scale < 100:
                        number += current_number
                        current_number = scale
                    else:
                        current_number += scale
                last_scale = scale
            elif word == "and":
                continue
            else:
                raise ValueError(f"Invalid word in text: {word}")
        
        number += current_number
        return number