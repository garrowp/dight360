from glob import glob
import nltk
import re

'''Feature 1: Years'''

re_year = r'[0-9]{4}'


'''Feature 2: Ending Punctuation'''

re_punc = r'\b(\?|\.|!|\?|(?:\.\.\.))'

'''Feature 3: Contractions'''

re_cont = r'(\w\'(?:s|t|(?:ll)|(?:ve)|m|d))'


h_re = r'<h>(.*?)<'
p_re = r'<p>(.*?)<'


filenames = glob('Mini-CORE/*.txt')

with open('output.tsv', 'w') as out_file:
    header = 'Filename\tYears\tPunctuation\tContractions\tRegister'
    print(header, file=out_file)

    for filename in filenames:
        register_search = r'Mini-CORE/1\+(\w{2})'
        register = re.findall(register_search, filename)[0]

        adjust_filename_search = r'Mini-CORE/(.*)'
        adjusted_filename = re.findall(adjust_filename_search, filename)[0]

        with open(filename, 'r') as f:
            raw_text = f.read()
            h_text = ' '.join(re.findall(h_re, raw_text, re.S))
            p_text = ' '.join(re.findall(p_re, raw_text, re.S))
            file_text = h_text + ' ' + p_text

            num_years = len(re.findall(re_year, file_text))
            year_rate = num_years / 1000

            num_end_punc = len(re.findall(re_punc, raw_text, re.S))
            end_punc_rate = num_end_punc / 1000

            num_cont = len(re.findall(re_cont, raw_text))
            cont_rate = num_cont / 1000

            values = adjusted_filename + '\t' + str(year_rate) + '\t'
            values += str(end_punc_rate) + '\t' + str(cont_rate) + '\t'
            values += register
            print(values, file=out_file,)
