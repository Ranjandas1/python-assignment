import django_filters
from .models import WheelForm

class WheelFormFilter(django_filters.FilterSet):
    submittedDate = django_filters.DateFromToRangeFilter()

    class Meta:
        model = WheelForm
        fields = ['formNumber', 'submittedBy', 'submittedDate']
