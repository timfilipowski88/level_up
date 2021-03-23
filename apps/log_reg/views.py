from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import RegisterForm, LogForm
from django.template.context_processors import csrf
from crispy_forms.utils import render_crispy_form
from django.core.exceptions import ValidationError

# Create your views here.
def index(request):
    reg_form = RegisterForm()
    log_form = LogForm()
    context = { 
        "reg_form": reg_form,
        "log_form": log_form,
        }
    return render(request, 'index.html', context)

def register(request):
    if request.method == 'POST':
        bound_form = RegisterForm(request.POST)
        if bound_form.is_valid():
            user = bound_form.save(commit=False)
            user.clean()
            user.save()
            request.session['user'] = user 
            return render(render, "main:index")          
        else:
            context = {
                'reg_form': bound_form,
                'log_form': LogForm()
            }
            return render(request, 'index.html', context)
    else:
        return redirect('login_register:index')




            # if ValidationError:
            #     for k, v in ValidationError.items():
            #         messages.error(request, v)
            #     return redirect('/')






        # form = RegisterForm(request.POST)
        # # if form['password'] == form['confirm_password']:
        # if form.is_valid():
        #         form.save()
        #         return redirect('main:index')
        # else:
        #     return redirect('/')










    # return HttpResponse('it worked')
    # if request.method == 'POST' and request.is_ajax():
    #     form = RegisterForm(request.POST)
    #     resp = {}
    #     if form.is_valid():
    #         form.save()
    #         resp['success'] = True
    #     else:
    #         resp['success'] = False
    #         csrf_context = {}
    #         csrf_context.update(csrf(request))
    #         index_html = render_crispy_form(form, context=csrf_context) 
    #         resp['html'] = index_html
    #     return redirect(request, 'main/index.html')
    # else:
    #     return redirect('/')
