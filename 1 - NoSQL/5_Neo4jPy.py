from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "newpw"))

def create_person(tx,name, age):
    return tx.run("MERGE (a:Person {name:$name, age:$age}) "
                           "RETURN id(a)", name=name, age= age)

def get_age(tx,name):
    for record in tx.run("MATCH (a:Person) WHERE a.name = $name "
                          "RETURN a.age", name=name):
        print(record["a.age"])

def relate_person(tx,name, anothername):
    return tx.run("MATCH (a:Person),(b:Person) "
                          "WHERE a.name = $name AND b.name = $anothername "
                            "MERGE (a)-[r:KNOWS]->(b) "
                            "RETURN r", name=name, anothername=anothername)

def update_age(tx,name, value):
    return tx.run("MATCH (a:Person) "
                          "WHERE a.name = $name "
                          "Set a.age = $value "
                          "RETURN id(a)", name=name, value=value)

def delete_person(tx,name):
    return tx.run("MATCH (a:Person) "
                  "WHERE a.name = $name "
                  "DETACH DELETE a "
                  ,name=name)


with driver.session() as session:
    session.read_transaction(create_person,"Hubert",52)
    session.read_transaction(get_age,"Hubert")
    session.read_transaction(create_person,"Agathe",43)
    session.read_transaction(get_age, "Agathe")
    session.read_transaction(relate_person,"Hubert", "Agathe")
    session.read_transaction(update_age, "Agathe", 48)
    session.read_transaction(get_age, "Agathe")
    session.read_transaction(delete_person,"Agathe")
    session.read_transaction(delete_person, "Hubert")