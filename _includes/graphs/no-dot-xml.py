import os,re

gvpath = '_includes/graphs/'
#gvpath = 'dot/test/'


graphs = [f for f in os.listdir(gvpath) if f.endswith('.svg')]
to_trim = []

xml = re.compile(r'(?s)<\?xml.*?">')

default_encoding = 'utf-8'

for file in graphs:
    with open(f"{gvpath}{file}",'r',encoding=default_encoding) as f:
        graph = f.read()
        if xml.search(graph):
            new_graph = xml.sub('',graph)
            to_trim.append((file,new_graph))

for file in [file for file, contents in to_trim]:
    os.rename(f"{gvpath}{file}",f"{gvpath}{file.replace('.svg','-xml.svg')}")

print(f"Trimming {len(to_trim)} file(s)...")

for file, contents in to_trim:
    with open(f"{gvpath}{file}",'w',encoding=default_encoding) as f:
        f.write(contents)

print("Deleting old files...")        

for file in [f for f in os.listdir(gvpath) if f.endswith('-xml.svg')]:
    os.remove(f"{gvpath}{file}")


print("Done.")


