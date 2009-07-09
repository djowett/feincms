from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import translation

from feincms.module.page.models import Page


def handler(request, path=None):
    if path is None:
        path = request.path

    page = Page.objects.page_for_path_or_404(path)

    response = page.setup_request(request) or \
               render_to_response(page.template.path, {
                    'feincms_page': page,
                    }, context_instance=RequestContext(request))

    return response
    