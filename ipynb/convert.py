
import os
import sys
import re

ipynb_file = sys.argv[1]

if not os.path.isfile(ipynb_file):
    abort("Incorrect path to ipynb file")

os.system("jupyter nbconvert --to markdown {}".format(ipynb_file))

prepend_str = "{{ site.baseurl }} /ipynb/"

# ![png](manifolds_files/manifolds_3_0.png)

md_file = os.path.splitext(ipynb_file)[0] + ".md"

tmp_f = "tmp.1"

with open(tmp_f, "w") as fw:
    with open(md_file, "r") as fr:
        for line in fr.readlines():
            m = re.match(r'(\!\[png\]\()(.*)', line)
            if m:
                mod_line = m.group(1) + prepend_str + m.group(2)
                fw.write(mod_line)
            else:
                fw.write(line)

os.system("rm {} && mv {} {}".format(md_file, tmp_f, md_file))
