from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import PostModel
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
class ListClass(ListView):
    template_name = 'list.html'
    model = PostModel

class FormClass(CreateView):
    template_name = 'form.html'
    model = PostModel
    fields = ('title','memo','image')
    success_url = reverse_lazy('formapp:list')

from django.shortcuts import get_object_or_404, render, redirect

def delete_form(request, post_id):
    post = get_object_or_404(PostModel, id=post_id)
    
    if request.method == 'POST':
        post.delete()
        # 削除後にリダイレクト
        return redirect('formapp:list')  # 'formapp:list' は URL 名
    # 確認画面を表示
    return render(request, 'delete.html', {'post': post})



