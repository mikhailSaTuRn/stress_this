from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
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


def index(request):
    # ствараю слоўнік са складамі
    work_dict = take_random_word()
    syllable_list = work_dict['word'].split('_')
    context = {'syllable_list': syllable_list, 'work_dict': work_dict}

    return render(request, "index.html", context)


def article(request, id):
    curr_word_data = get_object_or_404(Words, id=id)
    word_data = {'word': curr_word_data.word,
                 'stress_idx': curr_word_data.stress_idx,
                 'stress_extra_idx': curr_word_data.stress_extra_idx,
                 'example': curr_word_data.example,
                 'article': curr_word_data.article,
                 }

    return render(request, 'article.html', word_data)


def result(request):
    id = request.GET['id']
    stress = request.GET['stress']
    curr_word_data = get_object_or_404(Words, id=id)
    flag = True
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
    return render(request, "result.html", word_data)


def add_word(request):
    # word = request.POST['word']
    # stress_idx = request.POST['stress_idx']
    # example = request.POST['example']
    # article = request.POST['article']
    # words = Words(word=word, stress_idx=stress_idx, example=example, article=article)
    # words.save()
    return redirect('add_page?r=success')


def add_new_word(request):
    text1 = request.GET['r']
    return render(request, "add_word.html", {'text1': text1})
