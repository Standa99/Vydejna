import debug_toolbar
from django.contrib import admin

from django.urls import include, path

from accounts.views import SubmittableLoginView, LogoutView, SubmittablePasswordChangeView
from viewer.views import (SparePartsListView, QuantityEditorListView, integer_view, QuantitySelect, OrderedPartsView,
    OrderPartsView, NewSparePartView, SparePartUpdateView, SparePartBRTcodeFormView, ReturnPartsView,
    QuantitySelectReturnListView)

accounts_patterns=[
    path('login/', SubmittableLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_change/', SubmittablePasswordChangeView.as_view(), name='password_change'),
]

urlpatterns = [
    path('admin_vydejna/', admin.site.urls),
    path('', SparePartsListView.as_view(), name='index'),
    path('quantity', QuantityEditorListView.as_view(), name='quantity'),
    path('quantity_select', QuantitySelect.as_view(), name='quantity_select'),
    path('quantity_select_return', QuantitySelectReturnListView.as_view(), name='quantity_select_return'),
    path('ordered_parts', OrderedPartsView.as_view(), name='ordered_parts'),
    path('order_parts', OrderPartsView.as_view(), name='order_parts'),
    path('return_parts', ReturnPartsView.as_view(), name='return_parts'),
    path('newsp', NewSparePartView.as_view(), name='newsp'),

    path('form_brt_code_input', SparePartBRTcodeFormView.as_view(), name='form_brt_code_input'),
    path('update/<pk>', SparePartUpdateView.as_view(), name='update'),


    # path('accounts/login/', SubmittableLoginView.as_view(), name='login'),
    # path('accounts/logout/', LogoutView.as_view(), name='logout'),
    # path('accounts/password_change/', SubmittablePasswordChangeView.as_view(), name='password_change'),
    path('__debug__', include(debug_toolbar.urls)),

    path('integer',integer_view, name='integer'),

    path('accounts/', include(accounts_patterns)),
]
