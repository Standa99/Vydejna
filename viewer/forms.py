from django import forms
from viewer.models import SubCategory, StorePlace, StoreName, MainCategory, SparePart
from django.core.exceptions import ValidationError

class NewSparePartForm(forms.Form):
    order_code_brt = forms.CharField(max_length=128)
    order_code_suppliers = forms.CharField(max_length=128)
    name_CZ = forms.CharField(max_length=128)
    name_EN_DE = forms.CharField(max_length=128)
    main_category = forms.ModelChoiceField(queryset=MainCategory.objects.all())
    sub_category = forms.ModelChoiceField(queryset=SubCategory.objects)
    quantity = forms.IntegerField()
    price_CZ = forms.DecimalField(max_digits=20, decimal_places=2)
    price_EUR = forms.DecimalField(max_digits=20, decimal_places=2)
    store_place = forms.ModelChoiceField(queryset=StorePlace.objects)
    store_name = forms.ModelChoiceField(queryset=StoreName.objects)
    description = forms.CharField(widget=forms.Textarea, required=False)

class BrtCodeForm(forms.Form):
    order_code_brt = forms.CharField(max_length=128)


def capitalized_validator(value):
  if value[0].islower():
    raise ValidationError('Value must be capitalized.')

class SparePartModelForm(forms.ModelForm):

  class Meta:
    model = SparePart
    fields = '__all__'

