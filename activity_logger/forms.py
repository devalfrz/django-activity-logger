from django import forms

#i18n
from django.utils.translation import ugettext as _, ugettext_lazy as _lazy

class SearchEntriesForm(forms.Form):
    ALL = '0'
    ANONYMOUS = '1'
    AUTHENTICATED = '2'
    NOT_STAFF = '3'
    STAFF = '4'

    USER_CHOICES = (
        (ALL,_('All')),
        (ANONYMOUS,_('Anonymous')),
        (AUTHENTICATED,_('Authenticated')),
        (NOT_STAFF,_('Not Staff')),
        (STAFF,_('Staff')),
    )

    DAY_OF_THE_MONTH = '0'
    DAY_OF_THE_WEEK = '1'
    TIME_OF_THE_DAY = '2'
    YEAR = '3'

    DISPLAY_BY_CHOICES = (
        (DAY_OF_THE_MONTH,_('Day of the Month')),
        (DAY_OF_THE_WEEK,_('Day of the Week')),
        (TIME_OF_THE_DAY,_('Time of the day')),
        (YEAR,_('Year')),
    )
    
    BAR = '0'

    GRAPH_CHOICES = (
        (BAR,_('Bar')),
    )

    start_date = forms.DateField(label=_('Start Date'),required=False)
    end_date = forms.DateField(label=_('End Date'),required=False)
    users = forms.ChoiceField(label=_('Users'),initial=ALL,choices=USER_CHOICES)
    display_by = forms.ChoiceField(label=_('Display By'),initial=DAY_OF_THE_MONTH,choices=DISPLAY_BY_CHOICES)
    graph = forms.ChoiceField(label=_('Graph'),initial=BAR,choices=GRAPH_CHOICES)