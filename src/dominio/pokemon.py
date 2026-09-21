class Pokemon:
    def __init__(self,id_,nombre,tipo,ataque,hp,velocidad):
        self.id = id_
        self.nombre = nombre
        self.tipo = tipo
        self.ataque = ataque 
        self.hp = hp
        self.velocidad = velocidad

    def resumen(self):
        return f"#{self.id} {self.nombre} Tipo: {self.tipo} Ataque: {self.ataque} HP: {self.hp} Velocidad: {self.velocidad}"


    