from django.shortcuts import render, redirect
from .models import Cliente, Producto, Egreso, ProductosEgreso
from .forms import AddClienteForm, EditarClienteForm, AddProductoForm
from django.contrib import messages
from django.views.generic import ListView
from django.http import JsonResponse, HttpResponse
from django.template.loader import get_template
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
from django.conf import settings
import os

# Vistas Clientes.

def ventas_view(request):
    num_ventas = 156
    context = {
        'num_ventas': num_ventas
    }
    return render(request, 'ventas.html', context)

def clientes_view(request):
    clientes = Cliente.objects.all()
    form_personal = AddClienteForm()
    form_editar = EditarClienteForm()
    
    context = {
        'clientes': clientes,
        'form_personal': form_personal,
        'form_editar': form_editar
    }
    return render(request, 'clientes.html', context)


def add_cliente_view(request):
    if request.method == 'POST':
        form = AddClienteForm(request.POST, request.FILES)
        
        if form.is_valid():
            # Extraer el NIT del formulario
            nit = form.cleaned_data.get('nit')
            
            # Validar el NIT
            if not validar_nit(nit):
                messages.error(request, "NIT inválido")
                return redirect('Clientes')
            
            try:
                form.save()
                messages.success(request, "Cliente guardado con éxito")
                
            except Exception as e:
                messages.error(request, f"Error al guardar el cliente: {str(e)}")
                return redirect('Clientes')
        
        else:
            messages.error(request, "Usuario ya existe")
    
    return redirect('Clientes')


def validar_nit(nit):
    '''Funcion para validar NIT'''
    # Elimina espacios en blanco
    nit_n = nit.replace(' ', '')
    # Elimina el guion del nit
    nit_ok = nit_n.replace('-', '')
    # Base para multiplicar
    base = 1

    # Guarda el digito validador, el ultimo
    dig_validador = nit_ok[-1]

    # Guarda el resto de numeros para sumar
    dig_nit = list(nit_ok[0:-1])

    # Reverse invierte el orden de los digitos del original
    # El array inverso se refleja al original
    dig_nit_rev = dig_nit.reverse()  # None

    try:
        suma = 0
        # Por cada numero del nit en inversa
        for n in dig_nit:
            base += 1
            suma += int(n) * base

        # Guarda el residuo
        resultado = suma % 11
        comprobacion = 11 - resultado

        if suma >= 11:
            resultado = suma % 11
            comprobacion = 11 - resultado

        if comprobacion == 10:
            if dig_validador.upper() == 'K':
                return True

        elif comprobacion == int(dig_validador):
            return True

        else:
            return False

    except:
        return False
    

def edit_cliente_view(request):
    if request.method == 'POST':
        cliente = Cliente.objects.get(pk=request.POST.get('id_personal_editar'))
        # Pasa la instancia del cliente, no la clase 'Cliente'
        form = EditarClienteForm(request.POST, request.FILES, instance=cliente)
        # Asegúrate de que estás llamando al método is_valid()
        if form.is_valid():
            form.save()
    
    return redirect('Clientes')


def delete_cliente_view(request):
    if request.POST:
        cliente = Cliente.objects.get(pk=request.POST.get('id_personal_eliminar'))
        cliente.delete()
    return redirect('Clientes')



#Vistas de Productos

def productos_view(request):
    """
    clientes = Cliente.objects.all()
    
    form_editar = EditarClienteForm()
    """
    productos = Producto.objects.all()
    form_add = AddProductoForm()
    
    context = {
        'productos': productos,
        'form_add': form_add
    }
    return render(request, 'productos.html', context)


def add_producto_view(request):
    #print("Guardar Cliente")
    if request.POST:
        form = AddProductoForm(request.POST, request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages(request, "Error al guardar el producto")
                return redirect('Productos')
    return redirect('Productos')


# Vista Venta

class add_ventas(ListView):
    template_name = 'add_ventas.html'
    model = Egreso

    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)
    """
    def get_queryset(self):
        return ProductosPreventivo.objects.filter(
            preventivo=self.kwargs['id']
        )
    """
    def post(self, request,*ars, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'autocomplete':
                data = []
                for i in Producto.objects.filter(descripcion__icontains=request.POST["term"])[0:10]:
                    item = i.toJSON()
                    item['value'] = i.descripcion
                    data.append(item)
            else:
                data['error'] = "Ha ocurrido un error"
        except Exception as e:
            data['error'] = str(e)

        return JsonResponse(data,safe=False)
    
    
def export_pdf_view(request, id, iva):
    #print(id)
    template = get_template("ticket.html")
    #print(id)
    subtotal = 0 
    iva_suma = 0 

    venta = Egreso.objects.get(pk=float(id))
    datos = ProductosEgreso.objects.filter(egreso=venta)
    for i in datos:
        subtotal = subtotal + float(i.subtotal)
        iva_suma = iva_suma + float(i.iva)

    empresa = "Mi empresa S.A. De C.V"
    context ={
        'num_ticket': id,
        'iva': iva,
        'fecha': venta.fecha_pedido,
        'cliente': venta.cliente.nombre,
        'items': datos, 
        'total': venta.total, 
        'empresa': empresa,
        'comentarios': venta.comentarios,
        'subtotal': subtotal,
        'iva_suma': iva_suma,
    }
    html_template = template.render(context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "inline; ticket.pdf"
    css_url = os.path.join(settings.BASE_DIR,'index\static\index\css/bootstrap.min.css')
    #HTML(string=html_template).write_pdf(target="ticket.pdf", stylesheets=[CSS(css_url)])
   
    font_config = FontConfiguration()
    HTML(string=html_template, base_url=request.build_absolute_uri()).write_pdf(target=response, font_config=font_config,stylesheets=[CSS(css_url)])

    return response
