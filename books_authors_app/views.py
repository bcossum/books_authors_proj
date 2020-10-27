from django.shortcuts import render, redirect
from .models import Books, Authors

def index(request):
  context = {
    "all_books": Books.objects.all()
  }
  return render(request, 'index.html', context)

def create_book(request):
  if request.method == 'POST':
    Books.objects.create(
      title = request.POST['title'],
      desc = request.POST['desc']
    )
  return redirect('/')

def book_view(request, book_id):
  book = Books.objects.get(id=book_id)
  context = {
    'book': book,
    'all_authors': Authors.objects.exclude(book__id=book_id),
  }
  return render(request, 'books.html', context)

def add_author(request, book_id):
  book = Books.objects.get(id=book_id)
  author = Authors.objects.get(id=request.POST['author_id'])
  book.author.add(author)
  return redirect(f'/books/{book_id}')

def author_view(request, author_id):
  author = Authors.objects.get(id=author_id)
  context = {
    'author': author,
    'all_books': Books.objects.exclude(author__id=author_id),
  }
  return render(request, 'authors.html', context)

def authors(request):
  context = {
    'all_authors': Authors.objects.all()
  }
  return render(request, 'author_page.html', context)

def create_author(request):
  if request.method == 'POST':
    Authors.objects.create(
      first_name = request.POST['first_name'],
      last_name = request.POST['last_name'],
      notes = request.POST['notes'],
    )
  return redirect('/authors')

def add_book(request, author_id):
  author = Authors.objects.get(id=author_id)
  book = Books.objects.get(id=request.POST['book_id'])
  author.book.add(book)
  return redirect(f'/authors/{author_id}')