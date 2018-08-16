from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# View 는 2종류가 있다. Function View 와 Class View
# 장고 목적: python 으로 web 구현하기 귀찮으니깐 편하게
# class 형: 자주 쓰는 기능을 상속받아서 간단하게 생성 -> 자주 사용한다.

# 오늘 하는 일은 기본 구현되어있는 View 들을 상속받아 사용
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

"""
def list(request):
    return HttpResponse('List Page')
"""
# ListView 상속
from .models import Bookmark

class BookmarkListView(ListView):
    model = Bookmark # Bookmark model 을 가져옴
    # 클래스형 View는 기본적으로 렌더링할 템플릿 파일이 지정이 되어있다.
    # bookmark/bookmark_list.html

"""
def write(request):
    return HttpResponse('Write Page')
"""
from django.urls import reverse_lazy
class BookmarkCreateView(CreateView):
    model = Bookmark # 입력화면에 출력된 form tag를 자동으로 만들어줌
    # _form : create , update
    # 원래 template 의 이름이 _form 인데 _create 로 변경
    template_name_suffix = '_create'
    # 입력받을 필드 목록
    fields = ['site_name', 'url']
    # success_url 이 없으면 model 에 get_absolute_url 이 실행
    success_url = reverse_lazy('list')


"""
def update(request):
    return HttpResponse('List Page')
"""
class BookmarkUpdateView(UpdateView):
    model = Bookmark
    template_name_suffix='_update'
    fields=['site_name', 'url']

"""
def delete(request):
    return HttpResponse('List Page')
"""
class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:list')

class BookmarkDetailView(DetailView):
    model = Bookmark
