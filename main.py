import re
import celular
from utils import enviar_email, email_existe_no_banco_de_dados, gerar_codigo_recuperacao, atualizar_senha_no_banco_de_dados

def mostrar_mensagem(mensagem):
    print(mensagem)

def verifica_email(email):
    if not email:
        raise ValueError("Nenhum e-mail fornecido")
    
    if email.endswith("@gmail.com, @hotmail.com, @outlook.com") :
        return True
    else:
        raise ValueError("E-mail inválido")

# Cadastro de usuario
def cadastrar_novo_usuario():
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    
    try:
        if verifica_email(email):
            celular.cadastrar_usuario(email, senha)
            mostrar_mensagem("Usuário cadastrado com sucesso!")
    except ValueError as e:
        mostrar_mensagem(str(e))

# Sistema de login
def logar_usuario():
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    usuario = celular.buscar_usuario(email)
    if usuario and usuario[1] == senha:
        mostrar_mensagem("Login realizado com sucesso!")
    else:
        mostrar_mensagem("Email ou senha incorretos.")

# Recuperar senha 
def recuperar_senha():
    email = input("Digite seu email: ")
    usuario = celular.buscar_usuario(email)
    if usuario:
        codigo = gerar_codigo_recuperacao()
        enviar_email(email, f"Seu código de verificação é: {codigo}")
        codigo_digitado = input("Digite o código de verificação enviado para seu email: ")
        if codigo_digitado == codigo:
            nova_senha = input("Digite sua nova senha: ")
            confirmacao_senha = input("Confirme sua nova senha: ")
            if nova_senha == confirmacao_senha:
                atualizar_senha_no_banco_de_dados(email, nova_senha)
                mostrar_mensagem("Senha alterada com sucesso!")
            else:
                mostrar_mensagem("As senhas não coincidem. Tente novamente.")
        else:
            mostrar_mensagem("Código incorreto. Tente novamente.")
    else:
        mostrar_mensagem("Email não cadastrado.")

# Opções do console
def main():
    celular.criar_tabela()
    
    while True:
        print("\n1 - Cadastrar novo usuário")
        print("2 - Login")
        print("3 - Recuperar senha")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_novo_usuario()
        elif opcao == '2':
            logar_usuario()
        elif opcao == '3':
            recuperar_senha()
        elif opcao == '4':
            break
        else:
            mostrar_mensagem("Opção inválida.")

if __name__ == "__main__":
    main()
