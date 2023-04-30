from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
import uuid


class Document(models.Model):
    uuid = models.UUIDField(
        verbose_name='Идентификатор',
        default = uuid.uuid4
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Название документа',
    )
    content = models.TextField(
        verbose_name='Содержание документа',
    )
    is_deleted = models.BooleanField(
        default=False,
        verbose_name='Помечен на удаление'
    )

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"

# 17a6758f-22fa-4ddc-b031-bd8985000c16

class DocumentVersion(models.Model):
    document = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
        related_name='versions',
    )
    uuid = models.CharField(
        max_length=255,
        verbose_name='Идентификатор документа',
        null=True,
        blank=True
    )
    version = models.PositiveIntegerField(
        verbose_name="Версия документа", 
        default=1, 
        blank=True, 
        null=True
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Название документа',
    )
    content = models.TextField(
        verbose_name='Содержание документа',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    
    def __str__(self):
        return f'{self.document} - {self.version}'
    
    class Meta:
        verbose_name = "Version"
        verbose_name_plural = "Versions"    

@receiver(post_save, sender=Document)    
def document_created_handler(sender, instance, created, *args, **kwargs):
    if created:
        document_version = DocumentVersion.objects.create(
            document=instance,
            name=instance.name,
            content=instance.content,
            uuid=instance.uuid
        )
        document_version.save()
    else:
        latest_version = DocumentVersion.objects.filter(uuid=instance.uuid).last()
        version_number = latest_version.version
        new_version = DocumentVersion.objects.create(
            document=instance,
            name=instance.name,
            version=version_number + 1,
            content=instance.content,
            uuid=instance.uuid
        )
        new_version.save
