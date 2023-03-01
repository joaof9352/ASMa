def par_ou_impar(num: int):
    '''
        Retorna verdadeiro se for par
    '''
    return num%2 == 0

def media(lista: list):
    return sum(lista)/len(lista)

class Person:

    def __init__(self, primeiro_nome, ultimo_nome, idade, nacionalidade):
        self.primeiro_nome = primeiro_nome
        self.ultimo_nome = ultimo_nome
        self.idade = idade
        self.nacionalidade = nacionalidade

    def printfname(self):
        print(self.primeiro_nome)

class Student(Person):
    
    def __init__(self, first_name, last_name, age, nationality, course, academic_year):
        super().__init__(first_name, last_name, age, nationality)
        self.course = course
        self.academic_year = academic_year

phone_book = {
    'John': ['8592970000', ''],
    'Bob': ['7994880000', ''],
    'Tom': ['9749552647', '']
}

def imprimir_par_chave(nome: str):
    if nome in phone_book.keys():
        print(nome + ': ' + phone_book[nome]) 
