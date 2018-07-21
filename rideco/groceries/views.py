from django.shortcuts import render
from .models import Lists, Items
from django.views.generic.base import TemplateView
from django.views import generic
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
import json


def index(request):
    grocery_lists = Lists.objects.order_by('-pub_date')
    template = loader.get_template('groceries/index.html')
    context = {
        'grocery_lists': grocery_lists,
    }
    return HttpResponse(template.render(context, request))

class createView(TemplateView):
    template_name = 'groceries/create.html'


class listView(generic.DetailView):
    template_name = 'groceries/list.html'
    model = Lists

    def get_context_data(self, *, object_list=None, **kwargs):
        list = Lists.objects.filter(pk=self.kwargs['pk']).values('list_name', 'pub_date').first()
        context = super(listView, self).get_context_data(**kwargs)
        context['list_items'] = Items.objects.filter(list_id=self.kwargs['pk']).all().order_by('item_name')
        return context


@csrf_exempt
def createList(request):
    if request.is_ajax():
        body_string = request.body.decode('utf8').replace("'", '"')
        obj = json.loads(body_string)
        title = obj['title']
        created_at = datetime.datetime.now()

        grocery_list = Lists(list_name=title, pub_date=created_at)
        grocery_list.save()

        grocery_list_items = obj['grocery_list']
        for grocery_item in grocery_list_items:
            item = Items(list_id=grocery_list.id, item_name=grocery_item['item_name'], quantity=grocery_item['item_quantity'])
            item.save()

        result = {'response': 'success'}

    return JsonResponse(result)


@csrf_exempt
def updateList(request):
    if request.is_ajax():
        body_string = request.body.decode('utf8').replace("'", '"')
        obj = json.loads(body_string)

        grocery_list_items = obj['grocery_list']
        for grocery_item in grocery_list_items:
            item = Items.objects.filter(pk=grocery_item['item_id']).first()
            item.item_name = grocery_item['item_name']
            item.quantity = grocery_item['item_quantity']
            item.save()

        result = {'response': 'success'}

    return JsonResponse(result)