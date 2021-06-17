import yaml, os, re
from pyhtml2pdf import converter

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
        urlname = re.sub(r'\.md','',syl)
        pdfname = re.sub(r'\.md','.pdf',syl)
        converter.convert(
            f'https://www.nickdanis.com/syllabi/{urlname}', 
            f'assets/pdfsyllabi/{pdfname}')


# convert cv
converter.convert(f'https://www.nickdanis.com/cv/', f'assets/pdfs/danis-cv.pdf') 