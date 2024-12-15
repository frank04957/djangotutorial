from .models import Note
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,  get_object_or_404,  redirect


def index(request):
    notes = Note.objects.all()
    return render(request, 'note/index.html', {'notes': notes})


def detail(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    return render(request, 'note/detail.html', {'note': note})

@csrf_exempt
def add_note(request):
    if request.method == "POST":
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()

        if title and content:
            Note.objects.create(title=title, content=content)
            return redirect('/')
        
        return render(request, 'note/add_note.html', {'error': 'Title and Content are required'})

    return render(request, 'note/add_note.html')
