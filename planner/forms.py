from django import forms
from django.forms import ModelForm
from .models import User, Post, Trip, Comment
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from django.contrib.admin.widgets import AdminDateWidget

class TripForm(ModelForm):
    class Meta:
        model = Trip
        #fields = "__all__"
        fields = ["destination", "purpose", "departure", "arrival"]
        labels = {
            'arrival': 'Return'
        }
        widgets = {
            'destination': forms.TextInput(attrs={"size": 10, 'class': 'form-control', 'placeholder': 'City', 'id':"cityInput"}),
            #'departure': AdminDateWidget,
            #'arrival' : AdminDateWidget,
           # 'departure': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            #'arrival': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'date': AdminDateWidget()}),
            'departure': AdminDateWidget(attrs={'id': 'departure-date'}),
            'arrival': AdminDateWidget(attrs={'id': 'arrival-date'}),
            'purpose': forms.TextInput(attrs={"size": 3, 'class': 'form-control', 'id':"reason", 'placeholder': 'Reasons...'}),
        }

class PostForm(ModelForm):
    class Meta:
        model= Post
        fields = ["title","location", "photo", "tags", "body"]
        labels = {
            'location': 'City'
        }
        widgets = {
            'title': forms.TextInput(attrs={"size": 10, 'class': 'form-control', 'placeholder': 'Title', 'id':"post-title"}),
            'location': forms.TextInput(attrs={"size": 10, 'class': 'form-control', 'placeholder': 'Location', 'id':"post-location"}),
            'body': forms.Textarea(attrs={"cols": 80, "rows": 20, 'class': 'form-control',  'id':"post-body"}),
            'photo': forms.FileInput(attrs ={'class': 'form-control', 'id':"post-image"}),
            'tags': forms.TextInput(attrs={"size": 10, 'class': 'form-control', 'placeholder': 'list your tags here', 'id':"post-tags"}),
            
        }

class ProfileForm(ModelForm):
     class Meta:
        model= User
        fields =  ['first_name', 'last_name', 'about', 'photo']
        
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'about': 'About',
            'photo': 'Profile Photo',
        }
      
        widgets = {
            'first_name': forms.TextInput(attrs={"size": 10, 'class': 'form-control', 'placeholder': 'Title', 'id':"firstName-input"}),
            'last_name': forms.TextInput(attrs={"size": 10, 'class': 'form-control', 'placeholder': 'Location', 'id':"lastName-input"}),
            'about': forms.Textarea(attrs={"cols": 80, "rows": 20, 'class': 'form-control',  'id':"about-input"}),
            'photo': forms.FileInput(attrs ={'class': 'form-control', 'id':"image-input"}),
            
            
        }

class CommentForm(ModelForm):
     hidden = forms.CharField(widget=forms.HiddenInput(), required=False)
     class Meta:
        model= Comment
        fields =  ['content']
      
        widgets = {
            'content': forms.Textarea(attrs={"cols": 40, "rows": 4, 'class': 'form-control',  'id':"content-input"}),
            
        }

      