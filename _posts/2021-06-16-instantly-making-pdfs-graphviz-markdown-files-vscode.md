---
layout: post
title: Instantly making PDFs with Graphviz from Markdown files in VSCode
tags: teaching python
published: false
---

Graphviz is a popular and powerful engine for creating diagrams and graphs without having to worry about the layout (usually...). VSCode has existing extensions that will show you the compiled graphviz diagram in your markdown file directly. This post explains how to turn that markdown file into a PDF instantly. This is handy for creating quick handouts that don't require the time or finesse of something like TikZ/LaTeX. This particular method requires VSCode and a number of extensions.

## Required extensions and modules

### VSCode

[Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one), among many other things, generates an HTML file from the Markdown source. 

[Graphviz Markdown Preview](https://marketplace.visualstudio.com/items?itemName=geeklearningio.graphviz-markdown-preview) compiles any graphviz code inside a `graphviz` labeled codeblock in a markdown file into a visual diagram. 

With support for LaTeX-style math equations as well, this might be enough for some. To make sure the graphviz diagrams are shown the same for everyone who sees the file, though, it's nice to have it as a pdf.

### Python

The core conversion to a PDF file is done via [headless Chrome](https://developers.google.com/web/updates/2017/04/headless-chrome). This allows you to use Chrome's print to PDF function without actually opening the application window. If Chrome is installed, this can be done with the following command (depending on your OS):

```
chrome --headless --disable-gpu --print-to-pdf https://www.nickdanis.com/
```

Local html files work the same way; just include the path instead of the URL. However, to automate the process, you can make a python script that uses these same tools under the hood. I based mine around [pyhtml2pdf](https://pypi.org/project/pyhtml2pdf/). This package can do the following:

```python
from pyhtml2pdf import converter
converter.convert(f'file:///{input_path}', 'output.pdf')
```

Here, `input_path` is the full path to the HTML file, and `output.pdf` is the resulting PDF file. This package should download the necessary Chrome web drivers necessary if your computer does not already have them installed. 

## Automating the process

So far, you can invoke the `Print to HTML` function from VSCode to convert a Graphviz-rich markdown file to an HTML file, and then use either a shell command or python script to convert that to a PDF file. Note that the HTML files outputted by this extension are quite large (in my case, about 2mb for a simple markdown file), as there is lots of embedded code. First, we will build a python script that takes a filename as an argument, and then we will combine these tools into a VSCode [Task](https://code.visualstudio.com/docs/editor/tasks). 

### The python script

The following script accepts and requires a single argument in the commandline. This should be the name of the file to be converted. The converter needs an html file. 

```python
import sys, os, re
from pyhtml2pdf import converter

# save working directory
cwd = os.getcwd()

# get passed argument
input_raw = sys.argv[1]

# substitute file extension (more on this later)
input_name = re.sub(r'\.md','.html',input_raw)
input_path = os.path.abspath(input_name)

# create output name dot pdf
output_name = re.sub('\.md','.pdf',input_raw)

# the actual conversion
converter.convert(f'file:///{input_path}', output_name)

# delete the html file
os.remove(input_name)

```

Save this somewhere. Maybe in the current project directory for now.

### The build task

The `converter` object needs an HTML file. However, in VSCode, work is done on a Markdown file. Invoking the `Print current document to HTML` command will generate a file, but then we still have to pass this file to the script. To do this all in one step, we will create two **tasks**: one for MD to HTML, and one for HTML to PDF. Then, we will create a compound task, that runs these in order. This compound task will be the one that does the conversion in a single step. In VSCode, open the command palette and find `Tasks: Open User Tasks`. Mine looks like this. 

```json
{
    "version":"2.0.0",
    "tasks":[
        {
            "label": "MD-to-HTML",
            "command": "${command:markdown.extension.printToHtml}",
            "problemMatcher": []
        },
        {
            "label": "HTML-to-PDF",
            "type": "shell",
            "command": "python {PATH-TO-SCRIPT}.py ${file}"
        },
        {
            "label": "BuildPDF",
            "dependsOn": [
                "MD-to-HTML",
                "HTML-to-PDF"
            ],
            "problemMatcher": []
        }
    ]
}
```

You will need to replace `{PATH-TO-SCRIPT}` with whatever the path is to your script. The first task, `MD-to-HTML`, simply calls the command to conver the Markdown file to HTML. On calling this task, an HTML file with the same basename as the markdown file will appear in the current directory. The second task, `HTML-to-PDF`, runs the python script created earlier. Notice that it's called with the `${file}` variable after it; this means VSCode will pass the current file's name as an argument, which the script then parses. However, this argument has an `.md` extension, because that's all VSCode sees at the time of the compound task call. The few lines of python code are there to replace `.md` in the filename string to `.html`. We can be sure that this HTML file will always be present because of the `BuildPDF` compound task. This task as the property `dependsOn`, which takes a list of existing tasks (called by their `"label"`.) Because `MD-to-HTML` is called first, the necessary HTML file will always be there for `HTML-to-PDF` to convert.

At this point, it's done. `BuildPDF` can be invoked from the command palatte by name, and a PDF of the active markdown file will appear in the working directory. The HTML file is deleted in the process to avoid bloat. From here, you can also set a keyboard shortcut for the compound task, so it is indeed instant. 