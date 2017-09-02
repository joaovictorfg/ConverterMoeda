#!/usr/bin/python
# -*- coding: iso-8859-1-*-

import os

while 1:
    os.system('clear')
    print '''Por favor Digite o número da opção desejada:
		1- Converter de real para euro digite 1 e aperte enter.
		2- Sair e aperte enter.'''
    opcao = int(raw_input('Digite aqui: '))
    if opcao == 1:
        real = float(raw_input('Qual o valor atual do real? '))
        valor = float(raw_input('Qual o valor atual do euro? '))
        total = real / valor
        print 'Seu valor em euro fica: R$ %.2f.' % total
        raw_input('Pressione qualquer tecla para continuar')

    if opcao == 2:
        print 'Encerrando.......'
        break
