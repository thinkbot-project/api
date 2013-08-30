from django.views.generic import TemplateView
from django.conf import settings

from rest_framework.authtoken.models import Token

class HomePageView(TemplateView):

    template_name = "pages/home.html"


class AboutPageView(TemplateView):

    template_name = "pages/about.html"


class DocsPageView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(DocsPageView, self).get_context_data(**kwargs)

        if self.request.user.is_authenticated():
            print self.request.user
            context['user_token'] = Token.objects.get(user=self.request.user)
        return context

    template_name = "pages/docs.html"


class PricingPageView(TemplateView):

    template_name = "pages/pricing.html"


class SupportPageView(TemplateView):

    template_name = "pages/support.html"


class TermsPageView(TemplateView):

    template_name = "pages/terms.html"


class PrivacyPageView(TemplateView):

    template_name = "pages/privacy.html"
