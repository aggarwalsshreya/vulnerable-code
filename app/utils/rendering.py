from jinja2 import Template


def render_custom_template(template_text, context):
    return Template(template_text).render(**context)  # CWE-1336


def unsafe_html(name):
    return f"<h1>Hello {name}</h1>"  # CWE-79
