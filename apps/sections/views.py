# from datetime import datetime
#
# from django.core.paginator import Paginator
# from django.views.generic import TemplateView
#
# from virtunews.apps.articles.models import Article
# from virtunews.apps.sections.models import Section
#
#
# class SectionsView(TemplateView):
#     model = Section
#     template_name = 'sections/index.html'
#
#     def get_context_data(self, **kwargs):
#
#         p = {}
#         now = datetime.now()
#
#         page = self.request.GET.get('page')
#
#         section = Section.objects.get(path=self.kwargs['path'])
#
#         article = Article.objects.\
#             prefetch_related('comments').\
#             select_related('section').\
#             filter(section__path=self.kwargs['path'], publish=True, publication_date__lte=now).\
#             order_by('-publication_date')
#
#         total = article.count()
#
#         sections = Section.objects.filter(in_menu=True).order_by('title')
#
#         article_per_page = Paginator(article, 16)
#
#         result = article_per_page.get_page(page)
#
#         time = datetime.now()
#
#         p['now'] = time
#         p['total'] = total
#         p['object'] = section
#
#         p['sections'] = sections
#         p['articles'] = result
#
#         return p
