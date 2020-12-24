from jinja2 import Template
name = 'Dhivya'
id = 15
tm = Template("My name is {{ name }} and my id is {{ id }}")
msg = tm.render(name=name, id=id)
print(msg)