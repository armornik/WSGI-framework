# from os.path import join
# from jinja2 import Template
from jinja2 import FileSystemLoader
from jinja2.environment import Environment


def render(template_name, folder='templates', **kwargs):
    """
    :param template_name: name template
    :param folder: folder where search template
    :param kwargs: params, sending in template
    :return:
    """

    # # Variant with jinja2 - Template and os
    # file_path = join(folder, template_name)
    # # Opening the template by name
    # with open(file_path, encoding='utf-8') as f:
    #     template = Template(f.read())
    # # Rendering template with params
    # return template.render(**kwargs)

    env = Environment()
    # path where search template
    env.loader = FileSystemLoader(folder)
    # load template
    template = env.get_template(template_name)
    return template.render(**kwargs)
