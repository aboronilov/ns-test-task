# Тестовое задание на должность Python разработчика 
 
✅Тестовое задание: 

Реализовать приложение - хранение документов. 
БД можно использовать sqlite 
Документы имеют атрибута - id, наименование и содержание 
При их редактировании необходимо вести историю версий или помечать как удалённые. 
Реализовать сравнение всех документов с их текущей и самой последней версией. 
Использовать фреймворки flask или django, обязательно использовать ORM и html шаблонизатор. 
С решением так же отправлять демо БД. 

## Технололгии

### Backend
* [Django](https://www.djangoproject.com/)

### Frontend
* [Django-tailwind](https://django-tailwind.readthedocs.io/en/latest)

## Приложение развернуто [здесь](https://nsign-test-task.onrender.com/) 

## Функционал

1. Основная страница с Navbar (также доступен на остальных стрницах). При нажатии на левый логотип произойдет переход на основную страницу
    
![Landing page](https://github.com/aboronilov/ns-test-task/blob/main/theme/static/images/list.png)

2. Кнопка *Создать документ* активна. При её нажатии откроется соотвествующая форма

![Landing page](https://github.com/aboronilov/ns-test-task/blob/main/theme/static/images/create.png)

3. При нажатии на конкретный документ откроется его страница. Кнопка *Удалить* - динамическая, она меняется в зависимости от статуса записи в БД и отрабатывает для каждого случая свой функционал.

![Landing page](https://github.com/aboronilov/ns-test-task/blob/main/theme/static/images/document-deleted.png)

![Landing page](https://github.com/aboronilov/ns-test-task/blob/main/theme/static/images/document.png)

4. Кнопка *Изменить* открывает форму с редактированием записи

![Landing page](https://github.com/aboronilov/ns-test-task/blob/main/theme/static/images/update-document.png)

5. Кнопка *Версии* открывает страницу со сравнением актуальной версии и предыдущей

![Landing page](https://github.com/aboronilov/estate/blob/main/client/src/assets/screenshots/1.png)





