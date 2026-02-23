class Auth:
  def __init__(self, user, passkey):
   self.user = user
   self.passkey = passkey
  
  def checar_login(self):
    if self.user == 'neymar@mail.com':
      print('Agora digite a sua senha. ')
    else:
      print('Usuario nao cadastrado')

  def checar_senha(self):
    if self.passkey == 'peixao123':
      print(f'Pra finalizar, confirme o seu login usando o codigo que enviamos para o seu email {self.user}. ')
    else:
      print('Senha incorreta!')

class TwoFa(Auth):
  def __init__(self, user, passkey, twofa):
    super().__init__(user, passkey)
    self.twofa = twofa

  def checar_2steps(self):
   if self.twofa == '1S0FV7':
     print('Acesso liberado!, seja bem vindo')
   else:
     print('Acesso negado!')

login1 = TwoFa ('neymar@mail.com', 'peixao123', '1S0FV7')

login1.checar_login()
login1.checar_senha()
login1.checar_2steps()


