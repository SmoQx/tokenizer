import time
import re


def date_translate(day, month, year):

    months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
              9: 'September', 10: 'October', 11: 'November', 12: 'December'}

    return f"{numbere_translate(int(day))} {months[int(month)]} {numbere_translate(int(year))}"


def time_translate(time):
    hour, minute = map(int, time.split(':'))

    hours = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
             10: 'ten', 11: 'eleven', 12: 'twelve'}
    minutes = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
               10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
               17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
               50: 'fifty'}

    if minute == 0:
        return f"{hours[hour]} o'clock"
    elif minute <= 20:
        return f"{minutes[minute]} past {hours[hour]}"
    else:
        return f"{minutes[minute // 10 * 10]} {minutes[minute % 10]} past {hours[hour]}"


def numbere_translate(number):
    ones = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    teens = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
             17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    tens = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}

    if number == 0:
        return 'zero'

    words = ''
    if number >= 1000:
        words += ones[number // 1000] + ' thousend '
        number %= 1000
    if number >= 100:
        words += ones[number // 100] + ' hundred '
        number %= 100
    if number >= 20:
        words += tens[number // 10 * 10] + ' '
        number %= 10
    elif number >= 10:
        return words + teens[number]
    if number > 0:
        words += ones[number]

    return words.strip()


def roman_numbere_translate(roman):
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    result = 0

    i = 0
    while i < len(roman):
        current_value = roman_map[roman[i]]

        if i < len(roman) - 1 and roman_map[roman[i + 1]] > current_value:
            result += roman_map[roman[i + 1]] - current_value
            i += 2   
        else:
            result += current_value
            i += 1
    
    result = numbere_translate(result)

    return result


def tokenize(text: str) -> list:
    index = 1
    pattern = r'\b(?:\d{1,2}/\d{1,2}/\d{2,4}|(?:[0-1]?[0-9]|2[0-3]):[0-5][0-9](?::[0-5][0-9])?|(?:[IVXLCDM])+|\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4}|\w+|[^\w\s])\b'
    token_list = []
    
    for match in re.finditer(pattern, text):
        # Determine the type of token
        token = match.group()
        if match := re.match(r'(\d{1,2})/(\d{1,2})/(\d{2,4})', token):
            token_type = 'date'
            day, month, year = match.groups()
            value = date_translate(day, month, year)
        elif re.match(r'(?:[0-1]?[0-9]|2[0-3]):[0-5][0-9](?::[0-5][0-9])?', token):
            token_type = 'time'
            value = time_translate(token)
        elif re.match(r'(?:[IVXLCDM])+', token) and token.isupper():
            token_type = 'roman_numeral'
            value = roman_numbere_translate(token)
        elif match := re.match(r'(\d{4})-(\d{2})-(\d{2})', token):
            token_type = 'date'
            year, month, day = match.groups()
            value = date_translate(day, month, year)
        elif match := re.match(r'(\d{2})/(\d{2})/(\d{4})', token):
            token_type = 'date'
            day, month, year = match.groups()
            value = date_translate(day, month, year)
        elif re.match(r'\w+', token):
            token_type = 'word'
            value = token
        else:
            token_type = ''
            value = ''

        token_dict = {
            'index': index,
            'type': token_type,
            'word': token,
            'value': value
        }
        
        token_list.append(token_dict)

        index = index + 1
    
    return token_list


def measure_execution_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time


if __name__ == "__main__":
    text = "Text to be tokenized. Maybe. Very number 10, XIX, XV"
    tokens, time_to_finish1 = measure_execution_time(tokenize, text)
    for token in tokens:
        print(token)

    text = "Today is 12/05/2024, the time is 9:29. Chapter XVII discusses Roman history. The deadline is approaching, it's 2024-05-12 or 05/12/2024. The meeting is scheduled for 09:00 AM."
    tokens, time_to_finish2 = measure_execution_time(tokenize, text)
    for token in tokens:
        print(token)

#    with open('lore_ipsum.txt' ,'r') as text:
#        text = text.read()
#    tokens, time_to_finish3 = measure_execution_time(tokenize, text)
#    for token in tokens:
#        print(token)

    print("first text ", time_to_finish1, "seconds")
    print("second text ", time_to_finish2, "seconds")
#    print("third text ", time_to_finish3, "seconds")
