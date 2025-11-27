from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Grievance
from .forms import GrievanceForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# ---1. READ (List View)----
def grievance_list(request):
    posts_list = Grievance.objects.all().order_by('-created_at')  #Sabhi posts layega
    query = request.GET.get('q')
    if query:
        posts_list = posts_list.filter(title__icontains=query)
    paginator = Paginator(posts_list, 4)  # Show only 3 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'grievance/grievance_list.html', {'page_obj': page_obj, 'posts': page_obj.object_list, 'query': query})

# --- 2. READ (Detail View) ---
def grievance_detail(request, pk):
    post = get_object_or_404(Grievance, pk=pk)
    return render(request, 'grievance/grievance_detail.html', {'post':post})

# --- 3. CREATE (Naya Post) ---
@login_required # Sirf logged-in user hi post bna skta hai
def grievance_create(request):
    if request.method == 'POST':  #'POST' method isliye use kr rhe hai kyuki user apni details bhj rhai hai for create a post
        form = GrievanceForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # Current user ko author banao
            post.save()
            return redirect('grievance_list')
    else:
        form = GrievanceForm()
    return render(request, 'grievance/grievance_form.html', {'form':form})

# --- 4. UPDATE (Edit Post) ---
@login_required
def grievance_edit(request, pk):
    post = get_object_or_404(Grievance, pk=pk)
    if request.method == "POST":
        form = GrievanceForm(request.POST, request.FILES, instance=post)  # include request.FILES to handle uploaded files
        if form.is_valid():
            form.save()
            return redirect('grievance_detail', pk=post.pk)
    else:
            form = GrievanceForm(instance=post)
    return render(request, 'grievance/grievance_form.html', {'form':form})
    
# --- 5. DELETE (Delete Post)---
@login_required
def grievance_delete(request, pk):
    post = get_object_or_404(Grievance, pk=pk)
    post.delete()
    return redirect('grievance_list')

# --- 6. SIGNUP (Register) ---
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})

        


