import re

with open('khmer_language.html', 'r') as khmer_file:
    str_text = khmer_file.read()
    str_re = r'<table class="wikitable".*?</table>'
    result = re.findall(str_re, str_text, re.S)
    with open('khmer_tables_parsed.txt', 'w') as parsed_file:
        for item in result:
            print(item, file=parsed_file)
            print('\n', file=parsed_file)
