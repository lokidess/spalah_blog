from django.forms import Textarea


class TinyMceWidget(Textarea):
    template_name = 'widgets/tiny_mce_widget.html'