from os.path import join
from jinja2 import Template


def render(template_name, folder='templates', **kwargs):
    """
    :param template_name: name template
    :param folder: folder where search template
    :param kwargs: params, sending in template
    :return:
    """
    file_path = join(folder, template_name)
    # Opening the template by name
    with open(file_path, encoding='utf-8') as f:
        template = Template(f.read())
    # Rendering template with params
    return template.render(**kwargs)
