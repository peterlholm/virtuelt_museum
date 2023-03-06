"backoffice views"
from django.shortcuts import render
from .models import MuseumTopic
from .forms import TopicForm

def index(request):               # pylint: disable=unused-variable
    "Start side"
    return render(request, 'index.html')

def topic(request):
    "page with museum topic"

    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("fejl i form", form.errors)
    else:
        form = TopicForm()

    mycontext = { 'form': form }
    return render(request, 'topic.html', context=mycontext)

def list_topics(request):
    "List and edit topics"
    topic_list = list(MuseumTopic.objects.all().order_by('TopicNo').values())
    mycontext = {'topiclist': topic_list }
    return render(request, 'list_topics.html', context = mycontext)

def sign(request):
    "Udstillings skilt"

    mytopic = MuseumTopic.objects.get(pk=1)
    #form = TopicForm(instance=mytopic)

    #print(form)
    #print(mytopic.id)
    #print(mytopic.Titel)
    mycontext = {'titel': mytopic.Titel, "manuctaturer": mytopic.Manufacturer, 'factuals': mytopic.Factual_text, 'description': mytopic.Description}
    #print (mycontext)
    return render(request, 'sign.html', context=mycontext)
