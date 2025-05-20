import pkg_resources
from xblock.core import XBlock
from xblock.fields import Scope, String
from xblock.fragment import Fragment
from xblockutils.resources import ResourceLoader

loader = ResourceLoader(__name__)

class KashidaXBlock(XBlock):
    display_name = String(
        display_name="Kashida XBlock",
        default="Kashida XBlock",
        scope=Scope.settings,
    )

    def resource_string(self, path):
        """Handles static resources"""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def studio_view(self, context=None):
        """Studio editor view"""
        html = loader.render_django_template('static/html/kashida_edit.html', {})
        frag = Fragment(html)
        
        # Add static resources
        frag.add_css(self.resource_string("static/css/style.css"))
        frag.add_javascript(self.resource_string("static/js/main.js"))
        
        # Add CKEditor resources
        frag.add_javascript_url("https://cdn.ckeditor.com/ckeditor5/45.1.0/ckeditor5.umd.js")
        frag.add_css_url("https://cdn.ckeditor.com/ckeditor5/45.1.0/ckeditor5.css")
        
        return frag

    def student_view(self, context=None):
        """Student view - same as studio view"""
        return self.studio_view(context)