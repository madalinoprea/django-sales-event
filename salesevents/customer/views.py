# Create your views here.
from forms import SignupRequestForm
from mario.utils import render_to

@render_to('signup_request.html')
def signup_request_view(request):
    if request.method == 'POST':
        form = SignupRequestForm(request.POST)
        if form.is_valid():
            # Process data
            form.save()
    else:
        form = SignupRequestForm()

    return {'form': form}

@render_to('singup_thanks.html')
def signup_thanks_view(request):
    return {}