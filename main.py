import argparse
import os
import pdfkit
from bs4 import BeautifulSoup, NavigableString
import math
from tqdm import tqdm
from xhtml2pdf import pisa

parser = argparse.ArgumentParser(description='Convert a PDF')

parser.add_argument('--file', required=True, dest = "file", help = "location of file")
parser.add_argument("--fixation", choices = [1, 2, 3, 4, 5], default = 1, dest = "fix",  help = "The fixation value" )
parser.add_argument("--saccade", choices = [10, 20, 30, 40, 50], default = 10, dest = "sacc", help = "The saccade value")
parser.add_argument("--output", type = str,default = None, help = "The name or location of the output file", dest = "output")

args = parser.parse_args()

import uuid
temp_file_root = uuid.uuid4()

if not os.path.exists(args.file):
    raise Exception("The target file does not exist")

if args.file[-5:] != ".html":
    raise Exception("The file provided is not a html")

if args.output is not None and args.output[-4:0] != ".pdf":
    raise Exception("The output file is not a pdf extension")

# doc = aw.Document(args.file)
# doc.save(f"./{temp_file_root}.html")

# the fixation controls the amount of bold per word. The higher the fixation the fewer part of hte word is bold (i.e
# if the fixation is 5 only 1/6 of the word is bolder but if it 1 1/2 of the word is bolded.

# the saccade controls how far apart the bolded words are. I.e the hgiehr the saccade the farther apart the words are
# that we end up bolding

def convert_to_bionic(element, soup, fixation=1, saccade=10):
    text = element.text
    element.string = ""
    word_list = text.split(" ")
    for i in range(len(word_list)):
        word = word_list[i]
        if word == "":
            a = 1
        else:
            saccade_value = round(saccade // 13) + 1
            if i % saccade_value == 0:
                split_word = max(1, len(word) * 2.4 / (fixation + 2.1))
                if len(word) <= 3:
                    split_word = math.floor(split_word)
                else:
                    split_word = round(split_word)
                new_b = soup.new_tag("b")
                new_b.string = word[0:split_word]
                element.append(new_b)

                element.append(NavigableString(word[split_word:] + " "))

            else:
                element.append(NavigableString(word + " "))


html_root = args.file[0:-5]
with open(args.file, encoding='utf-8') as fp:
    soup = BeautifulSoup(fp, 'html.parser')

for a in tqdm(soup.findAll(['span', 'p'])):
    convert_to_bionic(a, soup)

if args.output is not None:
    output = args.output
else:
    output = f"{html_root}_bionic.pdf"


result_file = open(output, "w+b")
pisa_status = pisa.CreatePDF(str(soup), dest = result_file)
result_file.close()
pisa_status



