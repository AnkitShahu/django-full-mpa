from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, "bindex.html", context)

def post_detail(request, slug):
    post = get_object_or_404(Post,
    slug=slug )
    return render(request, 'bdetails.html', {'post': post})
    