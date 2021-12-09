import re

weird_chars = ['-', '‘', '’', '।', '/', '\u200c', '\x94', '"', 
               '\u200d', '\x93' ,'…','“', '”', '–', '_', '—', '\u200e',
               "«", "»", "(", ")", "+", "−"]

remove_weird_chars_pattern = re.compile('[' + ''.join(weird_chars) + ']', flags=re.UNICODE)

all_punc = ['!', '?', ',', ';', ':', '.']

newsent_punc = ['!', '?', '.']

def number_convert(text, num_dict):
    text_norm = ""
    for l in text.split('\n'):
        line = ""
        for t in l.split():
            m = re.search(r'[0-9]', t) 
            if m:
                if t in num_dict:
                    textualized = num_dict[t]
                    line += textualized + " "
                else:
                    print("WARNING: %s not found in numbers dictionary"%(t))

            else:
                line += t + " "
        line = line[:-1]
        text_norm += line + "\n"     

    return text_norm

def normalize_text(text, newline_at_each_sent=False, remove_punc=False, num_dict=None):
    clean_text = remove_weird_chars_pattern.sub(r' ', text)

    if newline_at_each_sent:
        pattern = re.compile('([' + ''.join(newsent_punc) + '])', flags=re.UNICODE)
        clean_text = pattern.sub(r'\1\n', clean_text)

    if remove_punc:
        pattern = re.compile('[' + ''.join(all_punc) + ']', flags=re.UNICODE)
        clean_text = pattern.sub(r' ', clean_text)
        clean_text = clean_text.lower()

    if num_dict:
        clean_text = number_convert(clean_text, num_dict)
    clean_text = re.sub(' +', ' ', clean_text)
    clean_text = re.sub('\n +', '\n', clean_text)
    clean_text = re.sub('\n+', '\n', clean_text)
    clean_text = clean_text.strip()

    return clean_text