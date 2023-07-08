from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import Answers_form,Post_form
from .models import Post,Answers
from django.shortcuts import get_object_or_404

# Create your views here.


def index(request):
    all_posts = Post.objects.all().order_by('-created_at')
    return render(request, 'index.html', { 'all_posts': all_posts })

def base(request):
    return render(request,'base.html')

@login_required(login_url="/login/")
def addpost(request):
    form = Post_form()
    if request.method == 'POST':
        form = Post_form(request.POST, request.FILES)
        if form.is_valid():
            question = form.save(commit=False)  
            question.author = request.user
            question.save() 
            return redirect('blog:index')
    else:
        all_posts = Post.objects.all().order_by('created_at')
        return render(request, 'addpost.html', {'form': form, 'all_posts': all_posts})




@login_required(login_url="/login/")
def see_posts(request):
    all_posts = Post.objects.all().order_by('created_at')
    return render(request, 'index.html', {'all_posts': all_posts})

@login_required(login_url="/login/")
def detail(request, slug):
    question = Post.objects.get(slug=slug)
    answers = Answers.objects.filter(question=question).order_by('-updated_at')
    answer_form = Answers_form()

    if request.method == 'POST':
        answer_data = Answers_form(request.POST)
        if answer_data.is_valid():
            answer = answer_data.save(commit=False)
            answer.question = question
            answer.user = request.user
            answer.save()
            return redirect('blog:detail', slug=slug)

    return render(request, 'detail.html', {
        'question': question,
        'answers': answers,
        'answer_form': answer_form,
    })

@login_required(login_url="/login/")
def delete_item(request, model, pk):
    if model == 'question':
        item = Post.objects.get(pk=pk)
        answers = Answers.objects.filter(question=item)
        if request.method == 'POST' and request.user == item.author:
            answers.delete()
            item.delete()
            return redirect('blog:index')
    elif model == 'answer':
        item = Answers.objects.get(pk=pk)
        if request.method == 'POST' and request.user == item.user:
            item.delete()
            return redirect('blog:detail', slug=item.question.slug)
    
    # Handle invalid model parameter or unauthorized access (optional)
    return redirect('blog:index')


@login_required(login_url="/login/")
def update(request, slug):
    question = Post.objects.get(slug=slug)
    form = Post_form(instance=question)
    
    if request.method == 'POST':
        form = Post_form(request.POST, request.FILES, instance=question)
        if form.is_valid():
            form.save()
            return redirect('blog:detail', slug=slug)
    
    return render(request, 'detail.html', {
        'form': form,
        'question': question,
    })
