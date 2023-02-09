from django.views.generic import ListView
from django.shortcuts import render
from .models import Post
# Create your views here.

# fbv 형식으로 만든 목록 페이지
# def index(request):
#     posts = Post.objects.all().order_by('-pk')

#     return render(request, 
#     'blog/index.html',
#     {

#         'posts':posts,
#         #데이터베이스와 연결된 인자.
#     }
#     )

# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)

#     return render(request,
#         'blog/single_post_page.html',
#         {
#             'post':post,
#         }
#     )


#cbv형식으로 만들기
class PostList(ListView):
    model = Post
    ordering = '-pk'
    # template_name = 'blog/index.html'
    # 템플릿 명을 명시하지 않으면 post_list로 템플릿을 인식한다.