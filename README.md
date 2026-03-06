# JAPPY: Recurso educacional para realizar clases de programación en Java, C++ y Python


## 1) Implantación del contenedor de desarrollo

<details>
<summary>Mostrar</summary>

### 1.1) Software base

Los ejemplos y las tareas de la asignatura se realizarán utilizando `Jupyter Notebook` como herramienta de desarrollo y Docker como tecnología de infraestructura. Para lograr esto, en su computador deberá instalar:

* [Docker desktop](https://docs.docker.com/get-docker/)
* [GitHub CLI](https://github.com/cli/cli#installation) *(Opcional)*


### 1.2) Instalación del contenedor de desarrollo 


Para instalar el contenedor de desarrollo, es suficiente con el archivo`docker-compose.yml` y la carpeta `workspace` dentro de una carpeta. Este ejemplo muestra la obtención de estos archivos a través de la clonación de un repositorio determinado.

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


## 2) Uso del contenedor con Jupyter Lab

<details>
<summary>Mostrar</summary>

En este caso, el inicio y apagado del contenedor se realiza a través de la plataforma `Docker Compose`. Una vez que el contenedor se inicia, la herramientas de desarrollo se acceder a través de un servidor Jupyter Lab.

Partiendo del paso 2) de la sección 1.2), abra un terminal en la carpeta `jappy.classroom`. Luego, inicie el contenedor con el siguiente comando:

```
docker compose up -d
```

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

Para detener el contenedor, debe ingresar el siguiente comando:

```
docker compose down
```

<figure>
     <div align="center" width="80%">
        <img width="80%" src="https://raw.githubusercontent.com/g-courses/jappy.rc/refs/heads/main/imgs/classroom/jupyter05.png" alt=""/>
        <br />
        <figure-caption>Figura 2.4 Proceso de apagado del contenedor a través de Docker Compose.</figure-caption>
    </div>
</figure>

<br />

</details>

## 3) Prueba de funcionamiento del contenedor con Jupyter Lab

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


## 5) Selección de kernel

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

## Anexo: Sofware instaladado (2025-19-01)

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