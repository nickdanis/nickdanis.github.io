import yaml, os, re, sys
from pyhtml2pdf import converter
from dateutil.parser import parse
from datetime import datetime, timedelta

# makes pdfs from live web versions
raw_date = sys.argv[1]

if raw_date == "today":
    update_after = datetime.today() - timedelta(days = 1)
else:
    update_after = parse(raw_date)

print(f"Updating PDFs modified after {update_after}...")

def get_tags(raw_contents):
    y_start = raw_contents.index('---\n')
    y_end = raw_contents.index('---\n',1)
    header = raw_contents[y_start:y_end]
    tags = yaml.safe_load("".join(header))
    return tags

syllabi = [f for f in os.listdir('_syllabi/') if f.endswith('.md')]

# convert all syllabi with pdf: true
for syl in syllabi:
    raw_contents = []
    with open(f"_syllabi/{syl}", 'r') as file:
        for line in file:
            raw_contents.append(line)
    tags = get_tags(raw_contents)
    if tags.get('pdf') == True:
        last_edited = parse(tags.get('last-updated'))
        if update_after < last_edited:
            urlname = re.sub(r'\.md','',syl)
            pdfname = re.sub(r'\.md','.pdf',syl)
            print(f"Generating {pdfname}...")
            converter.convert(
                f'https://www.nickdanis.com/syllabi/{urlname}', 
                f'assets/pdfsyllabi/{pdfname}')


# convert cv
cv_contents = []
with open('cv.md','r') as file:
    for line in file:
        cv_contents.append(line)
    tags = get_tags(cv_contents)
    last_edited = parse(tags.get('last-updated'))
    if update_after < last_edited:
        print("Generating danis-cv.pdf...")
        converter.convert(f'https://www.nickdanis.com/cv/', f'assets/pdfs/danis-cv.pdf') 