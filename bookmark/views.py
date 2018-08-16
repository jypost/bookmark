from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# 뷰 종류는 두가지 : 함수형, 클래스형
# 아래건 함수형 뷰임
# 장고 목적? : 귀찮은거 하기 싫어서...
# 클래스형 : 자주 쓰는 기능을 상속받아서 간단하게 생성

# 장고에서 뷰 컴포넌트 불러온다
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# 모델에서 넘어옴 08
# 아래 주석들 다시만듬
# list View
from .models import Bookmark
class BookmarkListView(ListView):
    model = Bookmark
    # 클래스형 뷰는 기본적으로 렌더링할 템플릿 파일이 지정이 되어 있음
    # bookmark/bookmark_list.html


# urls로 넘어가 서 뷰이름 변경



# 이건 일단 안씀
# def list(request):
#     return HttpResponse("List Page")

from django.urls import reverse_lazy
class BookmarkCreateView(CreateView):
    model = Bookmark #입력화면에 출력된 form tag를 자동으로 만들어줌
    # _form : create, update
    #default : _form 아래 서픽스를 안쓰면 디폴트는 폼
    template_name_suffix = '_create'
    # 입력받을 필드 목록
    fields = ['site_name','url']
    # get_absolute_url
    success_url = reverse_lazy('bookmark:list')



class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'
    #동작이 완료된 후 어디로 가냐, 아래거 안쓰면 get absolute url
    # success_url = reverse_lazy('list')


class BookmarkDeleteView(DeleteView):
    model = Bookmark
    #북마크의 리스트 불러와서 메인페이지로
    success_url = reverse_lazy('bookmark:list')


class BookmarkDetailView(DetailView):
    model = Bookmark




# def write(request):
#     return HttpResponse("Write Page")
#
# def update(request):
#     return HttpResponse("Update Page")
#
# def delete(request):
#     return HttpResponse("Delete Page")