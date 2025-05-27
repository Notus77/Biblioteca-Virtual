from datetime import datetime

def registrar_log(mensagem):
    with open("Logs.txt", "a", encoding="utf-8") as arquivo:
        data_hora = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        arquivo.write(f"{data_hora} {mensagem}\n")


registrar_log('[V1.2] - Terminamos o sistema, fizemos suporte,historico de compra,formas de pagamentos,algumas melhorias e importamos tudo para um arquivo chamado main')