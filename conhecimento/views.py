from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Publicacao
from .forms import Aviso


def detalhe_python(request):
	python = Publicacao.objects.filter(tema='1')
	return render(request, 'conhecimento/python.html',{'python':python})


def lista_avisos(request, *args, **kwargs):
    tema = request.GET.get('tema', '')

    if tema != '':
        publicacao = Publicacao.objects.filter(tema__tema=tema)
    else:
        publicacao = Publicacao.objects.filter(
            data_publicacao__lte=timezone.now())

    return render(
        request,
        'conhecimento/avisos.html', {'publicacao': publicacao}
    )


def detalhe(request, pk):
    publicacao = get_object_or_404(Publicacao, pk=pk)
    return render(
        request,
        'conhecimento/detalhe.html',
        {'publicacao': publicacao})


def lista_publicacoes(request, tema):
    publicacoes = Publicacao.objects.filter(tema=tema)
    return render(
        request, 'conhecimento/python.html',
        {'publicacoes': publicacoes})


def novo(request):
    if request.method == 'POST':
        form = Aviso(request.POST)
        if form.is_valid():
            publicacao = form.save(commit=False)
            publicacao.autor = request.user
            publicacao.data_publicacao = timezone.now()
            publicacao.save()
            form.save_m2m()
            # Sem o save_m2m não salva com relacionamento ManytoMany
            return redirect('conhecimento.views.detalhe', pk=publicacao.pk)
    else:
        form = Aviso()
    return render(request, 'conhecimento/editar_aviso.html', {'form': form})


def novo_aviso(request, pk):
    publicacao = get_object_or_404(Publicacao, pk=pk)
    if request.method == "POST":
        form = Aviso(request.POST, instance=publicacao)
        if form.is_valid():
            publicacao = form.save(commit=False)
            publicacao.autor = request.user
            publicacao.data_publicacao = timezone.now()
            publicacao.save()
            form.save_m2m()
            # Sem o save_m2m não salva com relacionamento ManytoMany
            return redirect('conhecimento.views.detalhe', pk=publicacao.pk)
    else:
        form = Aviso(instance=publicacao)
    return render(request, 'conhecimento/editar_aviso.html', {'form': form})
