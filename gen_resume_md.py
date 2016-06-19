from string import Template

header = "[joeykblack.github.io](http://joeykblack.github.io)"

header_with_phone = """[joeykblack.github.io](http://joeykblack.github.io)
(904) 662-8117"""

header_with_links = """[Home page](http://joeykblack.github.io)
[PDF Resume](http://joeykblack.github.io/resume/joeykblack_resume.pdf)"""

def output_template(header, ndms_rolls, filename):
    with open ("resume.template", "r") as template_file:
        template = template_file.read()
        d = dict(header=header, ndms_rolls=ndms_rolls)
        result = Template(template).substitute(d)
        with open(filename, "w") as output_file:
            output_file.write(result)

def load(fileName):
    with open (fileName, "r") as part:
        part_string = part.read()
        return part_string

def main():
    ndms_rolls_short = load("ndms_rolls_short.part")
	
    output_template(header, ndms_rolls_short, "joeykblack_resume.md")
    output_template(header_with_phone, ndms_rolls_short, "joeykblack_resume_with_phone.md")
    output_template(header_with_links, ndms_rolls_short, "index.md")
	
    ndms_rolls_long = load("ndms_rolls_long.part")
    output_template(header_with_phone, ndms_rolls_long, "joeykblack_resume_with_phone_for_dod.md")



if __name__ == "__main__":
    main()
