from django import forms
from ventas.models import Cliente, Producto

class AddClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('codigo', 'nit', 'cui', 'nombre', 'telefono')
        labels = {
            'codigo': 'Codigo cliente: ',
            'nit': 'Nit cliente: ',
            'cui': 'Cui cliente: ',
            'nombre': 'Nombre cliente: ',
            'telefono': 'Telefono : ',
        }
        
        
class EditarClienteForm(forms.ModelForm):
     class Meta:
        model = Cliente
        fields = ('codigo', 'nit', 'cui', 'nombre', 'telefono')
        labels = {
            'codigo': 'Codigo cliente: ',
            'nit': 'Nit cliente: ',
            'cui': 'Cui cliente: ',
            'nombre': 'Nombre cliente: ',
            'telefono': 'Telefono : ',
        }
        widgets = {
            'codigo': forms.TextInput(attrs={'type': 'text', 'id': 'codigo_editar'}),
            'nit': forms.TextInput(attrs={'id': 'nit_editar'}),
            'cui': forms.TextInput(attrs={'id': 'cui_editar'}),
            'nombre': forms.TextInput(attrs={'id': 'nombre_editar'}),
            'telefono': forms.TextInput(attrs={'id': 'telefono_editar'}),
            
        }
        
        
class AddProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('codigo', 'cantidad', 'descripcion', 'categoria', 'precio_unitario','costo_unitario','imagen')
        labels = {
            'codigo': 'Cód. Producto: ',
            'cantidad': 'Cantidad: ',
            'descripcion': 'Descripción de producto: ',
            'categoria': 'Categoría: ',
            'precio_unitario': 'Precio U. GTQ: ',
            'costo_unitario': 'Costo U. GTQ : ',
            'imagen': 'Imagen :',
        }