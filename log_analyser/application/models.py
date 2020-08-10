from django.db import models

# Create your models here.

def read_file(uploaded_file_url):
    uploaded_file_url = '.' + uploaded_file_url
    file = open(uploaded_file_url, 'r')
    lines = file.readlines()
    content = []
    for item in lines:
        content.append(item)
    return content


def read_file_filter(uploaded_file_url, key):
    uploaded_file_url = '.' + uploaded_file_url
    file = open(uploaded_file_url, 'r')
    lines = file.readlines()
    content = []
    for item in lines:
        if key in item:
            content.append(item)
    return content

