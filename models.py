# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Book(models.Model):
	name = models.CharField(max_length=255, null=True)
	desc = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	modified_at = models.DateTimeField(auto_now = True)

class Author(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	modified_at = models.DateTimeField(auto_now = True)
	notes = models.TextField()
	books = models.ManyToManyField(Book, related_name = "authors")
	
	


