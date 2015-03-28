# -*- coding: utf-8 -*-

from django.db import models

from apps.base.models import AuditModel


class Author(AuditModel):
    """
    List of all authors.
    """
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class Language(AuditModel):
    """
    List of all languages.
    """
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    

class Book(AuditModel):
    """
    List of all books.
    """
    author = models.ForeignKey('Author')
    language = models.ForeignKey('Language')
    name = models.CharField(max_length=255)
    published_date = models.DateField()
    
    

