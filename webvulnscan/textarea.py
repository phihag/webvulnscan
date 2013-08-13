DEFAULT_VALUE = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr," \
                + "sed diam nonumy eirmod tempor invidunt ut labore et " \
                + "dolore magna aliquyam"


class TextArea(object):
    def __init__(self, element):
        self.element = element

    def _get_attrib_value(self, name):
        value = self.element.attrib.get(name)

        if value is None:
            return ""
        else:
            return value

    def get_type(self):
        return "textarea"

    def get_name(self):
        return self._get_attrib_value('name')

    def guess_value(self):
        placeholder = self._get_attrib_value("placeholder")
        if placeholder == "":
            return DEFAULT_VALUE
        else:
            return placeholder
