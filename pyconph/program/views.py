from django.shortcuts import redirect, render

from pyconph.program.forms import ProposalForm


def cfp(request):
    if request.user.is_authenticated and request.method == 'POST':
        form = ProposalForm(request.POST)
        if form.is_valid():
            proposal = form.save(commit=False)
            proposal.speaker = request.user
            proposal.save()
            return redirect('/cfp/thanks')
    else:
        form = ProposalForm()
    return render(request, 'program/cfp.html', {'form': form})


def cfp_thanks(request):
    return render(request, 'program/cfp_thanks.html')
