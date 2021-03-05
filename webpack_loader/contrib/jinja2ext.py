import jinja2.ext

from .. import utils


def stylesheet_pack(*names, **kwargs):
    """
    TODO: refactor
    """
    tags = []
    for name in names:
        sub_tags = utils.get_as_tags(
            name, extension="css", attrs=kwargs.get("attrs", "")
        )
        for sub_tag in sub_tags:
            if sub_tag not in tags:
                tags.append(sub_tag)
    return jinja2.Markup("\n".join(tags))


def javascript_pack(*names, **kwargs):
    """
    TODO: refactor
    """
    tags = []
    for name in names:
        sub_tags = utils.get_as_tags(
            name, extension="js", attrs=kwargs.get("attrs", "")
        )
        for sub_tag in sub_tags:
            if sub_tag not in tags:
                tags.append(sub_tag)
    return jinja2.Markup("\n".join(tags))


class WebpackExtension(jinja2.ext.Extension):
    def __init__(self, environment):
        super(WebpackExtension, self).__init__(environment)
        environment.globals["stylesheet_pack"] = stylesheet_pack
        environment.globals["javascript_pack"] = javascript_pack
