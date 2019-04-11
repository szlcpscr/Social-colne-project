from django.views.generic import TemplateView


class TestPage(TemplateView):
    template_name = 'test.html'


class TestPage2(TemplateView):
    template_name = 'test2.html'


class ThanksPage(TemplateView):
    template_name = 'thanks.html'


class ThanksPage2(TemplateView):
    template_name = 'thanks2.html'


class HomePage(TemplateView):
    template_name = 'index.html'
