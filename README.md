# Ampliación de Bases de Datos - Neo4j
El ejercicio consta de 2 partes, en la primera creamos una base de datos en la que se simularán las conexiones entre usuarios de una red social, los mensajes que intercambian, centros de educación y lugares de trabajo.

Por otro lado había que realizar las siguientes búsquedas:
1. Obtener los amigos y familiares de un usuario determinado.
2. Obtener los familiares de los familiares de un usuario determinado.
3. Obtener todos los mensajes enviados de un usuario determinado a otro usuario determinado después de una fecha especificada.
4. Obtener la conversación completa entre dos usuarios determinados.
5. Obtener todos los usuarios mencionados por un usuario determinado los cuales tengan una relación laboral con el usuario que los mencionó.
6. Obtener los usuarios (terceros) que, no teniendo relación con un usuario determinado (primero), tengan alguna relación en uno o varios saltos de relación con los usuarios (segundos) que tienen relación con el usuario determinado. Se podrá definir el número de saltos máximo en la consulta. En la consulta se mostrará el usuario segundo del que parte la relación con los terceros y el número de saltos de relación entre dichos usuarios y se ordenará por número de saltos.
7. Obtener los usuarios (terceros) que, no teniendo relación con un usuario determinado(primero), tengan alguna relación con los usuarios (segundos) que tienen relación con el usuario determinado. Sólo se mostrarán las relaciones entre usuarios que tengan más de un número especificado de mensajes. Ordenar el resultado primero por el número de mensajes entre el primer usuario y los segundos y después por el número de mensajes entre segundos y los terceros.
