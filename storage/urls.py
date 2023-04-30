from django.urls import path
from .views import (
    create_document,
    get_document,
    update_document,
    delete_document,
    get_document_versions,
    get_all_documents
)

urlpatterns = [
    path('', get_all_documents, name='list_documents'),
    path('document/create/', create_document, name='create_document'),
    path('document/<int:document_id>/', get_document, name='view_document'),
    path('document/<int:document_id>/update/', update_document, name='update_document'),
    path('document/<int:document_id>/delete/', delete_document, name='delete_document'),
    path('document/<int:document_id>/versions/', get_document_versions, name='compare_versions'),
]