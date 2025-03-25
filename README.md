Programacion-ISTEA

La idea de este repositorio es subir los comandos que se vayan viendo en la cursada y ademas los ejercicios.

Unidad 1 INTRODUCCION A PYTHON Y A LA PROGRAMACION (Teoria)

PROGRAMA
Un programa informático o programa de computadora es una secuencia de instrucciones u órdenes basadas en un lenguaje de programación que una computadora interpreta para resolver un problema o una función específica.

LENGUAJE DE PROGRAMACION
Un lenguaje de programación es un conjunto de reglas gramaticales, que instruyen a que un ordenador o dispositivo se comporte de una cierta manera. Cada lenguaje de programación tiene un vocabulario, un conjunto único de palabras clave que sigue a una sintaxis especial para formar y organizar instrucciones del ordenador. 

LENGUAJES FORMALES
Un lenguaje formal tiene símbolos, letras y números. Y tienen reglas específicas para unir todos esos símbolos. Los símbolos son el alfabeto y las reglas, la sintaxis o la gramática. 

LENGUAJES NATURALES
Los lenguajes naturales están llenos de ambigüedades, puede haber palabras con diferentes significados. Al contrario, en los formales los símbolos están bien definidos y las reglas nos permiten crear enunciados con significados concretos. 

ALGORITMO: Es un conjunto de instrucciones ordenadas que permiten alcanzar un objetivo o resolver un problema

CARACTERISTICA DE LOS ALGORITMO
Entrada: Es el conjunto de datos iniciales que el algoritmo necesita para funcionar. 
Proceso: Son las operaciones o pasos que el algoritmo aplica a los datos de entrada para transformarlos. 
Salida: Es el resultado generado por el algoritmo tras completar el proceso.

TIPO LENGUAJES DE PROGRAMACION

LENGUAJE BAJO NIVEL: Los lenguajes de bajo nivel están estrechamente ligados al hardware de la computadora. Aunque pueden ser más difíciles de aprender y usar, ofrecen una velocidad y eficiencia superior debido a su proximidad al hardware.

CARACTERISTICAS
Dependencia de la máquina: Están diseñados para funcionar en una arquitectura de hardware específica.  
Alta eficiencia: Ofrecen un rendimiento rápido y óptimo al interactuar directamente con el hardware. 
Complejidad: Su uso requiere un conocimiento profundo de la estructura interna de la computadora.

LENGUAJE ALTO NIVEL: están diseñados para ser independientes del hardware. Esto significa que el mismo código puede ejecutarse en diferentes tipos de 
computadoras sin necesidad de modificaciones significativas. Estos lenguajes son más fáciles de aprender y usar, ya que sus instrucciones se asemejan más al lenguaje humano. 

CARACTERISTICAS
Independencia de la máquina: Pueden ejecutarse en múltiples plataformas sin cambios significativos. 
Facilidad de uso: Ofrecen una sintaxis más amigable y cercana al lenguaje humano, lo que facilita el aprendizaje y la escritura de código. 
Flexibilidad: Son adecuados para una amplia gama de aplicaciones, desde desarrollo web hasta inteligencia artificial.

Estos lenguajes suelen requerir la traducción a lenguaje de máquina para ser ejecutados, lo que se realiza mediante dos procesos principales

Compilación:  El código fuente se traduce completamente antes de su ejecución, generando un archivo binario (por ejemplo, un archivo .exe en Windows). Este archivo puede distribuirse y ejecutarse sin necesidad del código fuente original. El compilador es el programa que realiza esta traducción, permitiendo que el código sea ejecutado directamente por la máquina. 

Interpretación: El código fuente se traduce línea por línea durante su ejecución. Este método permite una mayor flexibilidad, ya que los cambios en el código pueden probarse de inmediato. El intérprete es el programa que ejecuta el código directamente, traduciéndolo a medida que se necesita.

COMPARACION ENTRE COMPILADOR E INTERPRETACION

![image](https://github.com/user-attachments/assets/b286e2c2-b6e9-47fd-8a4c-04e0178a2801)


Python: es un lenguaje de programación de alto nivel, interpretado, orientado a objetos, de código abierto, y de uso generalizado con semántica dinámica. Se utiliza ampliamente para la programación de propósito general, abarcando desde desarrollo web hasta análisis de datos, inteligencia artificial, automatización en servidores y más.

Comando para saber que versión de Python esta instalada
Windows: Python –version
MAC y Linux: python3 –versión

Errores en Python

1. Ubicación exacta del error: Python nos indica la línea específica donde se ha producido el error, lo cual nos ayuda a localizarlo rápidamente.
2. El trace (o traza): Este es el recorrido que hace el código a través de diferentes partes del programa hasta llegar al error. En un programa simple, la traza puede no ser muy relevante, y puedes ignorarla por ahora, ya que generalmente será vacía o no tan útil para entender el problema. 
3. Detalles de la ubicación: El mensaje de error incluirá el nombre del archivo donde se ha producido el error, el número de línea correspondiente y, en algunos casos, el nombre del módulo. Nota importante: El número de línea que Python muestra no siempre coincide exactamente con la ubicación del error real, ya que Python señala la primera línea donde detecta el efecto del error, no necesariamente el lugar exacto donde ocurrió. 
4. La línea de código con el error: Python mostrará la línea de código que ha causado el problema, e intentará marcarla con un símbolo ^ debajo del lugar donde detecta el error. Sin embargo, ten en cuenta que esta marca no siempre es precisa, especialmente en casos de errores complejos. 
5. Descripción del error: Python también nos dará el nombre del error y una breve explicación del problema. En algunos casos, también puede ofrecer sugerencias o soluciones que pueden ayudar a resolver el inconveniente.

