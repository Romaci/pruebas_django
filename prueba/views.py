from django.shortcuts import render, HttpResponse

# Create your views here.

layout = """
<h1> Sitio prueba </h1>
<ul>
    <li>
        <a href="/">Inicio</a>
    </li>
    <li>
        <a href="/hola_mundo">Hola</a>
    </li>
    <li>
        <a href="/chau_mundo">chau</a>
    </li>
    <li>
        <a href="/contacto">contacto</a>
    </li>
</ul>
"""

def index(request):
    return HttpResponse (layout+"""
        <h1>Inicio</h1>
     """)
def hola_mundo(request):
    return HttpResponse(layout+"""
        <h1>Holis</h1>
     """)

def chau_mundo(request):
    return HttpResponse(layout+"""
        <h1>CHAUCHIS</h1>
     """)

def contacto(request, nombre, apellido):
    return HttpResponse(layout+f"""<h1>Contacto {nombre} {apellido} </h1>""")