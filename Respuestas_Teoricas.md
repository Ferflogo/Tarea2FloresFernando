# Tarea2FloresFernando

""" 1) ¿Qué es Git? 

Git es sistema de control de versiones, el cual es un programa que administra las distintas versiones de un programa/código. No es el único programa de control de versiones. Gracias a este programa se puede trabajar por medio de internet y en simultaneo por lo cual no es necesario estarse enviando los archivos, los otros usuarios pueden alterar el código por medio de una copia local.

Se puede observar la versión, los cambios, las líneas que se cambiaron, fechas y usuarios.

Git Bash es una consola o terminal

Funciones utiles

Git init: Inicia proyecto
Git status: Archivos dentro de entorno de trabajo
Git diff: Observar diferencias
Git log: Ver versiones anteriores

2) Que es Github? 

Servicio en la nube, es una erramienta para desarrollo de codigo el cual facilita a desarrolladores a almacenar y administrar sus códigos, al igual que llevar un registro y control, para un mejor trabajo en equipo.

3) Que es un branch? 

Git branch <Nombre>: Genera una copia del archivo principal
  
  Los branch son "Ramas" en las cuales se pueden generar para modificar el codigo y unir una vez se este satisfecho con el funcionamiento.
  
4) Que es un commit? 

Git commit: Crear punto de control

Por medio de este codigo se guarda o suben archivos.

Crea comentarios con git commit -m, sin entrar a terminal. La primera vez que se ejecuta nos pedirá identificarnos (Usuario), por medio de un correo.

5) Que se entiende cuando se dice que un archivo esta “staged”? 

Dentro de git se divide en tre areas de trabajo Working Directory, Staging Area y Repository

Esto se trabaja con tres estados: committed, modifie y staged. 

Cuando se utiliza commit, git crea un nuevo objeto de commit utilizando los archivos del stage y establece el padre al commit actual. Staged es un archivo modificado esta listo para ir a la proxima area de trabajo.


6) Que hace el comando git checkout?

Git checkout – <Nombre de Archivo>: Para revertir los cambios
Git checkout <Nombre>: Se utiliza para cambiar el archivo a trabajar creado por medio del Branch. Se cambia entre “Ramas”
  
7) Que hace el comando git stash?

Git stash: Esta funcion se utiliza para salvar cambios que están comprometidos temporalmente, guardado provisional.

8) Que hace el comando git add?

Git add <File>: Agregar archive a tu espacio de trabajo
Git add . : Agrega todos los archivos
  
 9) Que es Pytest? 
 
Unit Testing es un método de prueba en el cual se prueban unidades de código individual, para determinar si estas funcionan.
Por ejemplo en diseño estructurado o en diseño funcional una función o un procedimiento, en diseño orientado a objetos una clase. Esto sirve para asegurar que cada unidad funcione correctamente y eficientemente por separado.

Pytest es un entorno de trabajo que permite probar tus codigos por medio de programas.

Ventajas

Reduce Bugs en nuevas y viejas implementaciones
Genera una buena documentación
Rápido Debugging
Mejor diseño

10) Bajo el contexto de pytest. Que es un “assert”? 

Un assert es una bandera booleana la cual nos indica si una condicion se cumple o no. En pytest si assert es falso se detiene ese codigo del programa.


11) Que es Flake 8? 

Es un programa el cual prueba todo el codigo y muestra todos errores y malas practicas de programacion, tambien ayuda con consejos de codigos optimos para funciones especificas.
"""
