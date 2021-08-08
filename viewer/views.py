
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, FormView, UpdateView

from viewer.models import SparePart
from viewer.forms import NewSparePartForm, SparePartModelForm, BrtCodeForm
from django.forms.widgets import NumberInput



class SparePartsListView(LoginRequiredMixin, ListView):
  template_name = 'spare_parts_list.html'
  model = SparePart

class QuantityEditorListView(ListView):
    integer_field = NumberInput().media
    template_name = 'quantity_editor.html'
    model = SparePart

class QuantitySelect(LoginRequiredMixin, ListView):
    integer_field = NumberInput().media
    template_name = 'quantity_select.html'
    model = SparePart

class QuantitySelectReturnListView(LoginRequiredMixin, ListView):
    integer_field = NumberInput().media
    template_name = 'quantity_select_return.html'
    model = SparePart

class OrderedPartsView(LoginRequiredMixin, ListView):
    template_name = 'ordered_parts.html'
    model = SparePart

class OrderPartsView(LoginRequiredMixin, View):

    model = SparePart

    def post(self, request):
        ordered_parts = {key:int(value) for key, value in request.POST.items() if key!='csrfmiddlewaretoken'}
        list_ordered = []
        for part_name, quantity in ordered_parts.items():
            part = self.model.objects.get(order_code_brt=part_name)
            if part.quantity < quantity:                   # TODO check why if/else works? :D
                part.quantity == part.quantity
            else:
                part.quantity -= quantity
            part.save()
            # part.quantity -= quantity
            # part.save()
            list_ordered.append({'part_object': part, 'ordered_quantity': quantity})
        return render(request, 'ordered_parts.html', dict(ordered_parts=list_ordered))

class ReturnPartsView(LoginRequiredMixin, View):

    model = SparePart

    def post(self, request):
        ordered_parts = {key:int(value) for key, value in request.POST.items() if key!='csrfmiddlewaretoken'}
        list_ordered = []
        for part_name, quantity in ordered_parts.items():
            part = self.model.objects.get(order_code_brt=part_name)
            if part.quantity < quantity:                   # TODO check why if/else works? :D
                part.quantity == part.quantity
            else:
                part.quantity -= quantity*(-1)
            part.save()
            # part.quantity -= quantity
            # part.save()
            list_ordered.append({'part_object': part, 'ordered_quantity': quantity})
        return render(request, 'returned_parts.html', dict(ordered_parts=list_ordered))

def integer_view(request): #TODO delete useless view
    context = {}
    context['forms'] = NewSparePartForm
    return render(request, "integer_field_test.html", context)

class NewSparePartView(LoginRequiredMixin, FormView): #TODO dopsat do formuláře funkci umožňující rovnou přidávat nové Main,Sub, places, names
    template_name = 'form_create_NEW_part.html'
    form_class = NewSparePartForm
    success_url = reverse_lazy('newsp')

    def form_valid(self, form):
        result = super().form_valid(form)
        clean_data = form.cleaned_data
        SparePart.objects.create(
            order_code_brt=clean_data['order_code_brt'],
            order_code_suppliers=clean_data['order_code_suppliers'],
            name_CZ=clean_data['name_CZ'],
            name_EN_DE=clean_data['name_EN_DE'],
            main_category=clean_data['main_category'],
            sub_category=clean_data['sub_category'],
            quantity=clean_data['quantity'],
            price_CZ=clean_data['price_CZ'],
            price_EUR=clean_data['price_EUR'],
            store_place=clean_data['store_place'],
            store_name=clean_data['store_name'],
            description=clean_data['description'],
            )
        return result

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not request.user.username == 'admin_vydejna':
                return redirect('http://127.0.0.1:8000/accounts/login/')
            else:
                return super().dispatch(request, *args, **kwargs)

class SparePartUpdateView(UpdateView):
    template_name = 'form_update_sp.html'
    model = SparePart
    form_class = SparePartModelForm
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not request.user.username == 'admin_vydejna':
                return redirect('http://127.0.0.1:8000/accounts/login/')
            else:
                return super().dispatch(request, *args, **kwargs)

class SparePartBRTcodeFormView(LoginRequiredMixin, FormView):
    template_name = 'form_brt_code_input.html'
    model = SparePart
    form_class = BrtCodeForm
    # success_url = reverse_lazy('index')

    def form_valid(self, form):
        pk = SparePart.objects.get(order_code_brt=form.cleaned_data.get('order_code_brt')).pk
        return redirect('update', pk=pk)

    # def get_success_url(self):
        #     pk = SparePart.objects.get(order_code_brt=self.request.POST.get('order_code_brt')).pk
        #     return reverse_lazy('index')


