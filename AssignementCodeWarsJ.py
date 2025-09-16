1.
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"
2.
def number_to_string(num):
    return str(num)
3.
def no_space(x):
    return x.replace(" ", "")
4. 
def get_count(sentence):
    vowels = "aeiou"
    count = 0

    for char in sentence:
        if char in vowels:
            count += 1

    return "The Count is: " + str(count)


