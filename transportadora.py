# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys
import easygui as eg

title = "Programa de controle de transportadora"

menu_entries = [ "Cadastro", "Pesquisa", "Operacao", "Relatorios", "Sair" ]

action = eg.choicebox("Escolha a opção desejada", title = title, choices = menu_entries)

if (action == "Cadastro"):
    cad_entries = [ "Localidades", "Filiais", "Funcionários", "Clientes", "Veículos", "Rotas", "Rodovias" ]
    cad_type = eg.choicebox("Escolha o tipo de cadastro", title = title, choices = cad_entries)
if (action == "Pesquisa"):
    pesq_entries = [ "Localidades", "Filiais", "Funcionários", "Clientes", "Veículos", "Rotas", "Rodovias" ]
    pesq_type = eg.choicebox("Escolha o tipo de pesquisa", title = title, choices = pesq_entries)
if (action == "Operacao"):
    op_entries = [ "Ordem serviço", "Viagens", "Carga/Descarga" ]
    op_type = eg.choicebox("Escolha o tipo de Operação", title = title, choices = op_entries)
if (action == "Relatorios"):
    rel_entries = [ "Veículos", "Clientes", "Funcionários" ]
    rel_type = eg.choicebox("Escolha o tipo de Relatorio", title = title, choices = rel_entries)
if (action == "Sair"):
    choice = eg.ynbox(msg = "Deseja realmente sair?", title = title, choices = ("Sim", "Não"), image = None)
    sys.exit(0)
