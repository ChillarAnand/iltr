# -*- coding: utf-8 -*-

from django.db import models

from apps.base.models import AuditModel


class Author(AuditModel):
    """
    List of all authors.
    """
    first_name = models.CharField(max_length=255, blank=True)
    middle_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.first_name

    def full_name(self):
        """
        Get full name of author.
        """
        return self.first_name + self.middle_name + self.last_name


class Language(AuditModel):
    """
    List of all languages.
    """
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(AuditModel):
    """
    List of all books.
    """
    author = models.ForeignKey('Author')
    language = models.ForeignKey('Language')
    name = models.CharField(max_length=255)
    translated_name = models.CharField(max_length=255, blank=True)
    published_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
