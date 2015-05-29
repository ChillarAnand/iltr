import os

from bs4 import BeautifulSoup
from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction

from apps.books.models import Book, Author, Language


class Command(BaseCommand):
    help = "Add gutenberg books to database."

    @transaction.atomic
    def handle(self, *args, **kwargs):
        dir_loc = os.path.join(settings.BASE_DIR, 'db/gutenberg/')
        print("Gutenberg db files: ", dir_loc)
        count = 0
        for dirpath, dirnames, filenames in os.walk(dir_loc):
            if filenames:
                try:
                    file_name = os.path.join(dirpath, filenames[0])
                    import pudb; pudb.set_trace();
                    title, author, language = self.parse_file(file_name)
                    
                    author, created = Author.objects.get_or_create(full_name=author)
                    language, created = Language.objects.get_or_create(code=language)
                    book, created = Book.objects.get_or_create(name=title, author=author, language=language)
                    print(title, author, language)

                    count += 1
                    if count == 1000:
                        break;
                except:
                    pass

    def parse_file(self, file_name):
        """
        Parse rdf file.
        """
        fh = open(file_name)
        soup = BeautifulSoup(fh)
        title = soup.find('dcterms:title').get_text()
        try:
            author = soup.find('dcterms:creator').find('pgterms:alias').get_text()
        except:
            author = soup.find('dcterms:creator').find('pgterms:name').get_text()
        language = soup.find('dcterms:language').find('rdf:value').get_text()

        return title, author, language
