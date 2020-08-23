from django.forms import widgets
from django import forms


class UserForm(forms.Form):
    username = forms.CharField(min_length=4, label='用户名',
                               error_messages={"required": "该字段不能为空"},
                               widget=widgets.TextInput(
                                   attrs={'class': 'form-control'})
                               )  # 必须用要提示错误信息的关键词
    password = forms.CharField(min_length=8, label='密码',
                               widget=widgets.PasswordInput(
                                   attrs={'class': 'form-control'}),
                               error_messages={
                                   "required": "密码需要至少需要8位"
                               })
