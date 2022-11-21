from django.shortcuts import render, HttpResponse, redirect

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
    return render(request,'index.html')
    
def hola_mundo(request):
    return render(request,'hola_mundo.html')

def chau_mundo(request, redirigir=0):
    if redirigir==1:
        return redirect('/')
    if redirigir==2:
        return redirect('/contacto/Rocio')
        
    return HttpResponse(layout+"""
        <h1>CHAUCHIS</h1>
     """)

def contacto(request, nombre="", apellido=""):
    return HttpResponse(layout+f"""<h1>Contacto {nombre} {apellido} </h1>""")