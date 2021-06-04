import datetime, string, re
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

def get_date():
    date = input("What is the post date? ")
    global post_date
    if date == "today":
        post_date = datetime.date.today()
    else:
        post_date = datetime.datetime.strptime(date, '%Y-%m-%d')
    return

def get_title():
    title = input("What is the post title? ")
    title_stripped = re.sub(rf'[{string.punctuation}]','',title)
    filetitle = [word.lower() for word in title_stripped.split() if word not in stop_words]
    if len(filetitle) > 7:
        filetitle = filetitle[:8]
    return title, '-'.join(filetitle)

def build_header(title):
    header = f"---\nlayout: post\n"
    header += f"title: {title}\n"
    header += f"tags:\n"
    header += f"published: false\n"
    header += f"---\n"
    return header

while True:
    try:
        get_date()
        break
    except:
        print("Could not parse date. Try again.")

title, filetitle = get_title()
filename = f"{post_date.strftime('%Y-%m-%d')}-{filetitle}.md"

contents = build_header(title)

with open(f"_posts/{filename}", "w") as f:
    f.write(contents)

print(f"New post created: {filename}")