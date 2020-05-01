# from django import template
# from django.conf import settings
#
# register = template.Library()
#
# # https://docs.djangoproject.com/en/3.0/howto/custom-template-tags/
#
# @register.simple_tag(name="settings")
# def get_settings(var_name):
#     return getattr(settings, var_name, "")
#
# # Usage in templates:
# # {% load skeleton_tags %}
# # {% settings_value "LANGUAGE_CODE" %}
