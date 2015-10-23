from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.utils import timezone
from .models import Postear
from .forms import PostForm
from django.shortcuts import redirect

def listar_publicaciones(request):
    publicaciones=Postear.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render (request,'blog/listar_publicaciones.html',{'publicaciones':publicaciones})

def detalle_publicar (request,pk):
    publicacion=get_object_or_404(Postear,pk=pk)
    return render(request,'blog/detalle_publicaciones.html',{'publicacion':publicacion})

def postear_nuevo(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('blog.views.detalle_publicar', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/edicion_publicaciones.html', {'form': form})

def editar_post(request, pk):
    post = get_object_or_404(Postear, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('blog.views.detalle_publicar', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edicion_publicaciones.html', {'form': form})
