# TFG_3D
Este repositorio contiene el Proyecto de Final de Carrera del Grado de Ingeniería de Telecomunicaciones de Marc Caravaca en la Universidad Autònoma de Barcelona, España.


## Descripción

Implementación de una impresora 3D de resina mediante una raspberry pi 3 y un proyector. Este repositorio contiene únicamente las instrucciones y el codigo del sistema de proyeción de imágenes.

## Creado sobre Linux

He utilizado Raspberry Pi OS (Version XXX) para el proyecto. 

[![NPM Version][npm-image]][npm-url]
[![Build Status][travis-image]][travis-url]
[![Downloads Stats][npm-downloads]][npm-url]
[![Python Version][python-img]][npm-url]


### Dependencias

- Instala los últimos drivers
- Instala todo lo necesario:

``` $ sudo apt-get install cmake make g++ libx11-dev libxi-dev libgl1-mesa-dev libglu1-mesa-dev libxrandr-dev libxext-dev libxi-dev ```

### Puesta en Marcha

Antes si quiera de empezar a ejecutar el programa, debes realizar ciertos ajustes para que todo salga correctamente. Inicialmente debes configurar tu Raspberry Pi para que se inicialize en sin intezfaz, solo Consola de Texto. 

#### raspi-config

Abrimos una nueva termainal de consola y mediante el comando descrito a continuación, se abre la configuración del sistema.

```
$ sudo raspi-config
```

Buscamos la opción que controle el Boot, y seleccionamos la opción que más nos interese. En nuestro caso, como el objetivo es eliminar completamente la interfaz, seleccionaremos:

```
Console text console, no login required.
```

A continuación habilitaremos el acceso mediante ssh, pues la idea es no tener que interactuar con las raspberry. Así que buscamos en el menú inicial de raspi-config:

```
Interficie options -> SSH -> Enable
```
A continuación procederemos a eliminar toda la sequencia de inicio para realizar el "Silent Boot". 
Para eliminar la imagen de inicio accedemos al archivo de config.txt en boot:

```
$ sudo nano /boot/config.txt
```

Y añadimos al final:

```
disable_splash=1
```

Para eliminar los mensajes de Boot, lo que haremos será "camuflarlos", los enviaremos a la TTy número 6, modificando el cmdline.txt:

```
$ sudo nano /boot/cmdline.txt
```
y susbtituimos:

```
console=tty1
```

por:

```
console=tty6
```

De esta manera los mensajes no se mostraran en la TTY por defecto, aue es la 1, sinó que se mostrarán en la TTY6.

Sin salirnos de este archivo, añadimos al final:

```
 loglevel=3 quiet logo.nologo vt.global_cursor_default=0
```
de esta manera eliminamos warnings, el logo de raspberry y el cursor que parpadea.

Seguidos todos estos pasos, no deberí haber ningún elemento en pantalla, quedando el FrameBuffer libre para editarlo.

## Imagenes por pantalla



```

$ cd Assignment-01/external/glfw-3.0.3
$ cmake .
$ make all
$ cd ../..
$ mkdir build
$ cd build
$ cmake ..
$ make all
```




### 1. Priority Queue

The heuristic defined for vertex removal is described on pseudo-code as follows:

- Go through all the vertex and calculate their connection with others (edges)
- Store the edges on a 2D vector together with the 'index' of its vertex
- Sort the vector by the size of the edges (smallest first)
- Get the first position of the vector which contains the two vertex to be compared
- Verify which of the two vertex has more connections (v1) and choose to be removed


### 2. Half-Edge Collapse

The technique chosen for vertex removal was the *Half-Edge Collapse* which works removing a vertex and reconnecting all its connections to another vertex:


![Half-Edge Collapse](http://jcae.sourceforge.net/amibe-doc/org/jcae/mesh/amibe/ds/doc-files/AbstractHalfEdge-2.png)


Pseudo-code:

- Go to the vertex to be removed (v1 - defined on priority queue)
- Check all the vertex that are connected to that vertex
- Remove v1 and reconnect all its connections to v2  


## References


David Luebke, Benjamin Watson, Jonathan D. Cohen, Martin Reddy, and Amitabh Varshney. 2002. *Level of Detail for 3D Graphics*. Elsevier Science Inc., New York, NY, USA.

OpenGL Tutorials. *Tutorial 1: Opening a Window*, Available at: http://www.opengl-tutorial.org/beginners-tutorials/tutorial-1-opening-a-window/ (Accessed: 3rd April 2016).

Mesh Simplification. Standford course (CS 468-10-fall) Lecture Notes. Available on: http://graphics.stanford.edu/courses/cs468-10-fall/LectureSlides/08_Simplification.pdf

Shene, Ching-Kuang. *Mesh Simplification*. Classes notes. Michigan Technological University. Available on:
http://www.cs.mtu.edu/~shene/COURSES/cs3621/SLIDES/Simplification.pdf

[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki
[python-img]: https://img.shields.io/pypi/pyversions/conda?style=flat-square
