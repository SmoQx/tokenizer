import re

def tokenize(text: str) -> list:
    index = 1
    pattern = r'\b(?:\d{1,2}/\d{1,2}/\d{2,4}|(?:[0-1]?[0-9]|2[0-3]):[0-5][0-9](?::[0-5][0-9])?|(?:[IVXLCDM])+|\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4}|\w+|[^\w\s])\b'
    token_list = []
    
    for match in re.finditer(pattern, text):
        # Determine the type of token
        token = match.group()
        if re.match(r'\d{1,2}/\d{1,2}/\d{2,4}', token):
            token_type = 'date'
        elif re.match(r'(?:[0-1]?[0-9]|2[0-3]):[0-5][0-9](?::[0-5][0-9])?', token):
            token_type = 'time'
        elif re.match(r'(?:[IVXLCDM])+', token) and token.isupper():
            token_type = 'roman_numeral'
        elif re.match(r'\d{4}-\d{2}-\d{2}', token) or re.match(r'\d{2}/\d{2}/\d{4}', token):
            token_type = 'date'
        elif re.match(r'\w+', token):
            token_type = 'word'
        else:
            token_type = 'none'

        token_dict = {
            'index': index,
            'type': token_type,
            'value': token
        }
        
        token_list.append(token_dict)

        index = index + 1
    
    return token_list


if __name__ == "__main__":
    text = "Text to be tokenized. Maybe. Very number 10, XIX, XV"
    tokens = tokenize(text)
    for token in tokens:
        print(token)

    text = "Today is 12/05/2024, the time is 14:30. Chapter XVII discusses Roman history. The deadline is approaching, it's 2024-05-12 or 05/12/2024. The meeting is scheduled for 09:00 AM."
    for token in tokenize(text):
        print(token)
