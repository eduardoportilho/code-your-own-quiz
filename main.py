# -*- coding: latin-1 -*-
lacuna = '_____'
lacuna_selecionada = '[_____]'

todas_frases = [
  'O Brasil foi descoberto por {lacuna} em 22 de abril de {lacuna}. Sua capital é {lacuna} e seu esporte mais popular é o {lacuna}.',
  'A Suécia é um país nórdico que faz parte da {lacuna}. Sua capital é {lacuna} e ela faz fronteira ao sul com a {lacuna}, à oeste com a {lacuna} e a noroeste com a {lacuna}.',
  'Zanzibar é nome dado ao conjunto de duas ilhas na costa da {lacuna}. As duas ilhas são chamadas {lacuna} e {lacuna} e estão separadas do continente pelo Canal de Zanzibar.'
]

todas_respostas = [
  ['Pedro Álvares Cabral', '1500', 'Brasília', 'futebol'],
  ['Escandinávia', 'Estocolmo', 'Dinamarca', 'Noruega', 'Finlândia'],
  ['Tanzânia', 'Unguja', 'Pemba', 'Canal de Zanzibar']
]

def pergunta_dificuldade():
  """Pergunta ao usuário a dificuldade e retorna o índice correspondente."""
  dificuldade = raw_input('> Selecione um grau de dificuldade (fácil, médio ou difícil):\n')
  while True:
    if dificuldade == 'fácil':
      return 0
    elif dificuldade == 'médio':
      return 1
    elif dificuldade == 'difícil':
      return 2
    else:
      dificuldade = raw_input('> Opção inválida, tente novamente.\n')

def obtem_frase_e_respostas(dificuldade):
  """Obtém a frase e a lista de respostas para a dificuldade informada.

  Args:
        dificuldade (int): Indice da dificuldade selecionada pelo usuário.

  Returns:
        str: Frase com lacunas.
        list: Lista com as respostas para cada lacuna.
  """
  return todas_frases[dificuldade].format(lacuna=lacuna), todas_respostas[dificuldade]

def pergunta_resposta(frase, resposta):
  """Pergunta ao usuário a resposta para a primeira lacuna da frase.

  Args:
        frase (str): Frase que será exibida para o usuário.
        resposta (str): Resposta correta.

  Returns:
        bool: True caso o número de tentativas tiver sido esgotado.
        str: Frase com a lacuna substituida pela resposta.
  """
  nova_frase = frase.replace(lacuna, lacuna_selecionada, 1)
  print("\n***\n\n" + nova_frase)
  tentativas = 3
  while tentativas > 0:
    resposta_usuario = raw_input('\n> Qual o conteúdo da lacuna selecionada?\n')
    if resposta_usuario.lower() == resposta.lower():
      nova_frase = nova_frase.replace(lacuna_selecionada, resposta)
      print('👍   Muito bem, você acertou!')
      return False, nova_frase
    else:
      print('👎   Sua resposta está incorreta, tente novamente.')
      tentativas -= 1
  print('Número de tentativas esgotado! ☹ ☹ ☹️')
  return True, frase


def inicia_jogo(dificuldade):
  """Inicia o jogo com a dificuldade informada.

  Args:
        dificuldade (int): Indice da dificuldade selecionada pelo usuário.
  """
  frase, respostas = obtem_frase_e_respostas(dificuldade)

  for resposta in respostas:
    tentativas_esgotadas, frase = pergunta_resposta(frase, resposta)
    if tentativas_esgotadas:
      return

  print('\n***\n\nVocê acertou tudo!   😀 😀 😀\nA frase completa é: {0}'.format(frase))


dificuldade = pergunta_dificuldade()
inicia_jogo(dificuldade)