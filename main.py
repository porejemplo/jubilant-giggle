from neo4j import GraphDatabase

class neo:

	def __init__(self, uri, user, password):
		self.driver = GraphDatabase.driver(uri, auth=(user, password))

	def close(self):
		self.driver.close()

	def run(self, queri):
		with self.driver.session() as session:
			greeting = session.run(queri)
			for x in greeting:
				print(x)


if __name__ == "__main__":
	greeter = neo("bolt://localhost:7687", "neo4j", "neo4j")
	a = 0
	while a != -1:
		a = int(input("Indica que query quieres ver (pulsa -1 para salir): "))
		if a == 1:
			nombre = input("Nombre de la persona de la query: ")
			greeter.run("MATCH (t:persona{name: '"+ nombre +"'})-[:amistad | familia]-(p:persona) RETURN DISTINCT p;")
			#Obtener los amigos y familiares de un usuario determinado

		if a == 2:
			nombre = input("Nombre de la persona de la query: ")
			greeter.run("MATCH(a:persona {name: '"+ nombre +"'})-[f:familia]-(s) MATCH (s)-[m:familia]-(n) where n.name <> '"+ nombre +"'return n")
			#Obtener los familiares de los familiares de un usuario determinado.
		if a == 3:
			nombre1 = input("Nombre de la primera persona: ")
			nombre2 = input("Nombre de la segunda persona: ")
			greeter.run("MATCH (a:persona{name:'"+ nombre1 +"'})-[m:Mensaje]-(b:persona{name:'" + nombre2 + "'}) RETURN m") 
            #Obtener todos los mensajes enviados de un usuario determinado a otro usuario
            #determinado después de una fecha especificada
		if a == 4:
			nombre1 = input("Nombre de la primera persona: ")
			nombre2 = input("Nombre de la segunda persona: ")
			greeter.run("MATCH(a:persona {name: '"+ nombre1 +"'})-[f:Mensaje]->(n:persona{name:'" + nombre2 + "'}) WHERE f.fecha > date({year:2020, week:10, dayOfWeek:3}) return f")
			#Obtener la conversación completa entre dos usuarios determinados.
		if a == 5:
			nombre = input("Nombre de la persona de la query: ")
			greeter.run("MATCH (a:persona {name: '"+ nombre +"'})-[:trabaja]-(:empresa)-[:trabaja]-(b:persona) WHERE (a)-[:publica]-(:publicacion)-[:menciona]-(b) RETURN DISTINCT b")
            #Obtener todos los usuarios mencionados por un usuario determinado los cuales
            #tengan una relación laboral con el usuario que los mencionó.
		if a == 6:
			nombre = input("Nombre de la persona de la query: ")
			num = input("Num maximo de relaciones")
			greeter.run("MATCH(a:persona{name: '"+ nombre +"'})-[:amistad|familia]-(b:persona)-[:amistad|familia*.." + num + "]-(c:persona), p = shortestPath((a)-[:amistad|familia*.." + num + "]-(c)) WHERE NOT (a)-[:amistad|familia]-(c) AND a.name<>c.name RETURN distinct a.name AS Primero, b.name AS Segundo, c.name AS Tercero, length(p) AS saltos ORDER BY saltos DESC;")
			#Obtener los usuarios (terceros) que, no teniendo relación con un usuario
            #determinado (primero), tengan alguna relación en uno o varios saltos de relación
            #con los usuarios (segundos) que tienen relación con el usuario determinado. Se
            #podrá definir el número de saltos máximo en la consulta. En la consulta se
            #mostrará el usuario segundo del que parte la relación con los terceros y el
            #número de saltos de relación entre dichos usuarios y se ordenará por número de
            #saltos.
		if a == 7:
			nombre = input("Nombre de la persona de la query: ")
			greeter.run("MATCH(a:persona{name: '"+ nombre +"'})-[:amistad|familia]-(b:persona)-[:amistad|familia]-(c:persona) OPTIONAL MATCH (a)-[m:Mensaje]-(b) OPTIONAL MATCH (b)-[n:Mensaje]-(c) WHERE NOT (a)-[:amistad|familia]-(c) AND a.name<>c.name RETURN distinct a.name, count(distinct m), count(distinct n);")
			#Obtener los usuarios (terceros) que, no teniendo relación con un usuario
            #determinado(primero), tengan alguna relación con los usuarios (segundos) que
            #tienen relación con el usuario determinado. Solo se mostrarán las relaciones
            #entre usuarios que tengan más de un número especificado de mensajes. Ordenar
            #el resultado primero por el número de mensajes entre el primer usuario y los
            #segundos y después por el número de mensajes entre segundos y los terceros.	
	greeter.close()
