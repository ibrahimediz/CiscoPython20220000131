from django.shortcuts import render,get_object_or_404,redirect
from .models import BlogModel
from .forms import BlogForm

def blgliste(request):
    bloglar = BlogModel.objects.all()
    return render(request, 'blog/bloglist.html',{"bloglar":bloglar})

def blgdetay(request,id):
    # blog = BlogModel.objects.get(id=id)
    blog = get_object_or_404(BlogModel,id=id)
    return render(request, 'blog/blogdetay.html',{"blog":blog})

# def blgyeni(request):
#     form = BlogForm()
#     return render(request, 'blog/blogyeni.html',{"form":form})

def blgyeni(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.yayinla()
            return redirect('bloglist')
    else:
        form = BlogForm()
    return render(request, 'blog/blogyeni.html',{"form":form})


def blgduzenle(request,id):
    blog = get_object_or_404(BlogModel,id=id)
    if request.method == "POST":
        form = BlogForm(request.POST,instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.yayinla()
            return redirect('bloglist')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/blogyeni.html',{"form":form})

