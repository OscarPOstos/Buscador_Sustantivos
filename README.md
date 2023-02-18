## Buscador de sustantivos

Este proyecto trata de un lector de documentos txt donde resaltará en pantalla aquellas palabras que sean identificadas como sustantivo

### Link a la aplicación

[Aplicación](https://oscarpostos-buscador-sustantivos-app-xexho0.streamlit.app/)

### Funcionamiento de la aplicación

Aqui iremos explicando parte por parte como usar esta aplicación, pero lo primero será explicar el formato de texto permitido

#### Texto permitido

Lo primero es que la aplicación solo permite documentos txt, pero no cualquier documento txt, sino uno cuyo contenido respete esta estructura

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/a74bc542d0bffc008778e1aa33a7233578dc8a5e886547a6.png)

la estructura la compone un titulo, una noticia y el resumen y deben estar separadas con 1 salto de linea como se ve en el ejemplo o sino no será capaz de detectar la estructura correctamente.

#### Como usar la aplicación

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/790dccdbc4b8891547c4c86bb14017b5688124071a468744.png)

Lo primero que podemos notar es que tenemos un botón para subir un archivo por lo que una vez hagamos click, tendremos el típico buscador de archivos, elegimos un archivo y ya estará cargado en nuestra pagina y habra encontrado los sustantivos de cada seccion del documento

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/2520a6401be63da460569fd5489c89609a279db414b0778c.png)

Una vez con el resultado cargado, tendremos 3 checkbox que nos permitirá visualizar una parte de la sección, si desactivamos titulo y resumen, solo se nos mostrará la sección noticia con los sustantivos remarcados

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/e3f8e302fd79d7dff0cb0695d2ce27269a4c1d91402e70f3.png)

y con eso tendriamos el como usar la pagina correctamente

#### Que pasa si mi documento no sigue la estructura correcta

Saltaría este mensaje de error

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/54c6fa4f8000b86d490fc956e2f9a80a4c0b7c20c14312ee.png)

### Conclusion

Este proyecto sería solo como introducción a lo que sería el PLN en este caso la indexacion y el analisis lexico de las palabras
