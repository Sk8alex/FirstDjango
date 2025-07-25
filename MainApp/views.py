from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

# def home(request):
#     text ="""
#     <h1>"Изучаем django"</h1>
#     <strong>Автор</strong>: <i>Иванов И.П.</i>
#     """
#     return HttpResponse(text)

def home(request) -> HttpResponse:
    context = {
        "name": "Иванов Иван Иванович",
        "email": "mail@mail.ru"
    }
    return render(request, "index.html", context)
"""
    author = {
        "Имя": "Иван",
        "Отчество": "Петрович",
        "Фамилия": "Иванов",
        "телефон": "8-923-600-01-02",
        "email": "vasya@mail.ru",
    }
"""

# author = {
#     "name": "Иван",
#     "middle_name": "Петрович",
#     "last_name": "Иванов",
#     "phone": "8-923-600-01-02",
#     "email": "vasya@mail.ru",
# }

def about(request):
    author = {
        "name": "Иван",
        "middle_name": "Петрович",
        "last_name": "Иванов",
        "phone": "8-923-600-01-02",
        "email": "vasya@mail.ru",
    }
    context = {
        'author': author
    }
    return render(request, "about.html", context)



items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]


def get_item(request, item_id: int):
    """ По указанному id возвращает элемент из списка"""
    for item in items:
        if item["id"] == item_id:
            context = {
                "item": item
            }
            return render(request, "item_page.html", context)
    #return HttpResponseNotFound(f'Item with id={item_id} not found')
    # return render(request, "error_prod_found.html", {"error": f'Item with id={item_id} not found'})
    return render(request, "errors.html", {"errors": [f'Item with id={item_id} not found']})


# def get_item(request, item_id: int):
#     """ По указанному id возвращает элемент из списка"""
#     for item in items:
#         if item["id"] == item_id:
#             result = f"""
#             <h2> Имя: {item["name"]} </h2>
#             <p> Количество: {item["quantity"]} </p>
#             <p> <a href='/items'> Назад к списку товаров </a></p>
#             """
        
#             return HttpResponse(result)
        
#     return HttpResponseNotFound(f'Item with id={item_id} not found')   
        
def get_items(request):
    context = {
        "items": items 
        }
    return render(request, "items_list.html", context)


# Проверка урла
# def get_item(request, item_id: int):
#     return HttpResponseNotFound(item_id)