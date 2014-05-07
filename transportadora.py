# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys
import easygui as eg
import MySQLdb

# connection
db = MySQLdb.connect("localhost", "root", "rapadura", "transportadora")

# create a cursor
cursor = db.cursor()

title = "Programa de controle de transportadora"

# show main menu
def showMenu():
   menu_entries = [ "Cadastro", "Pesquisa", "Operacao", "Relatorios", "Sair" ]
   action = eg.choicebox("Escolha a opção desejada", title = title, choices = menu_entries)
   while 1:
      # register
      if (action == "Cadastro"):
         cad_entries = [ "Localidades", "Filiais", "Funcionarios", "Clientes", "Veiculos", "Rotas", "Rodovias" ]
         cad_type = eg.choicebox("Escolha o tipo de cadastro", title = title, choices = cad_entries)
         if (cad_type == "Localidades"):
            sys.exit(0)
         if (cad_type == "Filiais"):
            sys.exit(0)
         if (cad_type == "Funcionarios"):
            cadFunc()
         if (cad_type == "Clientes"):
            sys.exit(0)
         if (cad_type == "Veiculos"):
            cadVei()
         if (cad_type == "Rotas"):
            sys.exit(0)
         if (cad_type == "Rodovias"):
            sys.exit(0)
         if (cad_type == None):
            sys.exit(0)
         
      # search
      if (action == "Pesquisa"):
         pesq_entries = [ "Localidades", "Filiais", "Funcionarios", "Clientes", "Veiculos", "Rotas", "Rodovias" ]
         pesq_type = eg.choicebox("Escolha o tipo de pesquisa", title = title, choices = pesq_entries)
         if (pesq_type == "Localidades"):
            sys.exit(0)
         if (pesq_type == "Filiais"):
            sys.exit(0)
         if (pesq_type == "Funcionarios"):
            pesqFunc()
         if (pesq_type == "Clientes"):
            sys.exit(0)
         if (pesq_type == "Veiculos"):
            pesqVei()
         if (pesq_type == "Rotas"):
            sys.exit(0)
         if (pesq_type == "Rodovias"):
            sys.exit(0)
         if (pesq_type == None):
            sys.exit(0)

      # operational
      if (action == "Operacao"):
         op_entries = [ "Ordem servico", "Viagens", "Carga/Descarga" ]
         op_type = eg.choicebox("Escolha o tipo de Operação", title = title, choices = op_entries)
         if (op_type == "Ordem servico"):
            sys.exit(0)
         if (op_type == "Viagens"):
            sys.exit(0)
         if (op_type == "Carga/Descarga"):
            sys.exit(0)
         if (op_type == None):
            sys.exit(0)

      # report
      if (action == "Relatorios"):
         rel_entries = [ "Veiculos", "Clientes", "Funcionarios" ]
         rel_type = eg.choicebox("Escolha o tipo de Relatorio", title = title, choices = rel_entries)
         if (rel_type == "Veiculos"):
            sys.exit(0)
         if (rel_type == "Clientes"):
            sys.exit(0)
         if (rel_type == "Funcionarios"):
            sys.exit(0)
         if (rel_type == None):
            sys.exit(0)

      # exit
      if (action == None) or (action == "Sair"):
         choice = eg.ynbox(msg = "Deseja realmente sair?", title = title, choices = ("Sim", "Não"), image = None)
         sys.exit(0)

# execute query
def execQuery(query):
   try:
      cursor.execute(query)
      db.commit()
      print "OK"
   except MySQLdb.Error, e:
      print "Error %d: %s" % (e.args[0], e.args[1])
      db.rollback()

# insert funcionario
def cadFunc():
   msg = "Informe dados do funcionario"
   fieldNames = [ "Nome", "Endereco", "Fone", "Data_Nascimento", "Classe", " Categoria" ]  
   fieldValues = []
   fieldValues = eg.multenterbox(msg, title, fieldNames)
   while 1:
      if fieldValues == None:
         break
      errmsg = ""
      for i in range(len(fieldNames)):
         if fieldValues[i].strip() == "":
            errmsg = errmsg + ('"%s" eh requerido'  % fieldNames[i])
      if errmsg == "":
         break
      fieldValues = eg.multenterbox(errmsg, title, fieldNames, fieldValues)
   if (fieldValues != None):
      funcionarios = "INSERT INTO Funcionarios(funNome, funEnder, funFone, funDtNasc, funClasse, funCateg) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (fieldValues[0], fieldValues[1], fieldValues[2], fieldValues[3], fieldValues[4], fieldValues[5])
      execQuery(funcionarios)

# insert veiculo
def cadVei():
   msg = "Informe dados do Veiculo"
   fieldNames = [ "Descricao", "Ano", "Placa", "Quilometragem", "categoria" ]  
   fieldValues = []
   fieldValues = eg.multenterbox(msg, title, fieldNames)
   while 1:
      if fieldValues == None:
         break
      errmsg = ""
      for i in range(len(fieldNames)):
         if fieldValues[i].strip() == "":
            errmsg = errmsg + ('"%s" eh requerido'  % fieldNames[i])
      if errmsg == "":
         break
      fieldValues = eg.multenterbox(errmsg, title, fieldNames, fieldValues)
   if (fieldValues != None):
      veiculos = "INSERT INTO Veiculos(veiDescr, veiAno, veiPlaca, veiKm, veiCateg) VALUES ('%s', '%d', '%s', '%d', '%s')" % (fieldValues[0], int(fieldValues[1]), fieldValues[2], int(fieldValues[3]), fieldValues[4])
      execQuery(veiculos)

# search Funcionario
def pesqFunc():
   msg = "Informe dados Funcionario"
   menu_entries = [ "Nome", "Endereco", "Fone", "Data_Nascimento", "Classe", "Categoria" ]
   search = eg.choicebox("Escolha a opção desejada", title = title, choices = menu_entries)
   if (search == "Nome"):
      query = "funNome"
   if (search == "Endereco"):
      query = "funEnder"
   if (search == "Fone"):
      query = "funFone"
   if (search == "Data_Nascimento"):
      query = "fun_DtNasc"
   if (search == "Classe"):
      query = "funClasse"
   if (search == "Categoria"):
      query = "funCateg"
   search_string = eg.enterbox("Informe a string a pesquisar", title = title, default = "", strip=True)
   fun_query = "SELECT * FROM Funcionarios WHERE %s LIKE '%s'" % (query, "%" + search_string + "%")
   try:
      cursor.execute(fun_query)
      # Fetch all the rows 
      results = cursor.fetchall()
      text  = "Codigo" + " | " + "Nome" + " | " + "Endereco" + " | " + "Fone" + " | " + "Data Nascimento" + " | " + "Classe" + " | " + "Categoria"
      for row in results:
         codigo = row[0]
         nome = row[1]
         endereco = row[2]
         fone = row[3]
         nasc = row[4]
         classe = row[5]
         categoria = row[6]
         text = text + '\n' + str(codigo) + " | " + nome + " | " + endereco + " | " + fone + " | "  + str(nasc) + " | " + classe + " | " + categoria 
   except MySQLdb.Error, e:
      print "Error %d: %s" % (e.args[0], e.args[1])
   eg.textbox("Pesquisa em Funcionarios:", title = title, text = text, codebox = 1)


# search veiculo
def pesqVei():
   msg = "Informe dados veiculo"
   menu_entries = [ "Descricao", "Ano", "Placa", "Quilometragem", "Categoria" ]
   search = eg.choicebox("Escolha a opção desejada", title = title, choices = menu_entries)
   if (search == "Descricao"):
      query = "veiDescr"
   if (search == "Ano"):
      query = "veiAno"
   if (search == "Placa"):
      query = "veiPlaca"
   if (search == "Quilometragem"):
      query = "veiKm"
   if (search == "Categoria"):
      query = "veiCateg"
   search_string = eg.enterbox("Informe a string a pesquisar", title = title, default = "", strip=True)
   vei_query = "SELECT * FROM Veiculos WHERE %s LIKE '%s'" % (query, "%" + search_string + "%")
   try:
      cursor.execute(vei_query)
      # Fetch all the rows 
      results = cursor.fetchall()
      text  = "Codigo" + " | " + "Descricao" + " | " + "Ano" + " | " + "Placa" + " | " + "Quilometragem" + " | " + "Categoria"
      for row in results:
         codigo = row[0]
         descricao = row[1]
         ano = row[2]
         placa = row[3]
         km = row[4]
         categ = row[5]
         text = text + '\n' + str(codigo) + " | " + descricao + " | " + str(ano) + " | " + placa + " | "  + str(km) + " | " + categ 
   except MySQLdb.Error, e:
      print "Error %d: %s" % (e.args[0], e.args[1])
   eg.textbox("Pesquisa em veiculos:", title = title, text = text, codebox = 1)

# main
showMenu()
db.close()
