from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404, get_list_or_404, redirect
from django.urls import reverse, reverse_lazy
from .models import Destino, List, Evento, PreferenciaTipo, Preferencia, Categoria
from django.views import generic, View
from .forms import DestinoForm, ReviewRoteiroForm, RoteiroForm, PreferenciaTipoForm, PreferenciaForm, EventoForm, CategoriaForm
from django.contrib.auth.decorators import login_required,permission_required,user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin,  UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import AtracaoCaracteristica
from .forms import AtracaoCaracteristicaForm

def detail_destino(request, destino_id):
    destino = get_object_or_404(Destino, pk=destino_id)
    context = {"destino": destino}
    return render(request, "destinos/detail.html", context)


class DestinoListView(generic.ListView):
    model = Destino
    template_name = 'destinos/index.html'

def search_destinos(request):
    context = {}
    if request.GET.get("query", False):
        search_term = request.GET["query"].lower()
        destino_list = Destino.objects.filter(name__icontains=search_term)
        context = {"destino_list": destino_list}
    return render(request, "destinos/search.html", context)


@login_required
@permission_required('destinos.add_destino')
def create_destino(request):
    if request.method == 'POST':
        form = DestinoForm(request.POST)
        if form.is_valid():
            destino = form.save()
            return HttpResponseRedirect(reverse('destinos:detail', args=(destino.id,)))
    else:
        form = DestinoForm()

    context = {'form': form}
    return render(request, 'destinos/create.html', context)

class CreateCategoriaView(UserPassesTestMixin, View):
    template_name = 'destinos/createCategoria.html'  
    form_class = CategoriaForm  

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'You are not authorized to create a category.')
        return redirect('destinos:index')  

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('destinos:listCategorias')  

        return render(request, self.template_name, {'form': form})
    
class listCategorias(generic.ListView):
    model = Categoria
    template_name = 'destinos/listCategorias.html'

class deleteCategoriaView(LoginRequiredMixin, generic.DeleteView):
    model = Categoria
    template_name = 'destinos/deleteCategoria.html'
    success_url = '/'

    def test_func(self):
        return self.request.user.is_staff
    
    def handle_no_permission(self):
        messages.error(self.request, 'You are not authorized to delete a category.')
        return redirect('posts:index')

class ListListView(generic.ListView):
    model = List
    template_name = 'destinos/lists.html'


class ListCreateView(LoginRequiredMixin, generic.CreateView):
    model = List
    template_name = 'destinos/create_roteiro.html'
    form_class = RoteiroForm

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('destinos:lists')

@login_required
def create_review(request, roteiro_id):
    roteiro = get_object_or_404(Destino, pk=roteiro_id)
    if request.method == 'POST':
        form = ReviewRoteiroForm(request.POST)
        if form.is_valid():
            review_author = request.user 
            review_text = form.cleaned_data['text']
            roteiro.review_set.create(author=review_author, text=review_text)
            return HttpResponseRedirect(
                reverse('destinos:roteiro',args=(roteiro_id,)))
    else:
        form = ReviewRoteiroForm()
        context = {'form': form, 'roteiro': roteiro}
    return render(request, 'destinos/review.html',context)

def RoteiroDetailView(request, pk):
     # Obtém a lista específica
    lista = List.objects.get(pk=pk)

    # Obtém os destino_id associados a essa lista
    destino_ids = List.objects.filter(pk=pk).values_list('atracoes', flat=True)

    # Obtém os destinos associados a esses destino_ids
    destinos = Destino.objects.filter(pk__in=destino_ids)

    return render(request, 'destinos/roteiro.html', {'destino_list': destinos})

class update_Roteiro(LoginRequiredMixin, generic.UpdateView):
    model = List
    template_name = 'destinos/update.html'
    fields = ['nome', 'Capa', 'descricao']
    success_url = reverse_lazy('destinos:lists')


class delete_Roteiro(LoginRequiredMixin, generic.DeleteView):
    model = List
    success_url = "/"
    template_name = "destinos/delete_roteiro.html"

@login_required
def listar_preferencias_tipo(request):
    preferencias = PreferenciaTipo.objects.all()  # Busca todas as preferências

    return render(request, 'destinos/listar_preferencias_tipo.html', {'preferencias': preferencias})

def is_admin(user):
    return user.is_authenticated and user.is_staff

@login_required
@user_passes_test(is_admin)
def add_preferencias_tipo(request):
    if request.method == 'POST':
        form = PreferenciaTipoForm(request.POST)
        if form.is_valid():
            novo_tipo_preferencia = form.save()
            form = PreferenciaTipoForm()
    else:
        form = PreferenciaTipoForm()

    return render(request, 'destinos/add_preferencias_tipo.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def delete_preferencias_tipo(request):
    if request.method == 'POST':
        tipo_preferencia = request.POST.get('tipo_preferencia')  # Obtém o tipo de preferência a ser excluído
        preferencias = PreferenciaTipo.objects.filter(nome=tipo_preferencia)
        if preferencias.exists():
            preferencias.delete()  # Exclui as preferências encontradas
        # Renderize novamente a página atual após a exclusão
        preferencias_atualizadas = PreferenciaTipo.objects.all()  # Obtém todas as preferências atualizadas
        return render(request, 'destinos/listar_preferencias_tipo.html', {'preferencias': preferencias_atualizadas})

    # Se houver um erro ou ação inválida, renderize a página novamente
    preferencias = PreferenciaTipo.objects.all()  # Obtém todas as preferências
    return render(request, 'destinos/listar_preferencias_tipo.html', {'preferencias': preferencias})

@login_required
def meu_perfil(request):
    preferencias_usuario = Preferencia.objects.filter(usuario=request.user)

    if request.method == 'POST':
        form = PreferenciaForm(request.POST)
        if form.is_valid():
            preferencia = form.save(commit=False)
            preferencia.usuario = request.user
            preferencia.save()
    else:
        form = PreferenciaForm()

    preferencias_disponiveis = PreferenciaTipo.objects.all()

    return render(request, 'destinos/meu_perfil.html', {
        'form': form,
        'preferencias_disponiveis': preferencias_disponiveis,
        'preferencias_usuario': preferencias_usuario
    })

@login_required
def remover_preferencia(request, preferencia_id):
    preferencia = get_object_or_404(Preferencia, pk=preferencia_id, usuario=request.user)
    
    if request.method == 'POST':
        preferencia.delete()
        return redirect('destinos:meu_perfil')
    
    return render(request, 'destinos/remover_preferencia.html', {'preferencia': preferencia})

class CreateEventoView(UserPassesTestMixin, View):
    form_class = EventoForm
    template_name = 'destinos/adicionarEvento.html'

    def test_func(self):
        roteiro = List.objects.get(pk=self.kwargs['pk'])
        return self.request.user.is_staff or roteiro.autor == self.request.user

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            roteiro = List.objects.get(pk=self.kwargs['pk'])
            form.instance.roteiro_id = roteiro
            form.save()
            return redirect('destinos:roteiro', pk=roteiro.pk)
        return render(request, self.template_name, {'form': form})

@login_required
def add_atracao_caracteristica(request,pk):
    caracteristicas_da_atracao = AtracaoCaracteristica.objects.filter(atracao=pk)

    if request.method == 'POST':
        form = AtracaoCaracteristicaForm(request.POST)
        if form.is_valid():
            caracteristicas_da_atracao = form.save(commit=False)
            caracteristicas_da_atracao.atracao = pk
            caracteristicas_da_atracao.save()
    else:
        form = AtracaoCaracteristicaForm()

    caracteristicas_disponiveis  = PreferenciaTipo.objects.all()

    return render(request, 'destinos/add_atracao_caracteristica.html', {
        'form': form,
        'caracteristicas_disponiveis ': caracteristicas_disponiveis ,
        'caracteristicas_da_atracao':caracteristicas_da_atracao
    })

@login_required
def remover_atracao_caracteristica(request, caracteristica_id):
    caracteristica = get_object_or_404(AtracaoCaracteristica, pk=caracteristica_id)
    
    if request.method == 'POST':
        caracteristica.delete()
        return redirect('destinos:listar_atracao_caracteristicas')
    
    return render(request, 'destinos/remover_atracao_caracteristica.html', {'caracteristica': caracteristica})