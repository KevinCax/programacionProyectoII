from django import forms
from ventas.models import Cliente, Producto

class AddClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('codigo', 'nitOCui', 'nombre', 'correoElectronico', 'direccion', 'notas')
        labels = {
            'codigo': 'Codigo cliente: ',
            'nitOCui': 'Nit o Cui: ',
            'nombre': 'Nombre : ',
            'correoElectronico': 'Correo Electrónico: ',
            'direccion': 'Dirección: ',
            'notas': 'Notas: ',
            'estado': 'Estado: ',
        }
        
        
class EditarClienteForm(forms.ModelForm):
     class Meta:
        model = Cliente
        fields = ('nombre','correoElectronico','direccion','notas')
        labels = {
            'nombre': 'Nombre : ',
            'correoElectronico': 'Correo Electrónico: ',
            'direccion': 'Dirección: ',
            'notas': 'Notas: ',
            'estado': 'Estado: ',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'type': 'text', 'id': 'nombre_editar'}),
            'correoElectronico': forms.TextInput(attrs={'id': 'correo_editar'}),
            'direccion': forms.TextInput(attrs={'id': 'direccion_editar'}), 
            'notas': forms.TextInput(attrs={'id': 'notas_editar'}),
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