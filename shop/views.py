from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Product, Category, CartItem, Order, Contact
from django.http import HttpResponseRedirect

def is_admin(user):
    return user.is_staff and user.is_superuser  # Updated for superuser only

def home(request):
    products = Product.objects.all()[:6]
    categories = Category.objects.all()
    if request.user.is_authenticated and is_admin(request.user):
        return render(request, 'home_admin.html', {
            'products': products, 
            'categories': categories
        })
    return render(request, 'home.html', {
        'products': products,
        'categories': categories 
    })

def products(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    
    # Admin sees edit/delete buttons
    is_admin_user = request.user.is_authenticated and is_admin(request.user)
    
    # Search functionality
    search_query = request.GET.get('search', '').strip()
    if search_query:
        products = products.filter(name__icontains=search_query)
    
    # Category filter
    category_id = request.GET.get('category')
    if category_id:
        products = products.filter(category_id=category_id)
    
    return render(request, 'products.html', {
        'products': products,
        'categories': categories,
        'search_query': search_query,
        'selected_category': category_id,
        'is_admin_user': is_admin_user  # Pass to template
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    is_admin_user = request.user.is_authenticated and is_admin(request.user)
    return render(request, 'product_detail.html', {
        'product': product,
        'is_admin_user': is_admin_user
    })

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'home_admin.html', {
        'products': products, 
        'categories': categories
    })

@login_required
@user_passes_test(is_admin)
def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        category_id = request.POST.get('category')
        description = request.POST.get('description', '')
        stock = request.POST.get('stock', 0)
        image = request.FILES.get('image')
        
        product = Product.objects.create(
            name=name, 
            price=price, 
            category_id=category_id, 
            description=description,
            stock=stock
        )
        if image:
            product.image = image
            product.save()
            
        messages.success(request, f'{name} added successfully!')
        return redirect('admin_dashboard')  # Redirect to dashboard
    categories = Category.objects.all()
    return render(request, 'add_product.html', {'categories': categories})

@login_required
@user_passes_test(is_admin)
def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Category.objects.create(name=name)
        messages.success(request, 'Category added successfully!')
        return redirect('admin_dashboard')
    return render(request, 'add_category.html')

@login_required
@user_passes_test(is_admin)
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.category_id = request.POST.get('category')
        product.description = request.POST.get('description', '')
        product.stock = request.POST.get('stock', 0)
        image = request.FILES.get('image')
        if image:
            product.image = image
        product.save()
        messages.success(request, 'Product updated successfully!')
        return redirect('admin_dashboard')
    categories = Category.objects.all()
    return render(request, 'edit_product.html', {
        'product': product, 
        'categories': categories
    })

@login_required
@user_passes_test(is_admin)
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product_name = product.name
        product.delete()
        messages.success(request, f'{product_name} deleted successfully!')
        return redirect('admin_dashboard')
    return render(request, 'delete_product.html', {'product': product})

@login_required
@user_passes_test(is_admin)
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category_name = category.name
        category.delete()
        messages.success(request, f'{category_name} deleted successfully!')
        return redirect('admin_dashboard')
    return render(request, 'delete_category.html', {'category': category})

@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user, product=product, defaults={'quantity': 1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    messages.success(request, f'{product.name} added to cart!')
    return redirect('cart')

@login_required
def remove_from_cart(request, pk):
    cart_item = get_object_or_404(CartItem, pk=pk, user=request.user)
    cart_item.delete()
    messages.success(request, 'Item removed from cart!')
    return redirect('cart')

@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})

@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price() for item in cart_items)
    if request.method == 'POST':
        Order.objects.create(user=request.user, total=total)
        cart_items.delete()
        messages.success(request, f'Order placed successfully! Total: ₹{total}')
        return redirect('home')
    return render(request, 'checkout.html', {'cart_items': cart_items, 'total': total})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Account created for {form.cleaned_data.get("username")}! Please login.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def about(request):
    categories = Category.objects.all()
    return render(request, 'about.html', {'categories': categories})

def contact(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        Contact.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            message=request.POST.get('message')
        )
        messages.success(request, 'Message sent successfully!')
        return redirect('contact')
    return render(request, 'contact.html', {'categories': categories})
