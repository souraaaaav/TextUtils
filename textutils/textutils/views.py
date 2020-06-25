#i have created this file-sourav
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def analyze(request):
    # get the text
    djtext=request.POST.get('text','deafult')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    spaceremover=request.POST.get('spaceremover','off')
    charcount=request.POST.get('charcount','off')
    if charcount == 'on':
        dictionary = {'purpose': 'Character Count', 'analyzed_text': (len(djtext)-djtext.count(' '))}
        return render(request, 'analyze.html', dictionary)

    else:
        if removepunc == 'on':
            punctuations=''''?<><#$%^&*()_+.":;'''
            analyzed=""
            for char in djtext:
                if char not in punctuations:
                    analyzed=analyzed+char

            dictionary={'purpose':'remove punctuations','analyzed_text':analyzed}
            djtext=analyzed

        if fullcaps=='on':
            analyzed=''
            for char in djtext:
                analyzed=analyzed+char.upper()
            dictionary = {'purpose': 'capitalize letter', 'analyzed_text': analyzed}
            djtext=analyzed
        if newlineremover=='on':
            analyzed=''
            for char in djtext:
                if char != '\n' and char!= '\r':
                    analyzed=analyzed+char
            dictionary={'purpose':'Remove New Line','analyzed_text':analyzed}
            djtext=analyzed
        if spaceremover=='on':
            analyzed=''
            for index,char in enumerate(djtext):
                if not(djtext[index]==' ' and djtext[index+1]==' '):
                    analyzed=analyzed+char
            dictionary={'purpose':'Extra Space Remover','analyzed_text':analyzed}
            djtext=analyzed

        if(removepunc!='on' and fullcaps!='on' and newlineremover!='on' and spaceremover!='on'):
            return HttpResponse("ERROR")


        return render(request,'analyze.html',dictionary)




