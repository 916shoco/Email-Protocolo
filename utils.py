import smtplib
import random
from email.message import EmailMessage

#Aqui e onde faço a conexao com o server SMTP nesse codigo abaixo esta meu email senha e tudo que vai ser explicado detalhadamante mais para frente
def enviar_email(destinatario, mensagem):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "yurimbrico@gmail.com"
    password = "qasmukwrhcephsae"
    
    #Aqui e o conteudo da mensagem (no meu caso recuperaçao de senha)
    msg = EmailMessage()
    msg.set_content(mensagem)
    msg['Subject'] = 'Recuperacao de senha'
    msg['From'] = sender_email
    msg['To'] = destinatario

    #aqui ele pega o email, senha, porta tudo que ja foi pedrefinido la em cima
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    server.login(sender_email, password)

    server.send_message(msg)

    server.quit()

def recuperar_senha():
    email = input("Digite o seu e-mail: ")

    # Verifica se o e-mail está cadastrado no banco de dados
    if email_existe_no_banco_de_dados(email):
        # Gera um código de recuperação
        codigo_recuperacao = gerar_codigo_recuperacao()

        # Envia o código de recuperação por e-mail
        enviar_email(email, f"Seu código de recuperação é: {codigo_recuperacao}")

        # Solicita ao usuário que digite o código recebido por e-mail
        codigo_digitado = input("Digite o código de recuperação enviado por e-mail: ")

        # Verifica se o código digitado está correto
        if codigo_digitado == codigo_recuperacao:
            nova_senha = input("Digite a nova senha: ")
            confirmacao_senha = input("Confirme a nova senha: ")

            # Verifica se as senhas coincidem
            if nova_senha == confirmacao_senha:
                # Atualiza a senha no banco de dados
                atualizar_senha_no_banco_de_dados(email, nova_senha)
                print("Senha atualizada com sucesso!")
            else:
                print("As senhas não coincidem. Tente novamente.")
        else:
            print("Código de recuperação incorreto. Tente novamente.")
    else:
        print("E-mail não encontrado. Verifique o e-mail digitado e tente novamente.")


def email_existe_no_banco_de_dados(email):
    return True

def gerar_codigo_recuperacao():
    return str(random.randint(100000, 999999))

def atualizar_senha_no_banco_de_dados(email, nova_senha):
    pass
