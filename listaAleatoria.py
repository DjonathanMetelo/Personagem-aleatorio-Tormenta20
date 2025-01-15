import random


def reacas():
    racas = [ 'Anão', 'Bugbear', 'Centauro', 'Ceratops', 'Dahllan', 'Elfo', 'Elfo-do-Mar', 'Finntroll', 'Gnoll',
              'Goblin', 'Golem', 'Harpia', 'Hobgoblin','Humano', 'Hynne', 'Kaijin', 'Kallyanach', 'Kappa', 'Kliren',
              'Kobolds', 'Lefou', 'Mashin', 'Medusa', 'Meio-Orc', 'Minauro', 'Minotauro', 'Moreau', 'Nagah', 'Nezumi',
              'Ogro', 'Orc', 'Osteon', 'Pteros', 'Qareen', 'Sereia/Tritão', 'Silfide', 'Suraggel', 'Tabrachi', 'Tengu',
              'Trog', 'Velocis', 'Voracis', 'Yidishan']

    subracas_map = {
        'Moreau': ['Bufalo', 'Coelho', 'Coruja', 'Crocodilo', 'Gato', 'Hiena', 'Leão', 'Lobo', 'Morcego', 'Raposa',
                   'Serpente', 'Urso']
        , 'Suraggel': ['Aggelus', 'Sulfure']
        , 'Osteon': ['Comum', 'Soterrado']
        , 'Trog': ['Comum', 'Anão']
        , 'Golem': ['Comum', 'Barro', 'Bronze', 'Carne', 'Espelhos', 'Ferro', 'Gelo Eterno', 'Pedra', 'Sucata']
    }

    race = random.choice(racas)

    if race in subracas_map:
        race = race + ' ' + random.choice(subracas_map[race])

    return race


def trabalhos():
    classes = ['Arcanista', 'Barbaro', 'Bardo', 'Bucaneiro', 'Cavaleiro' , 'Caçador', 'Clerigo', 'Druida', 'Guerreiro',
               'Inventor', 'Ladino', 'Lutador', 'Nobre', 'Paladino']

    subclasses_map = {
        'Arcanista': ['(Bruxo)', '(Feiticeiro: Linhagem Draconica)',  '(Feiticeiro: Linhagem Feerica)',
                      '(Feiticeiro: Linhagem Rubra)', '(Mago)']
        , 'Clerigo': ['(Aharadak)', '(Allihana)', '(Arsenal)', '(Azgher)', '(Hyninn)', '(Kally)', '(Khalmyr)',
                      '(Lena)', '(Lin-wu)', '(Marah)', '(Megalokk)', '(Nimb)', '(Oceano)', '(Panteão)', '(Sszzaas)',
                      '(Tanna-Toh)', '(Tenebra)', '(Thwor)', '(Thyatis)', '(Valkaria)', '(Wynna)']
        , 'Druida': ['(Allihana)', '(Megalokk)', '(Oceano)']
        , 'Inventor': ['(Alquimista)', '(Armeiro)', '(Cozinheiro)', '(Engenhoqueiro)']
        , 'Paladino': ['(Azgher)', '(Do bem)', '(Khalmyr)', '(Lena)', '(Lin-wu)', '(Marah)', '(Tanna-Toh)',
                       '(Thyatis)', '(Valkaria)']

    }

    jobs = random.choice(classes)

    if jobs in subclasses_map:
        jobs = jobs + ' ' + random.choice(subclasses_map[jobs])

    return jobs

def origem():

    origens = ['Acolito', 'Agricultor Sambur', 'Amazona de Hippion', 'Amazona de Hippion', 'Amigo dos Animais',
               'Amnésico', 'Amoque Púrpura', 'Anão de Armas', 'Andarilho Ubaneri', 'Aprendiz de Dragoeiro',
               'Aprendiz de Drogadora', 'Aristocrata Daizenshi', 'Aristocrata', 'Armeiro Armado', 'Artesão', 'Artista',
               'Aspirante a Herói', 'Assistente de Laboratório', 'Assistente Forense', 'Bandoleiro da Fortaleza',
               'Barão Arruinado', 'Capanga', 'Catador da Cidade Velha', 'Cativo das Fadas', 'Charlatão', 'Circense',
               'Competidor do Circuito', 'Cosmopolita', 'Cria da Favela', 'Criado pelas Voracis', 'Criminoso',
               'Curandeiro', 'De Outro Mundo', 'Descendente Colleniano', 'Desertor da Supremacia', 'Duplo Feérico',
               'Duyshidakk Infiltrado', 'Emissario Ubaneri', 'Eremita', 'Escravo', 'Escudeiro da Luz',
               'Escudeiro Solitário', 'Estandarte Vivo', 'Estudante da Academia Arcana', 'Estudante do Colégio Real',
               'Estudioso', 'Explorador de Ruínas', 'Fazendeiro', 'Filhote da Revoada', 'Forasteiro', 'Futura Lenda',
               'Ginete de Tumarkhân', 'Gladiador', 'Grumete Pirata', 'Guarda', 'Guardião Glacial', 'Herdeiro',
               'Heroi Camponês', 'Iniciado dos Caça-Monstros', 'Insurgente Tapistano', 'Irmão sem Esporas', 'Legionario',
               'Lenhador de Tollon', 'Liricista de Lenórienn', 'Marujo', 'Mateiro', 'Membro de Guilda',
               'Membro do Principado', 'Mercador', 'Minerador', 'Nitamuraniano', 'Nobre Zakharoviano', 'Nômade Sar-Allan',
               'Nômade', 'Pescador Parrudo', 'Pivete', 'Plebeu Arcano', 'Prisioneiro das Catacumbas',
               'Procurado: Vivo ou Morto', 'Profeta do Akzath', 'Querido Filho', 'Rebelde Agitador', 'Receptador das Nuvens',
               'Recruta Arcano', 'Recruta da Fênix', 'Refugiado', 'Sábio Matemático', 'Seguidor', 'Selvagem Sanguinário',
               'Selvagem', 'Soldado', 'Sucateiro de Batalhas', 'Tamalu', 'Taverneiro', 'Tocado pela Dama Altiva',
               'Tocado pelo Indomavel', 'Trabalhador', 'Tradicionalista Svalano', 'Trapaceiro Ahleniense',
               'Turista da Academia Arcana', 'Um com os Kami']

    ori = random.choice(origens)

    return ori

def genero ():

    generos = ['♀', '♂']

    gen = random.choices(generos)

    return gen

def personagem ():

    itemracas = reacas()
    itemclasses = trabalhos()
    itemorigens = origem()
    itemsgenero = genero()

    print(f"Raça: {itemracas}")
    print(f"Gênero: {itemsgenero[0]}")
    print(f"Origem: {itemorigens}")
    print(f"Classe: {itemclasses}")


personagem()