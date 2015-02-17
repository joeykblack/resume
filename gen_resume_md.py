from string import Template

header = "joeykblack.github.io"

header_with_phone = """joeykblack.github.io
(904) 662-8117"""

header_with_links = """[Home page](http://joeykblack.github.io)
[PDF Resume](http://joeykblack.github.io/resume/joeykblack_resume.pdf)"""

def output_template(header, filename):
    with open ("resume.template", "r") as template_file:
        template = template_file.read()
        d = dict(header=header)
        result = Template(template).substitute(d)
        with open(filename, "w") as output_file:
            output_file.write(result)

def main():
    output_template(header, "joeykblack_resume.md")
    output_template(header_with_phone, "joeykblack_resume_with_phone.md")
    output_template(header_with_links, "index.md")




if __name__ == '__main__':
    main()
