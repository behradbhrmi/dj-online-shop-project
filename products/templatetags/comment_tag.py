from django import template

register = template.Library()


@register.filter()
def only_demonstrable_messages(comments):
    return comments.filter(demonstrable=True)
