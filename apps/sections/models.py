# from django.db import models
# from django.utils.translation import ugettext_lazy as _
# from django.contrib.auth import get_user_model
# from django_extensions.db.fields import AutoSlugField
#
# from virtunews.communs.models import Content
#
# User = get_user_model()
#
#
# class Section(Content):
#     path = AutoSlugField(_("Path"), editable=True, populate_from=['title', 'id'], unique=True)
#     color = models.CharField(_("Color"), blank=True, max_length=7)
#     icon = models.ImageField(_("icon"), upload_to='image/%Y/', null=True, blank=True)
#     svg = models.TextField(_("svg"), null=True, blank=True)
#     in_menu = models.BooleanField(_("Menu"), default=False)
#
#     def get_cor(self):
#         cor = self.color
#         cor_tag = '<div ' \
#                   'style="vertical-align: middle;display:inline-block;' \
#                   'width:20px;height:20px;background-color:' + cor + '"></div><span style="vertical-align: middle;">' \
#                                                                      '' + cor + '</span>'
#         return cor_tag
#
#     get_cor.allow_tags = True
#     get_cor.short_description = 'Color'
#
#     def __str__(self):
#         return self.title
