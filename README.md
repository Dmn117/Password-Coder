<h1 align="center">Password Coder</h1>

Proyecto para cifrar y descifrar contraseñas

**Objetivo:** No almacenar archivos con contraseñas reales. Este proyecto es un lienzo sobre el cual puedes crear tu propio metodo de cifrado o usar el que ya viene por defecto

<div align="center">

![image](https://github.com/user-attachments/assets/cd135b7d-2cae-4b88-ac20-646e54768b94)

![App version](https://img.shields.io/badge/App-v1.0.0-blue)
![Python version](https://img.shields.io/badge/Python-v3.11.2-blue)
![License](https://img.shields.io/badge/License-MIT-blue)
![Platform](https://img.shields.io/badge/Plataforma-Windows-green)
  
</div>

## Montar Aplicacion

### Descargar Python
- Puedes descargar Python desde su pagina oficial:

  <div align="center">

  [![Python](https://img.shields.io/badge/Python_For_Windows-blue)](https://www.python.org/downloads/windows/)

  <div/>

- Una vez instalado es tan sencillo como ejecutar su IDLE y abrir el / los recursos .py y ejecutar el codigo usando F5

### Alternativamente recomendamos usar Visual Studio Code
- Puedes descargar VSCode desde su pagina oficial o la tienda de Microsoft:

  <div align="center">

  [![VSCode Official](https://img.shields.io/badge/Visual_Studio_Code-blue)](https://code.visualstudio.com/Download)
  [![VSCode Microsoft Store](https://img.shields.io/badge/Visual_Studio_Code_Microsoft_Store-blue)](https://apps.microsoft.com/store/detail/XP9KHM4BK9FZ7Q?ocid=pdpshare)

  <div/>


- No olvides agregar la extension de Python en VSCode y configurar el interprete: 

  
  <div align="center">
    
  [![VSCode Official](https://img.shields.io/badge/Python_In_VSCode-green)](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
  
  <div/>


## Configurar Aplicacion (Desarrollo)

- **characters:** Dentro del codigo la funcion app() contiene los caracteres validos (Puedes agregar mas, solo procura hacer las validaciones correctas para estos).
- **jumps:** Es el numero de posiciones que se pueden intercambiar los caracteres de tu password por los caracteres establecidos en **characters**

```python
def app(): 

    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*().,'
    jumps = 10

```

## Usar la Aplicacion

### Ejecutar

**Puedes Ejecutar**
- Corriendo el codigo desde el interprete
- Invocando el archivo principal .py desde consola
- En una terminal de Visual Studio Code con el poryecto montado
- Ejecutar el archivo .exe recientemente agregado al proyecto (Este no se actualiza con las mejoras que puedas agregar a la aplicacion, mejoraremos el .exe con cada version nueva de este proyecto)

### Interface Inicial

Nuesta Interfaz cuenta con una mascota que te acompañara a lo largo del uso de la aplicacion. Al ejecutarse por primera vez te dara la bienvenida, seguido de la primera interaccion cambiara sus gestos. Prometemos actualizarlos en tanto mejoremos el proyecto.
Las opciones actuales son:
 - 1.- Cifrar Password
 - 2.- Descifrar Password
 - 3.- Salir

**Nota:** Aceptamos sugerencias de funciones a agregar :D

![image](https://github.com/user-attachments/assets/33ad78c2-bef4-430f-8216-613d5ed48621)


### Cifrar Password (Opcion 1)

- Simplemente ingresas un texto (password) el cual desees codificar
- Obtienes el codigo de tu password cifrado
- Puedes repetir este paso tantas veces lo requieras, es decir, puedes cifrar codigos cifrados

**Nota:** Por el momento solo se aceptan letras numeros (del alfabeto Ingles, por ejemplo la ñ por el momento no funciona) y caracteres especiales como: !@#$%^&*()., Todo lo demas sera habilitado en siguientes versiones, incluyendo espacios. Tambien agregaremos soporte para que indique errores del uso de la aplicacion.

#### Cifrado Simple
![image](https://github.com/user-attachments/assets/2ad8e9a2-842e-404e-a7a6-64c5c3f41cb0)

#### Cifrado del cifrado
**Precacion:** Toma en cuenta que entre mas cifras mayor sera el tiempo en que la aplicacion se demorara el devolverte el nuevo cifrado y tambien en descifrarlo.
![image](https://github.com/user-attachments/assets/e91583ec-5485-4ec6-b568-07b5c818e3dd)


### Descifrar Password (Opcion 2)

- Al igual que la opcion recibe una entrada. Tu codigo o Password cifrado.
- Obtienes el codigo original del cifrado, es decir, si tu cifrado fue simple (solo cifraste tu password 1 vez) te devolvera el password original, por el contrario, si lo cifraste varias veces, te devolvera el cifrado anterior, deberas repetir el proceso hasta obtener el password original.

**Nota:** Agregaremos soporte y alertas para advertir sobre codigos que ya no se puedan descifrar mas

#### Descifrado Simple
![image](https://github.com/user-attachments/assets/bffc6f26-8e18-4e40-a5d4-3ff0efcb038d)

#### Descifrado del cifrado
**Precacion:** Como indicamos anteriormente, querer descifrar un password que no tiene cifrado emitira un error. Estamos trabajando para resolverlo en la siguiente version :D
![image](https://github.com/user-attachments/assets/24e48ae2-1bef-4e03-b543-d1afad6c5521)


### Salir del Programa
Basta con ingresar la opcion de salida, actualmente es la opcion 3, pero se cambiara para que la opcion sea otra, quizas 0, para dar espacio a otras mas funcionalidades. 
**Nota:** Despues de eso nuestra mascota te despedira amablamente.

![image](https://github.com/user-attachments/assets/28e6c683-82e3-4361-81f9-518f7c5dee98)


