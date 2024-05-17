from django.http import HttpResponse


class PDFResponse(HttpResponse):
    def __init__(self, content=b'', *args, **kwargs):
        kwargs['content_type'] = 'application/pdf'
        super().__init__(content=content, *args, **kwargs)
