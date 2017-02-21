from django.shortcuts import render
from django.shortcuts import Http404
from django.shortcuts import get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.views import generic

from .models import Question, Choice


# for vote view
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone


# for generic view
class IndexView(generic.ListView): #list view
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        # new amend, only publish the question till now, not the future"
        return Question.objects.filter(
            pub_date__lte=timezone.now()  #pub_date_lte will cause error
        ).order_by('-pub_date')[:5]
        #return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView): #detail view and the model is the thing it will be acting upon
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(selfself):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())



class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice']) #choice is the name in the template
    except (KeyError, Choice.DoesNotExist):
        #redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You did not select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        #always return an HttpResponseRedirect
        return HttpResponseRedirect(reverse('polls:results', args=(question_id))) # return a page like polls/3/results

# we need to write results view.


# 1. first try
#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    output = ', '.join([q.question_text for q in latest_question_list])
#    return HttpResponse(output)
# 2. view with http template
#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    template = loader.get_template('polls/registry.html')
#   context = {
#       'latest_question_list': latest_question_list,
#    }
#    return HttpResponse(template.render(context, request))
# 3. with render
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# normal detail

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

#def detail(request, question_id):
#    return HttpResponse("You're looking at question %s." % question_id)

# 4. 404
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


# below two functions are the old ones does not do logical things.
#def results(request, question_id):
#    response = "You're looking at the results of question %s."
#    return HttpResponse(response % question_id)

#def vote(request, question_id):
#    return HttpResponse("You're voting on question %s." % question_id)