# JAPPY: Recurso educacional para realizar clases de programación en Java, C++ y Python


## 1) Implantación del contenedor de desarrollo

<details>
<summary>Mostrar</summary>

### 1.1) Software base

Los ejemplos y las tareas de la asignatura se realizarán utilizando `VS Code` como herramienta de desarrollo y Docker como tecnología de infraestructura. Para lograr esto, en su computador deberá instalar:

* [Docker desktop](https://docs.docker.com/get-docker/)
* [VS Code](https://code.visualstudio.com). Se debe instalar el plugin [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).
* [GitHub CLI](https://github.com/cli/cli#installation) *(Opcional)*


**Observación**: Se recomienda que en la instalación de `VS Code`, se seleccione la opción **Agregar opción Abrir con VS Code** a archivos y directorios. Esta opción está sólo disponible en forma nativa para la versión de Windows. Si utiliza MacOSX, deberá seguir las instrucciones que se detallan a continuación.

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


### 1.2) Instalación del contenedor de desarrollo 


Para instalar el contenedor de desarrollo, es suficiente tener los archivos `.devcontainer.json` y `docker-compose.yml` dentro de una carpeta. Este ejemplo muestra la obtención de estos archivos a través de la clonación de un repositorio determinado.

1) Crear una carpeta y abrir un terminal dentro de esa carpeta:

<figure>
    <div align="center" width="80%">
        <img width="80%" src="https://raw.githubusercontent.com/g-courses/jappy.rc/refs/heads/main/imgs/classroom/paso01.png" alt=""/>
        <br />
        <figure-caption>Figura 1.2.1 Ejemplo de creación de carpeta "clases" y el terminal respectivo.</figure-caption>
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
        <figure-caption>Figura 1.2.2a Clonación a través del comando git.</figure-caption>
    </div>    
</figure>

<br />


Debe verificar que los archivos `.devcontainer.json` y `docker-compose.yml` estén en el directorio creado:

<figure>
    <div align="center" width="80%">
        <img width="60%" src="https://raw.githubusercontent.com/g-courses/jappy.rc/refs/heads/main/imgs/classroom/paso02-02.png" alt=""/>
        <br />
        <figure-caption>Figura 1.2.2b Verificación de los archivos de configuración del ambiente de desarrollo.</figure-caption>
    </div>    
</figure>

<br />

>**Nota**: Debe revisar que la directiva `platform` en el archivo `docker-compose.yml` coincida con la arquitectura del procesador de su computador. Use `linux/amd64` si el procesador es arquitectura Intel o AMD. Si es ARM, use `linux/arm64`.

</details>

## 2) Uso del contenedor con Jupyter Lab

<details>
<summary>Mostrar</summary>

En este caso, el inicio y apagado del contenedor se realiza a través de la plataforma `Docker Compose`. Una vez que el contenedor se inicia, la herramientas de desarrollo se acceder a través de un servidor Jupyter Lab.

Partiendo del paso 2) de la sección 1.2), abra un terminal en la carpeta `jappy.classroom`.

<figure>
     <div align="center" width="80%">
        <img width="80%" src="https://raw.githubusercontent.com/g-courses/jappy.rc/refs/heads/main/imgs/classroom/jupyter01.png" alt=""/>
        <br />
        <figure-caption>Figura 2.1 Terminal abierto en la carpeta jappy.classroom del repositorio clonado en el punto 1.2).</figure-caption>
    </div>
</figure>

<br />

Luego, inicie el contenedor con el comando `docker compose up -d`.

<figure>
     <div align="center" width="80%">
        <img width="80%" src="https://raw.githubusercontent.com/g-courses/jappy.rc/refs/heads/main/imgs/classroom/jupyter02.png" alt=""/>
        <br />
        <figure-caption>Figura 2.2 Inicio del contenedor a través de Docker Compose.</figure-caption>
    </div>
</figure>

<br />

Una vez iniciado, puede ingresar con su navegador web de preferencia a la URL `http://localhost:8888`. Se mostrará el acceso al servidor Jupyter Lab.

<figure>
     <div align="center" width="80%">
        <img width="80%" src="https://raw.githubusercontent.com/g-courses/jappy.rc/refs/heads/main/imgs/classroom/jupyter03.png" alt=""/>
        <br />
        <figure-caption>Figura 2.3 Servidor Jupyter Lab iniciado en el contenedor de desarrollo.</figure-caption>
    </div>
</figure>

<br />

Para detener el contenedor, debe ingresar el comando `docker compose down`.

<figure>
     <div align="center" width="80%">
        <img width="80%" src="https://raw.githubusercontent.com/g-courses/jappy.rc/refs/heads/main/imgs/classroom/jupyter05.png" alt=""/>
        <br />
        <figure-caption>Figura 2.4 Proceso de apagado del contenedor a través de Docker Compose.</figure-caption>
    </div>
</figure>

<br />

</details>


## 3) Uso del contenedor con VS Code

<details>
<summary>Mostrar</summary>

En este caso, el software `VS Code` inicia el contenedor revisando el contenido del archivo `.devcontainer.json` y `docker-compose.yml`.

1) En el explorador de archivos, seleccione `Abrir con VS Code` en el menú contextual de la carpeta `codes_examples`.

<figure>
     <div align="center" width="80%">
        <img width="80%" src="https://raw.githubusercontent.com/g-courses/jappy.rc/refs/heads/main/imgs/classroom/paso03.png" alt=""/>
        <br />
        <figure-caption>Figura 3.1 Selección opción "Abrir con VS Code" en el caso de MacOSX.</figure-caption>
    </div>
</figure>

<br />


2) Una vez que `VS Code` se ejecute, mostrará un aviso como el de la Figura 3.2. Seleccione **Volver a abrir en el contenedor**.

<figure>
    <div align="center" width="80%">
        <img src="https://raw.githubusercontent.com/g-courses/jappy.rc/refs/heads/main/imgs/classroom/paso04.png" alt=""/>
        <br />
        <figure-caption>Figura 3.2 VS Code avisa que encontró una configuración de un contenedor de desarrollo, por lo que es necesario abrir nuevamente la carpeta con esta opción.</figure-caption>
    </div>
</figure>

<br />

3) Si el aviso anterior desaparece, entonces seleccione el complemento "Explorador remoto" y abra la carpeta en el contenedor de desarrollo de la asignatura.

<figure>
    <div align="center" width="80%">
    <img width="80%" src="https://raw.githubusercontent.com/g-courses/jappy.rc/refs/heads/main/imgs/classroom/paso05.png" alt=""/>
    <br />
    <figure-caption>Figura 3.3 Abrir la carpeta en un contenedor de desarrollo. Esta opción abrirá y ejectura el contenedor de desarrollo de la asignatura.</figure-caption>
    </div>
</figure>

<br />

4) Una vez realizado el paso 2 ó 3, `VS Code` pasa por distinto estados, tal como muestran en la Figura 3.4. El primer paso la primera vez se puede demorar debido a que tiene que bajar la imagen del contenedor, cuyo tamaño es de aproximadamente 10 GB.

<figure>
    <div align="center" width="80%">
        <img width="60%" src="https://raw.githubusercontent.com/g-courses/jappy.rc/refs/heads/main/imgs/classroom/paso06.png" alt=""/>
        <br />
        <figure-caption>Figura 3.4 En la esquina inferior derecha VS Code muestra el estado de preparación del ambiente de desarrollo.</figure-caption>
    </div>
</figure>

<br />

5) Una vez que la imagen está configurada, `VS Code` tendrá una apariencia similar a la que se muestra en la Figura 3.5.

<figure>
    <div align="center" width="100%">
        <img src="https://raw.githubusercontent.com/g-courses/jappy.rc/refs/heads/main/imgs/classroom/paso07.png" alt=""/>
        <br />
        <figure-caption>Figura 3.5 Ambiente de desarrollo instalado con éxito. En la sección *WORKSPACE* debe estar las carpetas que se localizan dentro de la carpeta `workpace` en el host.</figure-caption>
    </div>
</figure>

<br />

</details>

## 4) Prueba de funcionamiento del contenedor con Jupyter Lab

<details>
<summary>Mostrar</summary>

Ingrese al directorio `workspace/notebook-examples` y seleccione el archivo `python_nb.ipynb`.

<figure>
     <div align="center" width="80%">
        <img width="100%" src="https://raw.githubusercontent.com/g-courses/jappy.rc/refs/heads/main/imgs/classroom/jupyter04.png" alt=""/>
        <br />
        <figure-caption>Figura 4.1 Cuaderno Jupyter de prueba.</figure-caption>
    </div>
</figure>

<br />

Finalmente, presione `Ejecutar todo` (botón `P` en la Figura 4.1. El cuaderno Jupyter debe mostrar un mensaje `Hola mundo`, un grafico sencillo y un diagrama UML. Si lo anterior se cumple, el servidor Jupyter Lab está operando.

>Nota: El kernel del cuaderno se puede cambiar presionando la sección `K` que se muestra en la Figura 4.1.


</details>


## 5) Prueba de funcionamiento del contenedor con VS Code

<details>
<summary>Mostrar</summary>

El contenedor de desarrollo tiene todo lo necesario para el desarrollo de la asignatura: compilador de `C++` y `Java` e intérprete de `Python`. Además, tiene los complementos de `VS Code` para facilitar la codificación en estos lenguajes. Se debe destacar que **no es necesario que estas herramientas estén instaladas en su computador**. Esto ya está resuelto a nivel del contenedor de desarrollo.

1) Seleccione la carpeta `notebook-examples` y luego el archvo `python_nb.ipynb`, tal como se muestra en la Figura 5.1.

<figure>
    <div align="center" width="80%">
        <img src="https://raw.githubusercontent.com/g-courses/jappy.rc/refs/heads/main/imgs/classroom/func01.png" alt=""/>
        <br />
        <figure-caption>Figura 5.1 Selección de carpetas en el contenedor de desarrollo.</figure-caption>
    </div>
</figure>

<br />

2) Para ejecutar el notebook, es necesario seleccionar un kernel apropiado. Se debe recordar que se debe seleccionar uno que **esté instalado en el contenedor**.


3) Finalmente, presione `Ejecutar todo`. El cuaderno Jupyter debe mostrar un mensaje `Hola mundo`, un grafico sencillo y un diagrama UML. Si lo anterior se cumple, el servidor Jupyter está operando y su ambiente de desarrollo esta listo.

>**Nota** Debido a que el contenedor iniciado a través de `VS Code` queda asociado al puerto `8888/tcp`, no pueden exister simultáneamente dos contenedores.

</details>

## 6) Selección de kernel

<details>
<summary>Mostrar</summary>

Para seleccionar un kernel, debe hacer click en el botón `Seleccionar el kernel` en el sector superior derecho de VS Code. Tras seleccionar `Servidor de Jupyter existente`, se debe ingresar la URL del servidor jupyter instalado en el contenedor (`http://localhost:8888`). Debido a que esta es una dirección no segura, se debe aceptar explícitamente la conexión. Estos pasos se muestran en la Figura 6.1.

<figure>
    <div align="center" width="80%">
        <img src="https://raw.githubusercontent.com/g-courses/jappy.rc/refs/heads/main/imgs/classroom/kernel01.png" alt=""/>
        <br />
        <figure-caption>Figura 6.1 Pasos iniciales para seleccionar un kernel en el contenedor.</figure-caption>
    </div>
</figure>

<br />

 Luego de aceptar la conexión no segura, se puede cambiar el nombre que VS Code usará para referenciar el servidor jupyter. En la Figura 6.2, muestra que el nombre por omisión `localhost` se cambia a uno más representativo, como `jappy_server`.

<figure>
    <div align="center" width="100%">
        <img width="80%" src="https://raw.githubusercontent.com/g-courses/jappy.rc/refs/heads/main/imgs/classroom/kernel02.png" alt=""/>
        <br />
        <figure-caption>Figura 6.2 Cambio del nombre lógico del servidor jupyter del contenedor.</figure-caption>
    </div>
</figure>

<br />

Finalmente, se selecciona el kernel a utilizar.

<figure>
    <div align="center" width="80%">
        <img width="80%" src="https://raw.githubusercontent.com/g-courses/jappy.rc/refs/heads/main/imgs/classroom/kernel03.png" alt=""/>
        <br />
        <figure-caption>Figura 6.3 Selección del kernel que se utilizará en el cuaderno jupyter.</figure-caption>
    </div>
</figure>

Una vez finalizado esto pasos, los otros kernels se pueden seleccionar escogiendo el servidor `jappy_server` creado.

</details>

## Anexos

## A) Arquitectura de desarrollo

<details>
<summary>Mostrar</summary>

La arquitectura que se desarrolló tiene por objetivo permitir a las personas que están tomando el ramo de Programación II tengan un ambiente de desarrollo coherente, de uso personal y que no efecte la calidad de las entregas de las tareas. Además, permite repasar conceptos y realizar ejercicios de programación.

La arquitectura de desarrollo se muestra en la Figura A1. Consiste en dos grandes bloques, representados por el Sistema Operatio nativo del computador, que se denomina **Sistema Operativo anfitrión** y un Sistema Operativo que se carga sobre este último, llamado **Sistema Operativo invitado**. En el lado del anfitrión, se utiliza el programa de desarrollo `VS Code` y del sistema de virtualización `Docker`. Cuando se abre la carpeta donde reside el proyecto a través de VS Code, este programa busca un archivo de configuración con nombre `.devcontainer.json`. Si este archivo existe, llama a la extensión `DevContainers` (1). Esta extensión revisa la estructura y sintaxis de este archivo y si no tiene errores, invoca a Docker para que ejecute la imagen que se especifica en el archivo de configuración (2). La ejecución de una imagen en el sistema Docker implica que se genera un `contenedor` que ejecuta un sistema operativo en particular (3). En este caso, se levanta un Sistema Operativo Linux Ubuntu 20.04. Si bien no es la última versión de esta distribución, utilizarla no afecta el objetivo del ambiente de desarrollo.

Una vez que el Sistema Operativo del contenedor está operativo, el sistema Docker implementa un sistema que permite acceder a los archivos de la carpeta que se abrió para dar inicio al paso (1). Estas referencias permiten que el Sistema Operativo invitado pueda acceder a los archivos que están en el anfitrión (4).

Luego, el programa `VS Code` que se ejecuta en el anfitrión, inicia el proceso `VS Code server` en el Sistema Operativo invitado (5). Este servidor permite acceder a los archivos del proyecto, editarlo, modificarlos, crear otros archivos, ejecutarlos con las **Herramientas de desarrollo Nativas** que ya están instaladas en el contenedor. etc. El sistema Docker y el proceso VS Code Server permiten mantener la coherencia de los archivos.


<figure>
    <div align="center" width="100%">
        <img src="https://raw.githubusercontent.com/g-courses/jappy.rc/refs/heads/main/imgs/classroom/arq02.png" alt=""/>
        <br />
        <figure-caption>Figura A1. Arquitectura de desarrollo basada en VS Code y Docker.
        <figure-caption>
    </div>
</figure>


</details>

## B) Sofware instaladado (2025-19-01)

<details>
<summary>Mostrar</summary>

**Compiladores e intérpretes**

* Compilador C++17 g++ 9.4.0, GNU Make 4.2.1, Cmake 3.16.3
* openJDK 11
* Python 3.10

**Herramientas de desarrollo**

* Doxygen 1.9.1
* Mermaid 11.4.x

**Módulos de Python**

* Matplotlib 3.7.5
* Numpy 1.24.4
* Pandas 2.0.3
* Ployly 5.23.0

**Jupyter Server**

* Servidor Jupyter 4.1
* kernel ipydrawio 1.3.0
* kernel IPython 3.12.8
* kernel IJava 1.3.0
* kernel Cling-cpp17 0.15.3

**VS Code extensions**

* ms-python.python
* ms-toolsai.jupyter
* ms-vscode.cpptools-extension-pack
* lfm.vscode-makefile-term
* ms-vscode.makefile-tools
* redhat.java
* ms-toolsai.datawrangler
* bierner.markdown-mermaid

</details>