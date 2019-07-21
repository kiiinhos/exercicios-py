class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
 
    def get_nome(self):
        return self.nome
     
    def get_idade(self):
        return self.idade

class Pet:
    def __init__(self,pet_nome,nome_dono,data_nascimento):
        self.pet_nome= pet_nome
        self.nome_dono= nome_dono
        self.data_nascimento= data_nascimento
    def get_pet_nome(self):
        return self.pet_nome
    def get_nome_dono(self):
        return self.nome_dono
    def get_data_nascimento(self):
        return self.data_nascimento


pessoa = Pessoa('Marcos','25')

print(pessoa.get_nome(), pessoa.get_idade())

animal = Pet('Sky','Luis','02/12/2018')
print(animal.get_pet_nome(),animal.get_nome_dono(), animal.get_data_nascimento())