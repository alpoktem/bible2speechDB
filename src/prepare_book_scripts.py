from bs4 import BeautifulSoup
import os
import sys
from text_utils import normalize_text

book_id = sys.argv[1]
usx_path = sys.argv[2]
out_text_path = sys.argv[3]
numbers_csv_path = sys.argv[4]
chapter_utterance = sys.argv[5]

#Read number dictionary
NUMBERS_DICT = {l.strip().split('\t')[0]:l.strip().split('\t')[1] for l in open(numbers_csv_path, 'r').readlines()}

usx_content = open(usx_path, 'r')
soup = BeautifulSoup(usx_content, features="lxml")

title = soup.find("para", {"style": "h"}).text
code = soup.find("book")['code']

chapters_original = {}
chapters_segmented = {}
chapters_normalized = {}
chapter_text = ""

for elem in soup.usx.children:
    if elem.name == 'chapter' and 'sid' in elem.attrs:
        chapter_text = ""
        chapter_no = elem['number']
        chapter_id = code + "_" + chapter_no.zfill(3)
        print(chapter_id)

        chapter_text = title + " " + chapter_utterance + " " + chapter_no + "\n"
    elif chapter_text and elem.name == 'para':
        if elem['style'] not in ['b', 'r']:
            for v in elem.children:
                if not v.name and not v.isspace():
                    chapter_text += v.strip() + " "
                elif v.name == "char":
                    chapter_text += v.text
        chapter_text += '\n'
    elif elem.name == 'chapter' and 'eid' in elem.attrs:
        chapters_original[chapter_id] = chapter_text
        chapters_segmented[chapter_id] = normalize_text(chapter_text, newline_at_each_sent=True, remove_punc=False, num_dict=NUMBERS_DICT)
        chapters_normalized[chapter_id] = normalize_text(chapter_text, newline_at_each_sent=True, remove_punc=True, num_dict=NUMBERS_DICT)

original_out_dir = os.path.join(out_text_path, "original", book_id)
segmented_out_dir = os.path.join(out_text_path, "segmented", book_id)
normalized_out_dir = os.path.join(out_text_path, "normalized", book_id)

if not os.path.exists(original_out_dir):
	os.makedirs(original_out_dir)
if not os.path.exists(segmented_out_dir):
	os.makedirs(segmented_out_dir)
if not os.path.exists(normalized_out_dir):
	os.makedirs(normalized_out_dir)

for chap_id in chapters_normalized:
	out_original_path = os.path.join(original_out_dir, chap_id + ".txt")
	with open(out_original_path, 'w') as f:
		f.write(chapters_original[chap_id])

	out_segmented_path = os.path.join(segmented_out_dir, chap_id + ".txt")
	with open(out_segmented_path, 'w') as f:
		f.write(chapters_segmented[chap_id])

	out_normalized_path = os.path.join(normalized_out_dir, chap_id + ".txt")
	with open(out_normalized_path, 'w') as f:
		f.write(chapters_normalized[chap_id])

	

