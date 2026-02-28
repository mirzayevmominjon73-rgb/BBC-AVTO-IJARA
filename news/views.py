from django.views.generic import TemplateView
from .models import News

class NewsListView(TemplateView):
    template_name = 'news/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_list'] = News.objects.all()
        return context
