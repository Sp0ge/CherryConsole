from jinja2 import Template
import os

def render_bot(name, args):
    f1 = open("templates/template_main.py", "r")

    s1 = f1.read()

    f1.close()

    template = Template(s1)

    os.mkdir(name)

    file_name = name+"/main.py" 
    f2 = open(file_name, "w")

    f2.write(template.render(token=args["token"]))

    f2.close()

    f3 = open(name+"/funcs.py", "a")
    
    f3.write("def work(text):")
    for i in range(args["n"]):
        f3.write("\n    if text =='"+str(args["q"][i][0])+"':\n        return '"+args["q"][i][1]+"'")
    f3.close()

    return 0
