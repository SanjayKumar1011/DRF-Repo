#global filter is case sensitive where as custom is insenstive
import django_filters
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    designation= django_filters.CharFilter(field_name='designation',lookup_expr='iexact')
    emp_name= django_filters.CharFilter(field_name='emp_name',lookup_expr='icontains')
    #id =django_filters.RangeFilter(field_name='id')
    id_min= django_filters.CharFilter(method='filterByIdRange',label='from Emp Id')
    id_max= django_filters.CharFilter(method='filterByIdRange', label='TO Emp Id')
    class Meta:
        model=Employee
        fields=['designation','emp_name','id_min','id_max']

    def filterByIdRange(self,queryset,name,value):
        if name=='id_min':
            return queryset.filter(emp_id__gte=value)
        elif name=='id_max':
            return queryset.filter(emp_id__lte=value)
