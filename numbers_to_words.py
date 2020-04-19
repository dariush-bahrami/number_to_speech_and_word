def number_to_word(number):
    assert type(number) == int, 'Enter integer number!'
    assert len(str(number)) < 4, 'Enter a number with maximum 3 digits!'

    ones_digits = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
                   5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

    tens_digits_1 = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
                     14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
                     17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

    tens_digits = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
                   60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}

    hundreds = ' hundred'

    def one_digit_numbers_to_words(number):
        return ones_digits[int(number)]

    def two_digit_numbers_to_words(number):
        if 10 <= int(number) < 20:
            return tens_digits_1[int(number)]
        elif number[1] != '0':
            return (tens_digits[int(number[0]+'0')] +
                    '-' + one_digit_numbers_to_words(number[1]))
        else:
            return tens_digits[int(number[0]+'0')]

    def three_digit_numbers_to_words(number):
        if number[1] != '0':
            return (ones_digits[int(number[0])] + hundreds + ' and ' +
                    two_digit_numbers_to_words(number[1:]))
        elif number[2] != '0':
            return (ones_digits[int(number[0])] + hundreds + ' and ' +
                    one_digit_numbers_to_words(number[2]))
        else:
            return ones_digits[int(number[0])] + hundreds

    number = str(number)
    if len(number) == 1:
        return one_digit_numbers_to_words(number)

    if len(number) == 2:
        return two_digit_numbers_to_words(number)

    if len(number) == 3:
        return three_digit_numbers_to_words(number)

if __name__ == '__main__':
    number = 42
    number_string = number_to_word(number)

    # Saving to .txt file
    if not os.path.isdir('numbers_txt_files'):
        os.mkdir('numbers_txt_files')

    txt_path = f'numbers_txt_files/{number}.txt'

    with open(txt_path, mode='w') as opened_file:
        opened_file.write(number_string)
