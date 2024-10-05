from django import forms
from .models import Cliente, Producto, Usuario
from django.core.exceptions import ValidationError

class AddClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nit_Cui', 'nombre', 'correoElectronico', 'direccion', 'notas' , 'estado')
        labels = {
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
        
class EditarProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('cantidad', 'descripcion', 'categoria', 'precio_unitario','costo_unitario','imagen')
        labels = {
            'cantidad': 'Cantidad: ',
            'descripcion': 'Descripción de producto: ',
            'categoria': 'Categoría: ',
            'precio_unitario': 'Precio U. GTQ: ',
            'costo_unitario': 'Costo U. GTQ : ',
            'imagen': 'Imagen :',
        }
        widgets = {
            'cantidad': forms.TextInput(attrs={'type': 'text' , 'id': 'cantidad_editar'}),
            'descripcion': forms.TextInput(attrs={'id': 'descripcion_editar'}),
            'categoria': forms.TextInput(attrs={'id': 'categoria_editar'}),
            'precio_unitario': forms.TextInput(attrs={'id': 'precio_editar'}),
            'costo_unitario': forms.TextInput(attrs={'id': 'costo_editar'}),
            'imagen': forms.FileInput(attrs={'id': 'imagen_editar'}),
        }
        
class AddUsuarioForm(forms.ModelForm):
    fecha_ingreso = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    confirmar_clave = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = Usuario
        fields = ('dpi', 'nombre', 'clave', 'confirmar_clave', 'correoElectronico', 'notas', 'fecha_ingreso', 'rol', 'estado')
        labels = {
            'dpi': 'DPI: ',
            'nombre': 'Nombre: ',
            'clave': 'Contraseña: ',
            'confirmar_clave': 'Confirmar Contraseña: ',
            'correoElectronico': 'Correo Electrónico: ',
            'notas': 'Notas: ',
            'fecha_ingreso': 'Fecha de Ingreso: ',
            'rol': 'Cargo: ',
            'estado': 'Estado: ',
        }
        
    def clean(self):
        cleaned_data = super().clean()
        clave = cleaned_data.get("clave")
        confirmar_clave = cleaned_data.get("confirmar_clave")

        if clave and confirmar_clave and clave != confirmar_clave:
            raise forms.ValidationError("Las contraseñas no coinciden.")