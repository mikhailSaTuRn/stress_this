from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from StressThis.models import Words
import random


def take_random_word():
    number_of_words = len(Words.objects.all())
    show_id = random.randint(1, number_of_words)
    curr_word_data = Words.objects.filter(id=show_id)[0]
    word_data = {'word': curr_word_data.word,
                 'stress_idx': curr_word_data.stress_idx,
                 'stress_extra_idx': curr_word_data.stress_extra_idx,
                 'id': curr_word_data.id,
                }
    return word_data


def take_a_quiz():
    work_dict = take_random_word()
    syllable_list = work_dict['word'].split('_')
    context = {'syllable_list': syllable_list, 'work_dict': work_dict}

    return context


def base_page():
    menu_context = {'menu': [
        {'title': 'main_page', 'link': '/'},
        {'title': 'all words', 'link': '/articles'},
        {'title': 'add new word', 'link': '/add_page?r=None'},
               ]}
    return menu_context

def index(request):
    # ствараю слоўнік са складамі
    context = take_a_quiz()
    context['menu_context'] = base_page()
    return render(request, "index.html", context)


def article(request, id):
    curr_word_data = get_object_or_404(Words, id=id)
    word_data = {'word': curr_word_data.word,
                 'stress_idx': curr_word_data.stress_idx,
                 'stress_extra_idx': curr_word_data.stress_extra_idx,
                 'example': curr_word_data.example,
                 'article': curr_word_data.article,
                 }

    context = take_a_quiz()
    context['word_data'] = word_data
    context['menu_context'] = base_page()
    return render(request, 'article.html', context)


def result(request):
    id = request.GET['id']
    stress = request.GET['stress']
    curr_word_data = get_object_or_404(Words, id=id)
    if int(stress) == int(curr_word_data.stress_idx):
        flag = True
    else:
        flag = False
    word_data = {'word': curr_word_data.word,
                 'stress_idx': curr_word_data.stress_idx,
                 'stress_extra_idx': curr_word_data.stress_extra_idx,
                 'example': curr_word_data.example,
                 'article': curr_word_data.article,
                 'flag': flag,
                 }

    context = take_a_quiz()
    context['word_data'] = word_data
    context['menu_context'] = base_page()
    return render(request, "result.html", context)


def add_word(request):
    word = request.POST['word']
    stress_idx = request.POST['stress_idx']
    example = request.POST['example']
    article = request.POST['article']
    words = Words(word=word, stress_idx=stress_idx, example=example, article=article)
    words.save()
    return HttpResponseRedirect('add_page?r=success')


def add_new_word(request):
    status = request.GET['r']
    return render(request, "add_word.html", {'status': status})
