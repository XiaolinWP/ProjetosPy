# 1. Definindo as váriaveis 
nome_magia = "Bola de fogo"
dano_base = 10
nivel_mago = 5
bonus_dano = 4

# 2. Definindo as funções 
def calcular_dano_base(dano, nivel):
    total_dano = dano * nivel
    return total_dano

def aplicar_bonus(total_dano, bonus_dano):
    dano_total = total_dano + bonus_dano
    return dano_total
    
def gerar_log_combate(nome_magia, dano_total):
    log_combate = f"Você usou {nome_magia} e seu dano foi {dano_total}"
    return log_combate

dano_inicial = calcular_dano_base(dano_base, nivel_mago)
dano_final = aplicar_bonus(dano_inicial, bonus_dano)

print(gerar_log_combate(nome_magia, dano_final))