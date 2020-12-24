from jinja2 import Template

data = '''
{% raw %}
His name is {{ name }}
{% endraw %}
'''

#:It will print in literal meaning

tm = Template(data)
msg = tm.render(name='Dhivya')

print(msg)
