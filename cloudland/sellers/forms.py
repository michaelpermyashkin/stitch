from django import forms
from store.models import Product, Seller

from crispy_forms.bootstrap import AppendedText, PrependedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from crispy_forms.layout import Field


class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'category', 'price', 'shipping_cost', 'description_short', 'description_full', 'product_image', 'quantity']

    def __init__(self, *args, **kwargs):
        super(ProductEditForm, self).__init__(*args, **kwargs)
        self.fields['description_short'].widget.attrs.update({
            'rows':'2'})
        self.fields['quantity'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '0',
            'type': 'text'})
        self.fields['price'].widget.attrs.update({
            'label': 'Price',
            'class': 'form-control',
            'placeholder': '0.00',
            'type': 'text'})
        self.fields['shipping_cost'].widget.attrs.update({
            'label': 'Shipping Price',
            'placeholder': '0.00',
            'class': 'form-control',
            'type': 'text'})

class ProductAddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'category', 'price', 'shipping_cost', 'description_short', 'description_full', 'product_image', 'quantity', 'seller']

    def __init__(self, *args, **kwargs):
        super(ProductAddForm, self).__init__(*args, **kwargs)
        self.fields['description_short'].widget.attrs.update({
            'rows':'2'})
        self.fields['quantity'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '0',
            'type': 'text'})
        self.fields['price'].widget.attrs.update({
            'label': 'Price',
            'placeholder': '0.00',
            'class': 'form-control',
            'type': 'text'})
        self.fields['shipping_cost'].widget.attrs.update({
            'label': 'Shipping Price',
            'placeholder': '0.00',
            'class': 'form-control',
            'type': 'text'})


class SellerBioEditForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['seller_full_name', 'seller_listing_name', 'profile_picture', 'bio_description', 'email']

    def __init__(self, *args, **kwargs):
        super(SellerBioEditForm, self).__init__(*args, **kwargs)
        self.fields['seller_full_name'].widget.attrs.update({
            'label': 'Full Name',
            'class': 'form-control',
            'placeholder': 'Your name',
            'type': 'text'})
        self.fields['seller_listing_name'].widget.attrs.update({
            'label': 'Listing Name',
            'class': 'form-control',
            'placeholder': 'Your listing name',
            'type': 'text'})
        self.fields['bio_description'].widget.attrs.update({
            'label': 'Bio',
            'class': 'form-control',
            'placeholder': 'Bio...',
            'type': 'text'})
        self.fields['email'].widget.attrs.update({
            'label': 'Email',
            'class': 'form-control',
            'placeholder': 'email@example.com',
            'type': 'email'})
