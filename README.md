# JAPPY: Educational resource for programming classes in  Java,  C++ and Python


## Implantación del ambiente de desarrollo

### Software base

Los ejemplos y las tareas de la asignatura se realizarán utilizando VS Code como herramienta de desarrollo y Docker como tecnología de infraestructura. Para lograr esto, en su computador deberá instalar:

* [VS Code](https://code.visualstudio.com)
* [Docker desktop](https://docs.docker.com/get-docker/)
* [GitHub CLI](https://github.com/cli/cli#installation)


**Observación**: Se recomienda que en la instalación de VS Code, se seleccione la opción **Agregar opción Abrir con VS Code** a archivos y directorios. Esta opción está sólo disponible en forma nativa para la versión de Windows. Si utiliza MacOSX, deberá seguir las instrucciones que se detallan a continuación.

><details>
><summary>Opción "Abrir en VS Code" en MacOSX</summary>
>
>- Abrir Automator
>- Crear un nuevo documento
>- Seleccionar "Acción rápida"
>- Configura "FLujo de trabajo recibe el actual" a `archivos o carpetas` en `cualquier aplicaciòn`
>- Agregar la acción `Ejecutar el script shell` 
>- configurar "Shell" al que utilizan normalmente (p.e. `/bin/bash`)
>- Configurar "Pasar datos de entrada" a `como argumentos`
>- En la sección del código del script, escribir:
><pre>
>   for f in "$@"; do
>     open -a 'Visual Studio Code' "$@"
>   done
></pre>
>- Salvar como  `Abrir en VS Code`
></details>

### Instalación del contenedor de desarrollo 
1) Crear una carpeta y abrir un terminal dentro de esa carpeta:

<figure>
    <div align="center" width="80%">
        <img width="80%" src="https://raw.githubusercontent.com/g-courses/jappy.rc/refs/heads/main/imgs/classroom/paso01.png" alt=""/>
        <br />
        <figure-caption>Figura 1. Ejemplo de creación de carpeta "clases" y el terminal respectivo.</figure-caption>
    </div>
</figure>

<br />

2) Clone este repositorio:

```
git clone https://github.com/g-courses/jappy.classroom.git
```

<figure>
    <div align="center" width="80%">
        <img width="80%" src="https://raw.githubusercontent.com/g-courses/jappy.rc/refs/heads/main/imgs/classroom/paso02-01.png" alt=""/>
        <br />
        <figure-caption>Figura 2a. Clonación a través del comando git.</figure-caption>
    </div>    
</figure>

<br />

Debe verificar que los archivos `.devcontainer.json` y `docker-compose.yml` estén en el directorio creado:

<figure>
    <div align="center" width="80%">
        <img width="60%" src="https://raw.githubusercontent.com/g-courses/jappy.rc/refs/heads/main/imgs/classroom/paso02-02.png" alt=""/>
        <br />
        <figure-caption>Figura 2b. Verificación de los archivos de configuración del ambiente de desarrollo.</figure-caption>
    </div>    
</figure>

<br />


3) En el explorador de archivos, seleccione `Abrir con VS Code` en el menú contextual de la carpeta `codes_examples`.

<figure>
     <div align="center" width="80%">
        <img width="80%" src="https://raw.githubusercontent.com/g-courses/jappy.rc/refs/heads/main/imgs/classroom/paso03.png" alt=""/>
        <br />
        <figure-caption>Figura 3. Selección opción "Abrir con VS Code" en el caso de MacOSX.</figure-caption>
    </div>
</figure>

<br />


4) Una vez que `VS Code` se ejecute, mostrará un aviso como el de la Figura 4. Seleccione **Volver a abrir en el contenedor**.

<figure>
    <div align="center" width="80%">
        <img src="https://raw.githubusercontent.com/g-courses/jappy.rc/refs/heads/main/imgs/classroom/paso04.png" alt=""/>
        <br />
        <figure-caption>Figura 4. VS Code avisa que encontró una configuración de un contenedor de desarrollo, por lo que es necesario abrir nuevamente la carpeta con esta opción.</figure-caption>
    </div>
</figure>

<br />

5) Si el aviso anterior desaparece, entonces seleccione el complemento "Explorador remoto" y abra la carpeta en el contenedor de desarrollo de la asignatura.

<figure>
    <div align="center" width="80%">
    <img width="80%" src="https://raw.githubusercontent.com/g-courses/jappy.rc/refs/heads/main/imgs/classroom/paso05.png" alt=""/>
    <br />
    <figure-caption>Figura 5. Abrir la carpeta en un contenedor de desarrollo. Esta opción abrirá y ejectura el contenedor de desarrollo de la asignatura.</figure-caption>
    </div>
</figure>

<br />

6) Una vez realizado el paso 4 o 5, `VS Code` pasa por distinto estados, tal como muestran en la Figura 6. El primer paso la primera vez se puede demorar debido a que tiene que bajar la imagen del contenedor, cuyo tamaño es de aproximadamente 7 GB.

<figure>
    <div align="center" width="80%">
        <img width="60%" src="https://raw.githubusercontent.com/g-courses/jappy.rc/refs/heads/main/imgs/classroom/paso06.png" alt=""/>
        <br />
        <figure-caption>Figura 6. En la esquina inferior derecha VS Code muestra el estado de preparación del ambiente de desarrollo.</figure-caption>
    </div>
</figure>

<br />

7) Una vez que la imagen está configurada, `VS Code` tendrá una apariencia similar a la que se muestra en la Figura 7.

<figure>
    <div align="center" width="100%">
        <img src="https://raw.githubusercontent.com/g-courses/jappy.rc/refs/heads/main/imgs/classroom/paso07.png" alt=""/>
        <br />
        <figure-caption>Figura 7. Ambiente de desarrollo instalado con éxito. En la sección *WORKSPAXE* debe estar las carpetas que se localizan dentro de la carpeta `workpace` en el host.</figure-caption>
    </div>
</figure>

<br />

### Prueba de funcionamiento del intérprete Python del contenedor de desarrollo

El contenido de desarrollo tiene todo lo necesario para el desarrollo de la asignatura: compiladores de `C++`, `Java` e intérprete de `Python`. Además, tiene los complementos de `VS Code` para facilitar la codificación en estos lenguajes. Se debe destacar que **no es necesario que estas herramientas estén instaladas en su computador**. Esto ya está resuelto a nivel del contenedor de desarrollo.

1) Seleccione la carpeta `notebook-examples` y luego el archvo `python_nb.ipynb`, tal como se muestra en la Figura 8.

<figure>
    <div align="center" width="80%">
        <img src="https://raw.githubusercontent.com/g-courses/jappy.rc/refs/heads/main/imgs/classroom/func01.png" alt=""/>
        <br />
        <figure-caption>Figura 8. Selección de carpetas en el contenedor de desarrollo.</figure-caption>
    </div>
</figure>

<br />

2) Para ejecutar el notebook, es necesario seleccionar un kernel apropiado. Se debe recordar que se debe seleccionar uno que **esté instalado en el contenedor**.

><details>
><summary>Pasos para seleccionar un kernel</summary>
>
>Para seleccionar un kernel, debe hacer click en el botón `Seleccionar el kernel` en el sector superior derecho de VS Code. Tras seleccionar `Servidor de Jupyter existente`, se debe ingresar la URL del servidor jupyter instalado en el contenedor (`http://localhost:8888`). Debido a que esta es una dirección no segura, se debe aceptar explícitamente la conexión. Estos pasos se muestran en la Figura A.
>
><figure>
>    <div align="center" width="80%">
>        <img src="https://raw.githubusercontent.com/g-courses/jappy.rc/refs/heads/main/imgs/classroom/kernel01.png" alt=""/>
>        <br />
>        <figure-caption>Figura A. Pasos iniciales para seleccionar un kernel en el contenedor.</figure-caption>
>    </div>
></figure>
>
><br />
>
> Luego de aceptar la conexión no segura, se puede cambiar el nombre que VS Code usará para referenciar el servidor jupyter. En la Figura B, muestra que el nombre por omisión `localhost` se cambia a uno más representativo, como `jappy_server`.
>
><figure>
>    <div align="center" width="100%">
>        <img width="80%" src="https://raw.githubusercontent.com/g-courses/jappy.rc/refs/heads/main/imgs/classroom/kernel02.png" alt=""/>
>        <br />
>        <figure-caption>Figura B. Cambio del nombre lógico del servidor jupyter del contenedor.</figure-caption>
>    </div>
></figure>
>
><br />
>
>Finalmente, se selecciona el kernel a utilizar.
>
><figure>
>    <div align="center" width="80%">
>        <img width="80%" src="https://raw.githubusercontent.com/g-courses/jappy.rc/refs/heads/main/imgs/classroom/kernel03.png" alt=""/>
>        <br />
>        <figure-caption>Figura C. Selección del kernel que se utilizará en el cuaderno jupyter.</figure-caption>
>    </div>
></figure>
>
>Una vez finalizado esto pasos, los otros kernels se pueden seleccionar escogiendo el servidor `jappy_server` creado.
>
></details>


3) Finalmente, presione `Ejecutar todo`. El cuaderno Jupyter debe mostrar un mensaje `Hola mundo`, un grafico sencillo y un diagrama UML. Si lo anterior se cumple, el servidor Jupyter está operando y su ambiente de desarrollo esta listo.
