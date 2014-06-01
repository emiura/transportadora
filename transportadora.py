#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import easygui as eg
import MySQLdb
import subprocess 
import ConfigParser
from threading import Thread

# parse config file
configParser = ConfigParser.RawConfigParser()
configFilePath = r'/etc/transportadora.conf'
configParser.read(configFilePath)
host = configParser.get('mysql','host')
user = configParser.get('mysql','user')
password = configParser.get('mysql','password')
db_name = configParser.get('mysql','db_name')

# global pref
title = "Programa de controle de transportadora"

# connection
db = MySQLdb.connect(host, user, password, db_name)

# create a cursor
cursor = db.cursor()

# send a text to printer
def sendPrinter(text):
   lpr = subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
   lpr.stdin.write(text) 

# place holder function
def notYet():
   eg.msgbox("Not implemented!")

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
            notYet()
            showMenu()
         if (cad_type == "Filiais"):
            notYet()
            showMenu()
         if (cad_type == "Funcionarios"):
            cadFunc()
         if (cad_type == "Clientes"):
            notYet()
            showMenu()
         if (cad_type == "Veiculos"):
            cadVei()
         if (cad_type == "Rotas"):
            notYet()
            showMenu()
         if (cad_type == "Rodovias"):
            notYet()
            showMenu()
         if (cad_type == None):
            showMenu()
         
      # search
      if (action == "Pesquisa"):
         pesq_entries = [ "Localidades", "Filiais", "Funcionarios", "Clientes", "Veiculos", "Rotas", "Rodovias" ]
         pesq_type = eg.choicebox("Escolha o tipo de pesquisa", title = title, choices = pesq_entries)
         if (pesq_type == "Localidades"):
            notYet()
            showMenu()
         if (pesq_type == "Filiais"):
            notYet()
            showMenu()
         if (pesq_type == "Funcionarios"):
            notYet()
            showMenu()
            pesqFunc()
         if (pesq_type == "Clientes"):
            notYet()
            showMenu()
         if (pesq_type == "Veiculos"):
            pesqVei()
         if (pesq_type == "Rotas"):
            notYet()
            showMenu()
         if (pesq_type == "Rodovias"):
            notYet()
            showMenu()
         if (pesq_type == None):
            showMenu()

      # operational
      if (action == "Operacao"):
         op_entries = [ "Ordem servico", "Viagens", "Carga/Descarga" ]
         op_type = eg.choicebox("Escolha o tipo de Operação", title = title, choices = op_entries)
         if (op_type == "Ordem servico"):
            cadOrdens()
         if (op_type == "Viagens"):
            cadViagens()
         if (op_type == "Carga/Descarga"):
            notYet()
            showMenu()
         if (op_type == None):
            showMenu()

      # report
      if (action == "Relatorios"):
         rel_entries = [ "Veiculos", "Clientes", "Funcionarios" ]
         rel_type = eg.choicebox("Escolha o tipo de Relatorio", title = title, choices = rel_entries)
         if (rel_type == "Veiculos"):
            reportVeiculos()
         if (rel_type == "Clientes"):
            notYet()
            showMenu()
         if (rel_type == "Funcionarios"):
            reportFunc()
         if (rel_type == None):
            showMenu()

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
         showMenu()
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
         showMenu()
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
   if (search == None):
      showMenu()

   search_string = eg.enterbox("Informe a string a pesquisar", title = title, default = "", strip=True)
   fun_query = "SELECT * FROM Funcionarios WHERE %s LIKE '%s'" % (query, "%" + search_string + "%")
   try:
      cursor.execute(fun_query)
      db.commit()
      # Fetch all the rows 
      results = cursor.fetchall()
      sql_output = []
      for row in results:
         codigo = row[0]
         nome = row[1]
         endereco = row[2]
         fone = row[3]
         nasc = row[4] 
         classe = row[5]
         categoria = row[6]
         text = str(codigo) + " | " + nome + " | " + endereco + " | " + fone + " | " + str(nasc) + " | " + classe + " | " + categoria
         sql_output.append(text)
   except MySQLdb.Error, e:
      print "Error %d: %s" % (e.args[0], e.args[1])

   # parses returned data, so can edit
   edit_func = eg.choicebox("Codigo - Nome - Endereco - Fone - Data Nasc. - Classe - Categoria", title = title, choices = sql_output)
   codigo = edit_func.split("|")[0].replace(" ", "")
   nome = edit_func.split("|")[1].strip()
   endereco = edit_func.split("|")[2].strip()
   fone = edit_func.split("|")[3].replace(" ", "")
   nascimento = edit_func.split("|")[4].replace(" ", "")
   print
   classe = edit_func.split("|")[5].replace(" ", "")
   categoria = edit_func.split("|")[6].replace(" ", "")

   msg = "Deseja editar, deletar o registro ou Continuar?"
   choices = ["Editar", "Deletar", "Continuar"]
   edit_or_delete = eg.buttonbox(msg,choices=choices)

   # update values
   if (edit_or_delete == "Editar"): 
      msg = "Atualizacao dos registros"
      fieldNames = [ "Codigo", "Nome", "Endereco", "Fone", "Data Nascimento", "Classe", "Categoria" ]  
      fieldValues = [ codigo, nome, endereco, fone, nascimento, classe, categoria ]
      fieldValues = eg.multenterbox(msg, title, fieldNames, fieldValues)
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
         try:
            print cursor.execute("UPDATE Funcionarios SET funNome = '%s' WHERE funCodigo = '%d'" % (fieldValues[1], int(codigo)))
            print cursor.execute("UPDATE Funcionarios SET funEnder = '%s' WHERE funCodigo = '%d'" % (fieldValues[2], int(codigo)))
            print cursor.execute("UPDATE Funcionarios SET funFone = '%s' WHERE funCodigo = '%d'" % (fieldValues[3], int(codigo)))
            print cursor.execute("UPDATE Funcionarios SET funDtNasc = '%s' WHERE funCodigo = '%d'" % (fieldValues[4], int(codigo)))
            print cursor.execute("UPDATE Funcionarios SET funClasse = '%s' WHERE funCodigo = '%d'" % (fieldValues[5], int(codigo)))
            print cursor.execute("UPDATE Funcionarios SET funCateg = '%s' WHERE funCodigo = '%d'" % (fieldValues[6], int(codigo)))
            db.commit()
         except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
   # delete entry
   if(edit_or_delete == "Deletar"):
      try:
         cursor.execute("DELETE FROM Funcionarios WHERE funCodigo = '%d'" % (int(codigo)))
         db.commit()
      except MySQLdb.Error, e:
         print "Error %d: %s" % (e.args[0], e.args[1])

   # return to main
   if (edit_or_delete == "Continuar"):
      showMenu()



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
   if (search == None):
      showMenu()

   search_string = eg.enterbox("Informe a string a pesquisar", title = title, default = "", strip=True)
   vei_query = "SELECT * FROM Veiculos WHERE %s LIKE '%s'" % (query, "%" + search_string + "%")
   try:
      cursor.execute(vei_query)
      db.commit()
      # Fetch all the rows 
      results = cursor.fetchall()
      sql_output = []
      for row in results:
         codigo = row[0]
         descricao = row[1]
         ano = row[2]
         placa = row[3]
         km = row[4]
         categ = row[5]
         text = str(codigo) + " | " + descricao + " | " + str(ano) + " | " + placa + " | "  + str(km) + " | " + categ 
         sql_output.append(text)
   except MySQLdb.Error, e:
      print "Error %d: %s" % (e.args[0], e.args[1])

   # parse output to edit
   edit_veic = eg.choicebox("Codigo - Descricao - Ano - Placa - KM - Categoria", title = title, choices = sql_output)

   codigo = edit_veic.split("|")[0].replace(" ", "")
   descricao = edit_veic.split("|")[1].strip()
   ano = edit_veic.split("|")[2].replace(" ", "")
   placa = edit_veic.split("|")[3].replace(" ", "")
   km = edit_veic.split("|")[4].replace(" ", "")
   categ = edit_veic.split("|")[5].replace(" ", "")

   msg = "Deseja editar ou deletar o registro ou Continuar?"
   choices = ["Editar", "Deletar", "Continuar"]
   edit_or_delete = eg.buttonbox(msg,choices=choices)

   # update
   if (edit_or_delete == "Editar"): 
      msg = "Atualizacao dos registros"
      fieldNames = [ "Codigo", "Descricao", "Ano", "Placa", "Quilometragem", "Categoria" ]  
      fieldValues = [ codigo, descricao, ano, placa, km, categ ]
      fieldValues = eg.multenterbox(msg, title, fieldNames, fieldValues)
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
         try:
            print cursor.execute("UPDATE Veiculos SET veiDescr = '%s' WHERE veiCodigo = '%d'" % (fieldValues[1], int(codigo)))
            print cursor.execute("UPDATE Veiculos SET veiAno = '%d' WHERE veiCodigo = '%d'" % (int(fieldValues[2]), int(codigo)))
            print cursor.execute("UPDATE Veiculos SET veiPlaca = '%s' WHERE veiCodigo = '%d'" % (fieldValues[3], int(codigo)))
            print cursor.execute("UPDATE Veiculos SET veiKm = '%d' WHERE veiCodigo = '%d'" % (int(fieldValues[4]), int(codigo)))
            print cursor.execute("UPDATE Veiculos SET veiCateg = '%s' WHERE veiCodigo = '%d'" % (fieldValues[5], int(codigo)))
            db.commit()
         except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])

   # delete entry
   if(edit_or_delete == "Deletar"):
      try:
         cursor.execute("DELETE FROM Veiculos WHERE veiCodigo = '%d'" % (int(codigo)))
         db.commit()
      except MySQLdb.Error, e:
         print "Error %d: %s" % (e.args[0], e.args[1])

   # back to main
   if(edit_or_delete == "Continuar"):
      showMenu()


# register ordens
def cadOrdens():
   try:
      cursor.execute("select ordNumero from Ordens order by ordNumero DESC limit 1")
      db.commit()
      num = cursor.fetchone()
      last_entry = int(num[0]) + 1
   except MySQLdb.Error, e:
      print "Error %d: %s" % (e.args[0], e.args[1])
   msg = "Informe dados do Pedido"
   fieldNames = [ "Data", "Quantidade itens", "Valor total", "Codigo Origem", "Codigo Destino", "Codigo Remetente", "Codigo Destinatario", "Codigo Funcionario", "ICMS", "ISS", "Tipo"  ]  
   fieldValues = []
   fieldValues = eg.multenterbox(msg, title, fieldNames)
   while 1:
      if fieldValues == None:
         showMenu()
      errmsg = ""
      for i in range(len(fieldNames)):
         if fieldValues[i].strip() == "":
            errmsg = errmsg + ('"%s" eh requerido'  % fieldNames[i])
      if errmsg == "":
         break
      fieldValues = eg.multenterbox(errmsg, title, fieldNames, fieldValues)
   if (fieldValues != None):
      ordens = "INSERT INTO Ordens(ordNumero, ordData, ordQtIteNS, ordVlTotal, CodOrigem, CodDestino, CodRemetente, CodDestinatario, funCodigo, ordICMS, ordISS, ordTipo) VALUES ('%d', '%s', '%d', '%f', '%d', '%d', '%d', '%d','%d', '%f','%f','%s')" % (last_entry, fieldValues[0], int(fieldValues[1]), float(fieldValues[2]), int(fieldValues[3]), int(fieldValues[4]), int(fieldValues[5]), int(fieldValues[6]), int(fieldValues[7]), float(fieldValues[8]), float(fieldValues[9]), fieldValues[10])
      print execQuery(ordens)


# register viagens
def cadViagens():
   try:
      cursor.execute("select viaNumero from Viagens order by viaNumero DESC limit 1")
      db.commit()
      num = cursor.fetchone()
      last_entry = int(num[0]) + 1
      print last_entry
   except MySQLdb.Error, e:
      print "Error %d: %s" % (e.args[0], e.args[1])

   msg = "Informe dados da Viagem:"
   fieldNames = [ "Data", "Observacoes", "KM Inicial", "KM Final", "Codigo Veiculo", "Codigo Funcionario", "Codigo da Rota" ]  
   fieldValues = []
   fieldValues = eg.multenterbox(msg, title, fieldNames)
   while 1:
      if fieldValues == None:
         showMenu()
      errmsg = ""
      for i in range(len(fieldNames)):
         if fieldValues[i].strip() == "":
            errmsg = errmsg + ('"%s" eh requerido'  % fieldNames[i])
      if errmsg == "":
         break
      fieldValues = eg.multenterbox(errmsg, title, fieldNames, fieldValues)
   if (fieldValues != None):
      viagens = "INSERT INTO Viagens(viaNumero, viaData, viaObs, viaKmIni, viaKmFim, veiCodigo, funCodigo, rtaCodigo) VALUES ('%d', '%s', '%s', '%d', '%d', '%d', '%d', '%d' )" % (last_entry, fieldValues[0], fieldValues[1], int(fieldValues[2]), int(fieldValues[3]), int(fieldValues[4]), int(fieldValues[5]), int(fieldValues[6]))
      print execQuery(viagens)


# report Funcionarios
def reportFunc():
   msg = "Relatorio de Funcionarios"
   func_query = "SELECT * FROM Funcionarios"
   try:
      cursor.execute(func_query)
      db.commit()
      # Fetch all the rows 
      results = cursor.fetchall()
      text  = "| \t" + "Codigo \t" + " | \t" + "Nome \t" + " | \t" + "Endereco \t" + " | \t" + "Fone \t" + " | \t" + "Data Nascimento \t" + " | \t" + "Classe \t" + " | \t" + "Categoria \t" + " |"
      for row in results:
         codigo = row[0]
         nome = row[1]
         endereco = row[2]
         fone = row[3]
         nasc = row[4] 
         classe = row[5]
         categoria = row[6]
         text = text + '\n' + str(codigo) + " - " + nome + " - " + endereco + " - " + fone + " - " + str(nasc) + " - " + classe + " - " + categoria 
   except MySQLdb.Error, e:
      print "Error %d: %s" % (e.args[0], e.args[1])
   eg.textbox("Pesquisa em Funcionarios:", title = title, text = text, codebox = 1)
   msg = "Deseja imprimir?"
   
   # print
   if eg.ccbox(msg, title): 
      sendPrinter(text)
   else:
      showMenu()


# report Veiculos
def reportVeiculos():
   msg = "Relatorio de Veiculos"
   veic_query = "SELECT * FROM Veiculos"
   try:
      cursor.execute(veic_query)
      db.commit()
      # Fetch all the rows 
      results = cursor.fetchall()
      text = "| \t" + "Codigo \t" + " | \t" + "Descricao \t" + " | \t" + "Ano \t" + " | \t" + "Placa \t" + " | \t"  + "Quilometragem \t" + " | \t" + "Categoria \t" + " |"
      for row in results:
         codigo = row[0]
         descricao = row[1]
         ano = row[2]
         placa = row[3]
         km = row[4]
         categ = row[5]
         text = text + '\n' + str(codigo) + " - " + descricao + " - " + str(ano) + " - " + placa + " - "  + str(km) + " - " + categ 
   except MySQLdb.Error, e:
      print "Error %d: %s" % (e.args[0], e.args[1])
   eg.textbox("Pesquisa em Veiculos:", title = title, text = text, codebox = 1)
   msg = "Deseja imprimir?"

   # print
   if eg.ccbox(msg, title): 
      sendPrinter(text)
   else:
      showMenu()


# main
showMenu()
db.close()
