import random


def reacas():
    racas = ['Anão', 'Bugbear', 'Centauro', 'Ceratops', 'Dahllan', 'Elfo', 'Elfo-do-mar', 'Finntroll', 'Galokk',
             'Gnoll',
             'Goblin', 'Golem', 'Harpia', 'Hobgoblin', 'Humano', 'Hynne', 'Kaijin', 'Kallyanach', 'Kappa', 'Kliren',
             'Lefou', 'Mashin', 'Medusa', 'Meio-elfo', 'Meio-Orc', 'Minauro', 'Minotauro', 'Moreau', 'Nagah', 'Nezumi',
             'Ogro', 'Orc', 'Osteon', 'Pteros', 'Qareen', 'Sereira/Tritão', 'Silfide', 'Soterrado', 'Suraggel',
             'Tabrachi', 'Tengu', 'Trog', 'Velovis', 'Voracis', 'Yidishan']

    subracas_map = {
        'Moreau': ['Bufalo', 'Coelho', 'Coruja', 'Crocodilo', 'Gato', 'Hiena', 'Leão', 'Lobo', 'Morcego', 'Raposa',
                   'Serpente', 'Urso']
        , 'Suraggel': ['Aggelus', 'Sulfure']
    }

    race = random.choice(racas)

    if race in subracas_map:
        race = race + ' ' + random.choice(subracas_map[race])

    return race


def trabalhos():
    classes = ['Arcanista', 'Barbaro', 'Bardo', 'Bucaneiro', 'Cavaleiro' , 'Caçador', 'Clerigo', 'Druida', 'Guerreiro'
        , 'Inventor', 'Ladino', 'Lutador', 'Nobre', 'Paladino']

    subClasses_map = {
        'Arcanista': ['(Bruxo)', '(Feiticeiro: Linhagem Draconica)',  '(Feiticeiro: Linhagem Feerica)'
            , '(Feiticeiro: Linhagem Rubra)', '(Mago)']
        , 'Clerigo': ['(Aharadak)', '(Allihana)', '(Arsenal)', '(Azgher)', '(Hyninn)', '(Kally)', '(Khalmyr)'
            , '(Lena)', '(Lin-wu)', '(Marah)', '(Megalokk)', '(Nimb)', '(Oceano)', '(Panteão)', '(Sszzaas)'
            , '(Tanna-Toh)', '(Tenebra)', '(Thwor)', '(Thyatis)', '(Valkaria)', '(Wynna)']
        , 'Druida': ['(Allihana)', '(Megalokk)', '(Oceano)']
        , 'Inventor': ['(Alquimista)', '(Armeiro)', '(Cozinheiro)', '(Engenhoqueiro)']
        , 'Paladino': ['(Azgher)', '(Do bem)', '(Khalmyr)', '(Lena)', '(Lin-wu)', '(Marah)', '(Tanna-Toh)'
            , '(Thyatis)', '(Valkaria)']

    }

    jobs = random.choice(classes)

    if jobs in subClasses_map:
        jobs = jobs + ' ' + random.choice(subClasses_map[jobs])

    return jobs


origens = [ 'Acolito', 'Agricultor sambur', 'Amazona de Hippion', 'Amnesico', 'Aprendiz de Dragoeiro'
    , 'Aprendiz de drogadora', 'Aristocrata', 'Artesão', 'Artista', 'Assistente de Laboratorio', 'Batedor', 'Capanga'
    , 'Catador da Cidade Velha', 'Cativo das Fadas', 'Charlatão', 'Circense', 'Cosmopolita', 'Cria da Favela'
    , 'Criado pelas Voracis', 'Criminoso', 'Curandeiro', 'Desertor da Supremacia', 'Duplo feerico', 'Eremita'
    , 'Escravo', 'Estandarte Vivo', 'Estudante da Academia Arcana', 'Estudante do colegio real', 'Estudioso'
    , 'Explorador de ruina', 'Fazendeiro', 'Filhote da Revoada', 'Forasteiro', 'Ginete de Tumarkhân', 'Gladiador'
    , 'Grumete Pirata', 'Guarda', 'Guardião Glacial', 'Herdeiro', 'Heroi Camponês', 'Legionario', 'Lenhador de Tollon'
    , 'Marujo', 'Mateiro', 'Membro de Guilda', 'Mercador', 'Minerador', 'Nitamuraniano', 'Nômade', 'Pescador Parrudo'
    , 'Pivete', 'Recruta da fenix', 'Refugiado', 'Seguidor', 'Selvagem', 'Soldado', 'Sucateiro de Batalhas'
    , 'Taverneiro', 'Trabalhador']

genero = ['♀', '♂']

itemRacas = reacas()
itemClasses = trabalhos()
itemOrigens = random.choice(origens)
itemsGenero = random.choices(genero)

print(f"Raça: {itemRacas}")
print(f"Gênero: {itemsGenero[0]}")
print(f"Origem: {itemOrigens}")
print(f"Classe: {itemClasses}")