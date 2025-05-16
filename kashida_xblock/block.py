import pkg_resources
from xblock.core import XBlock
from xblock.fields import Scope, String
from xblock.fragment import Fragment


class KashidaXBlock(XBlock):
    display_name = String(
        display_name="Kashida XBlock",
        default="Kashida XBlock",
        scope=Scope.settings,
    )

    def resource_string(self, path):
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")
    def studio_view(self, context=None):
        html = self.resource_string("templates/html/kashida_edit.html")
        frag = Fragment(html)
        return frag

    def student_view(self, context=None):
        html = self.resource_string("templates/html/kashida_edit.html")
        frag = Fragment(html)
        return frag

    @staticmethod
    def workbench_scenarios():
        return [
            ("Kashida XBlock - Basic", "<kashida_xblock/>"),
        ]
