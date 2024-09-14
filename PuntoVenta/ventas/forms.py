from django import forms
from ventas.models import Cliente, Producto
from django.core.exceptions import ValidationError

class AddClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('codigo', 'nit_Cui', 'nombre', 'correoElectronico', 'direccion', 'notas' , 'estado')
        labels = {
            'codigo': 'Codigo cliente: ',
            'nit_Cui': 'Nit o Cui: ',
            'nombre': 'Nombre : ',
            'correoElectronico': 'Correo Electrónico: ',
            'direccion': 'Dirección: ',
            'notas': 'Notas: ',
            'estado': 'Estado: ',
        }
        
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise ValidationError("El nombre es obligatorio.")
        palabras = nombre.split()
        if len(palabras) < 2:
            raise ValidationError("El nombre debe constar de al menos dos palabras.")
        if not all(palabra.isalpha() for palabra in palabras):
            raise ValidationError("El nombre solo puede contener letras.")
        return nombre

    def clean_correoElectronico(self):
        correo = self.cleaned_data.get('correoElectronico')
        if not correo:
            raise ValidationError("El correo electrónico es obligatorio.")
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, correo):
            raise ValidationError("El correo electrónico no es válido.")
        return correo
        
        
class EditarClienteForm(forms.ModelForm):
     class Meta:
        model = Cliente
        fields = ('nombre','correoElectronico','direccion','notas')
        labels = {
            'nombre': 'Nombre : ',
            'correoElectronico': 'Correo Electrónico: ',
            'direccion': 'Dirección: ',
            'notas': 'Notas: ',
            
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'type': 'text' , 'id': 'nombre_editar'}),
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