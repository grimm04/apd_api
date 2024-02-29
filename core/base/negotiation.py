from rest_framework.negotiation import DefaultContentNegotiation


class CustomContentNegotiation(DefaultContentNegotiation):
    def select_renderer(self, request, renderers, format_suffix=None):
        if request.method == 'POST':
            if format == request.data.get('format'):
                for renderer in self.filter_renderers(renderers, format):
                    if format==renderer.format:
                        return renderer,renderer.media_type
        return super().select_renderer(request, renderers, format_suffix)