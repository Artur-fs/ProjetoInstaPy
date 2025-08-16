import instaloader
from getpass import getpass

# 1. Crie a instância do Instaloader
L = instaloader.Instaloader()

# 2. Peça as credenciais
usuario = input("Digite seu nome de usuário do Instagram: ")
# Lembre-se: Digite a senha e pressione Enter. É normal não aparecer nada.
senha = getpass("Digite sua senha: ")

print("\nTentando fazer login...")

try:
    # 3. Tente fazer o login
    L.login(usuario, senha)
    print("Login bem-sucedido! A sessão foi salva.")

# 4. Tratamento de erros comuns
except instaloader.exceptions.TwoFactorAuthRequiredError:
    print("Sua conta tem Autenticação de Dois Fatores (2FA) ativada.")
    # O Instaloader vai pedir o código 2FA automaticamente no terminal.
    # Digite o código de 6 dígitos do seu app autenticador e pressione Enter.
    # Esta parte é gerenciada pelo próprio Instaloader após a exceção.
    # Em versões mais recentes, ele pode nem gerar exceção e pedir direto.
    codigo_2fa = input("Digite o código 2FA de 6 dígitos: ")
    L.two_factor_login(codigo_2fa)
    print("Login com 2FA bem-sucedido!")

except instaloader.exceptions.BadCredentialsException:
    print("Erro: Usuário ou senha incorretos. Verifique e tente novamente.")

except Exception as e:
    print(f"\nOcorreu um erro inesperado. Pode ser uma verificação de segurança.")
    print(f"Erro detalhado: {e}")
    print("\n--> AÇÃO RECOMENDADA: Abra seu app do Instagram no celular e veja se há algum aviso de segurança para aprovar o login.")
