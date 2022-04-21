import ply.lex as lex

tokens =(
    'AT_AK47', #A19
    'AT_PISTOL',  #P19
    'AT_HAND_GRANADE', #H19
    'KNIFE_KNIFE', #K19+K10
    'KNIFE_PISTOL', #K19+P10
    'KNIFE_AK47',  #K19+A10
    'KNIFE_HAND_GRANADE', #K19+H10
    'AV_AK47', #A70
    'AV_KNIFE', #K70
    'AV_PISTOL', #P70
    'AV_HAND_GRANADE', #H70
    'RIGHT', #R50
    'BACK', #B75
    'LEFT', #L100
    'GO', #POWER PLAYER <=0
    'EO', # ENEMY POWER <= 0
    'ELSE', #SIGUE ATACANDO SI NO ME MUEVO
)


# Definición de tokens simples:
t_AT_AK47= r'A19'
t_AT_PISTOL= r'P19'

t_AT_HAND_GRANADE = r'H19'
t_KNIFE_KNIFE = r'K19K10'
t_KNIFE_PISTOL = r'K19P10'
t_KNIFE_AK47 = r'K19A10'
t_KNIFE_HAND_GRANADE= r'K19H10'
t_AV_AK47 = r'A70'
t_AV_KNIFE = r'K70'
t_AV_PISTOL = r'P70'
t_AV_HAND_GRANADE = r'H70'
t_RIGHT = r'R50'
t_BACK = r'B75'
t_LEFT = r'L100'
#'GO', #POWER PLAYER <=0
#'EO', # ENEMY POWER <= 0
#'ELSE', #SIGUE ATACANDO SI NO ME MUEVO

# Definición de tokens que incluye código para
# complementar, por ejemplo, para la definición de número,
# se incluye su conversión a entero (para este caso):


# Paso 3. Crear el objeto tipo lex (el tokenizador)
lexer = lex.lex()


#paso 4 
action=input('-> ')
lexer.input(action)


print(lexer)
for tok in lexer:
    print(tok)
