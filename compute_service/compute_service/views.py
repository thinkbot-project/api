from django.views.generic import TemplateView
from django.conf import settings

class HomePageView(TemplateView):

    template_name = "pages/home.html"


class AboutPageView(TemplateView):

    template_name = "pages/about.html"


class DocsPageView(TemplateView):

    template_name = "pages/docs.html"


class SupportPageView(TemplateView):

    template_name = "pages/support.html"


class LegalPageView(TemplateView):

    template_name = "pages/legal.html"
