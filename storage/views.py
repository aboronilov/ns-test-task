from django.shortcuts import get_object_or_404, redirect, render
from django.core.exceptions import ValidationError

from .models import Document, DocumentVersion
from .forms import CreateDocumentForm, UpdateDocumentForm

def create_document(request, *args, **kwargs):
    if request.method == "POST":
        form = CreateDocumentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_documents")
    else:
        form = CreateDocumentForm()
        
    context = {
        "form": form
    }
    
    return render(request, 'storage/create_document.html', context=context)

def get_all_documents(request, *args, **kwargs):
    documents = Document.objects.all()
    context = {
        "documents": documents
    }
    return render(request, "storage/list_documents.html", context=context)


def get_document(request, *args, **kwargs):
    document_id = kwargs.get("document_id")

    if not document_id:
        raise ValidationError("Document id should be provided")
    
    document = get_object_or_404(Document, id=document_id)
    context = {
        "document": document
    }
    return render(request, 'storage/view_document.html', context=context)

def update_document(request, *args, **kwargs):
    document_id = kwargs.get("document_id")

    if not document_id:
        raise ValidationError("Document id should be provided")
    
    document = get_object_or_404(Document, id=document_id)
    form = UpdateDocumentForm(instance=document)
    
    if request.method == "POST":
        form = UpdateDocumentForm(request.POST, instance=document)
        if form.is_valid():
            form.save()
            return redirect("list_documents")
        
    context = {
        "form": form,
        "document_id": document_id
    }
    return render(request, 'storage/update_document.html', context=context)

def delete_document(request, *args, **kwargs):
   document_id = kwargs.get("document_id")

   if not document_id:
      raise ValidationError("Document id should be provided")
   
   document = get_object_or_404(Document, id=document_id)
   if document.is_deleted:
       document.is_deleted = False
   else:
       document.is_deleted = True
   document.save()
   
   return redirect('view_document', document_id=document.id)

def get_document_versions(request, *args, **kwargs):
   document_id = kwargs.get("document_id")

   if not document_id:
      raise ValidationError("Document id should be provided")
   
   document = get_object_or_404(Document, id=document_id)
   
   latest_version = DocumentVersion.objects.filter(uuid=document.uuid).last()
   
   if latest_version.version == 1:
       previous_version = latest_version
   else:
       previous_version = DocumentVersion.objects.filter(uuid=document.uuid, version=latest_version.version - 1).first()
   context = {
       "document": document,
       "previous_version": previous_version,
   }    
   print(document.name, previous_version.name)
   print(document.content, previous_version.content)

   return render(request, "storage/document_versions.html", context=context)

