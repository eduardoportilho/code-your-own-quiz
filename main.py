def obtem_dificuldade():
  dificuldade = raw_input('Selecione um grau de dificuldade (fácil, médio ou difícil):\n')
  while True:
    if dificuldade == 'fácil':
      return 0
    elif dificuldade == 'médio':
      return 1
    elif dificuldade == 'difícil':
      return 2
    else:
      dificuldade = raw_input('Opção inválida, tente novamente.\n')
