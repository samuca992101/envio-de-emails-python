import smtplib
from email.mime.text import MIMEText

def enviar_email(destinatario, assunto, corpo):
    remetente = "sbrasileiro4@gmail.com"
    senha = "xtlu qdwe yhng uock"

    # Configurar a mensagem
    mensagem = MIMEText(corpo)
    mensagem['Subject'] = assunto
    mensagem['From'] = remetente
    mensagem['To'] = destinatario

    # Conectar ao servidor SMTP
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
            servidor.starttls()
            servidor.login(remetente, senha)
            servidor.send_message(mensagem)
            print("E-mail enviado com sucesso!")
    except Exception as e:
        print("Erro ao enviar e-mail:", e)

# Teste
if __name__ == "__main__":
    enviar_email("destinatario@gmail.com", "Assunto Teste", "Corpo do e-mail")


enviar_email("sbrasileiro82@gmail.com", "Teste Script", "Testando meu código de automação de e-mail.")
