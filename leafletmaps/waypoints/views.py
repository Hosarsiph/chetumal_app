# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response

import psycopg2


def index(request):


    conn = psycopg2.connect(database="chetumal", user="postgres", password="postgres")
    cur = conn.cursor()

    print "conectado a la base de datos"

    conn.commit()

    cur.close()
    conn.close()


    return render_to_response('index.html', {
        'title': 'CHETUMAL APP'
    })
