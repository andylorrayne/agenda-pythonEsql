# agenda-pythonEsql
codigo em python de uma agenda simples que salva as informação usando sql 

import datetime
import time
import os
import sys
import string
import mysql.connector
conn=mysql.connector.connect(user='root', password='123sorvete',host='localhost',database='agenda')
mycursor=conn.cursor()
mycursor.execute("SHOW TABLES")
now = datetime.datetime.now()
#print(mycursor.fetchall()



def Excluir():
    print("\n\nVamos excluir alguns contatos...\n")
    print("Você deve saber o ID do contato que deseja excluir, se não sabe returne ao menu CONTATOS e vá em MOSTRAR TODOS\n\n")
    
    ID_del=str(input("ID que deseja excluir: "))
    
    conn=mysql.connector.connect(user='root', password='123sorvete',host='localhost',database='agenda')

    mycursor=conn.cursor()
    
    mycursor.execute("DELETE FROM contatos WHERE id='"+ID_del+"'")
    conn.commit()
    conn.close()
    Contatos()
    

#--------------------------------------------------------------------------------------
    
def Alterar():
    print("\n\nVamos alterar alguns contatos:\n")
    ID_alter=str(input("ID do contato que deseja alterar: "))
    opc=input("O que deseja alterar nesse contato?\n\n(1)-Nome\n(2)-Endereço\n(3)-Email\n(4)-Telefone\n(5)-Voltar para Contatos\n")

    conn=mysql.connector.connect(user='root', password='123sorvete',host='localhost',database='agenda')
    opc=int(opc)
    if opc<1 or opc>4:
           print("opçao invalida: verifique o valor digitado")

    elif opc==1:
        novo_nome=input("Novo nome: ")
        novo_nome=(novo_nome.upper())
        mycursor=conn.cursor()
        mycursor.execute("UPDATE contatos SET nome='"+novo_nome+"' WHERE id='"+ID_alter+"'")
        conn.commit()
        conn.close()
        Contatos()

    elif opc==2:
        novo_end=input("Novo endereço: ")
        novo_end=(novo_end.upper())
        mycursor=conn.cursor()
        mycursor.execute("UPDATE contatos SET endereco='"+novo_end+"' WHERE id='"+ID_alter+"'")
        conn.commit()
        conn.close()
        Contatos()

    elif opc==3:
        novo_email=input("Novo email: ")
        novo_email=(novo_email.upper())
        mycursor=conn.cursor()
        mycursor.execute("UPDATE contatos SET email='"+novo_email+"' WHERE id='"+ID_alter+"'")
        conn.commit()
        conn.close()
        Contatos()

    elif opc==4:
        novo_tel=input("Novo telefone: ")
        novo_tel=(novo_tel.upper())
        mycursor=conn.cursor()
        mycursor.execute("UPDATE contatos SET telefone='"+novo_tel+"' WHERE id='"+ID_alter+"'")
        conn.commit()
        conn.close()
        Contatos()

    elif opc==5:
        Contatos()
        
#------------------------------------------------------------------------------    
def desperta():
    import mysql.connector
    conn=mysql.connector.connect(user='root', password='123sorvete',host='localhost',database='agenda')
    mycursor=conn.cursor()  
    mycursor.execute("SELECT date_format(dt_tarefa, '%d/%m/%Y')as 'dt_format',time_format(hr_tarefa,'%H:%i')as 'hr_format' FROM agendamentos")
    resultados_dt=mycursor.fetchall()
    resultados_dt=str(resultados_dt)
    mycursor.execute("SELECT date_format(now(), '%d/%m/%Y'),time_format(now(),'%H:%i')")
    dt_atual=mycursor.fetchall()
    a=(resultados_dt)
    from datetime import datetime
    hj=datetime.today()

    if hj == a:
        print("tarefa")
    #a=str(a)
    #dt_atual=str(dt_atual)
    #print(a)
    #print(dt_atual)
    #if dt_atual == a:
        #print("você tem tarefas para fazer")

    #for x in a:
           # 3if dt_atual in a: 
             #   print("tarefa pendente")

    #if dt_atual in a:
        #print("VOCE TEM TAREFAS PENDENTES, CONSULTE SUA AGENDA")

#    from datetime import datetime
#    hj=datetime.today()

#
#    conn=mysql.connector.connect(user='root', password='123sorvete',host='localhost',database='agenda')
#    mycursor=conn.cursor()
#    agendame= mycursor.execute('SELECT dt_tarefa,hr_tarefa  FROM agendamentos')

#    if hj == agendame:
#        mycursor.execute('SELECT id_tarefa, tarefa FROM agendamentos')
        
#        print(mycursor.fetchall())
    
#  FUNÇÃO DEPERTA N FUNCIONA
#-----------------------------------------------------------------------------

    
def MostrarTodos():

    conn=mysql.connector.connect(user='root', password='123sorvete',host='localhost',database='agenda')

    mycursor=conn.cursor()
    mycursor.execute("SELECT * FROM contatos")
    resultados=mycursor.fetchall()
    print(resultados)
    print("\n------------------------------------------------------\n")
    conn.commit()

    conn.close()
    Contatos()


#****************************************************************************************
def Cadastrar():
    print("Digite os dados:\n")
    nome=str(input("Nome: "))
    nome=(nome.upper())
    end=str(input("Endereço: "))
    end=(end.upper())
    email=str(input("email: "))
    email=(email.upper())
    tel=str(input("Telefone: "))
    tel=(tel.upper())
    print("-------------------------------------------------------------------------\n")
    conn=mysql.connector.connect(user='root', password='123sorvete',host='localhost',database='agenda')
    mycursor=conn.cursor()
    mycursor.execute("INSERT INTO contatos(nome,endereco,email,telefone) VALUES ('"+nome+"','"+end+"','"+email+"','"+tel+"')")
    conn.commit()
    conn.close()
    Contatos()
        



#******************************************************************************

def Contatos():

    print("Você está em contatos\n")
    opc=input("O QUE QUER FAZER?\n\n\n[1]-Cadastrar\n[2]-Excluir\n[3]-Alterar\n[4]-Mostrar todos\n[5]-Voltar\n")

    opc=int(opc)
    if opc<1 or opc>5:
           print("opçao invalida: verifique o valor digitado")
           opc=input("O QUE QUER FAZER?\n\n\n[1]-Cadastrar\n[2]-Excluir\n[3]-Alterar\n[4]-Mostrar todos\n[5]-sair\n")

    if opc==1:
        conn=mysql.connector.connect(user='root', password='123sorvete',host='localhost',database='agenda')
        mycursor=conn.cursor()
        mycursor.execute("SELECT*FROM contatos")
        Cadastrar()

    elif opc==2:
        conn=mysql.connector.connect(user='root', password='123sorvete',host='localhost',database='agenda')
        mycursor=conn.cursor()
        mycursor.execute("SELECT*FROM contatos")
        Excluir()

    elif opc==3:
        conn=mysql.connector.connect(user='root', password='123sorvete',host='localhost',database='agenda')
        mycursor=conn.cursor()
        mycursor.execute("SELECT*FROM contatos")
        Alterar()


    elif opc==4:
        conn=mysql.connector.connect(user='root', password='123sorvete',host='localhost',database='agenda')
        mycursor=conn.cursor()
        mycursor.execute("SELECT*FROM contatos")
        MostrarTodos()

    elif opc==5:
        TelaInicial()
#**************************************************************************************************

def MostrarTarefas():
    conn=mysql.connector.connect(user='root', password='123sorvete',host='localhost',database='agenda')
    mycursor=conn.cursor()  
    mycursor.execute("SELECT id_tarefa,tarefa, date_format(dt_tarefa, '%d/%m/%Y')as 'dt_format',time_format(hr_tarefa,'%H:%i')as 'hr_format' FROM agendamentos")
    resultados_dt=mycursor.fetchall()
    resultados_dt=str(resultados_dt)


    a=(resultados_dt)
    print(a)
        
    conn.commit()
    conn.close()
    TelaAgendar()

    


#tela de agendar


def Agendar(now):
    conn=mysql.connector.connect(user='root', password='123sorvete',host='localhost',database='agenda')
    mycursor=conn.cursor()
    
    print("Digite os dados:\n")
    tarefa=str(input("Tarefa: "))
    tarefa=(tarefa.upper())

    from datetime import datetime
    
    data=input("Data: dd/mm/aaaa")
    data= now.strptime(data,'%d/%m/%Y')#.strftime('%d/%m%/Y')
    
    data=str(data)
    
    
    #mycursor.execute("SELECT DATE_FORMAT (dt_tarefa,"%d%m%y")as 'dt_tarefa' FROM agendamentos")
    hora=input("Hora: hh:mm")
         
    
    
    mycursor.execute("INSERT INTO agendamentos(tarefa,dt_tarefa,hr_tarefa) VALUES ('"+tarefa+"','"+data+"','"+hora+"')")
    conn.commit()
    desperta()
    conn.close()
    TelaAgendar()
#tela de excluir tarefas

def ExcluirTarefa():

    print("\n\nVamos Tarefas\n")
    print("Você deve saber o ID da Tarefa que deseja excluir, se não sabe returne ao menu AGENDAR TAREFAS e vá em MOSTRAR TODAS\n\n")
    
    ID_del=str(input("ID que deseja excluir: "))
    
    conn=mysql.connector.connect(user='root', password='123sorvete',host='localhost',database='agenda')

    mycursor=conn.cursor()
    mycursor.execute("DELETE FROM agendamentos WHERE id_tarefa='"+ID_del+"'")
    conn.commit()
    conn.close()
    TelaAgendar()
#tela apara fazer altereções

def FazerAlteracoes(now):

    print("\n\nVamos alterar algumas tarefas:\n")
    ID_alter=str(input("ID da TAREFA que deseja alterar: "))
    opc=input("O que deseja alterar nesse contato?\n\n(1)-Tarefa\n(2)-Data\n(3)-Hora\n(4)-Voltar para Contatos\n")

    conn=mysql.connector.connect(user='root', password='123sorvete',host='localhost',database='agenda')
    opc=int(opc)
    if opc<1 or opc>4:
           print("opçao invalida: verifique o valor digitado")
           opc=input("O que deseja alterar nesse contato?\n\n(1)-Tarefa\n(2)-Data\n(3)-Hora\n(4)-Voltar para Contatos\n")
           

    elif opc==1:
        nova_tarefa=input("Nova Tarefa: ")
        nova_tarefa=(nova_tarefa.upper())
        mycursor=conn.cursor()
        mycursor.execute("UPDATE agendamentos SET tarefa='"+nova_tarefa+"' WHERE id_tarefa='"+ID_alter+"'")
        conn.commit()
        desperta()
        conn.close()

        TelaAgendar()

    elif opc==2:
        from datetime import datetime
    
        nova_data=input("Nova Data (dd/mm/aaaa): ")
        nova_data= now.strptime(nova_data,'%d/%m/%Y')#.strftime('%d/%m%/Y')
    
        nova_data=str(nova_data)
        #nova_data=input("Nova data: ")
        
        mycursor=conn.cursor()
        mycursor.execute("UPDATE agendamentos SET dt_tarefa='"+nova_data+"' WHERE id_tarefa='"+ID_alter+"'")
        conn.commit()
        #desperta()
        conn.close()
        TelaAgendar()

    elif opc==3:
        nova_hora=input("Nova hora (00:00): ")
        
        mycursor=conn.cursor()
        mycursor.execute("UPDATE agendamentos SET hr_tarefa='"+nova_hora+"' WHERE id_tarefa='"+ID_alter+"'")
        conn.commit()
        #desperta()
        conn.close()
        TelaAgendar()

    elif opc==4:
        TelaAgendar()
    
#tela para agendamento de tarefas

#-----------------------------------------------------------------------------------------------------------------
def TelaInicial():
    
    print("---------------------------------------------")
    print("---------------------------------------------")
    print("------Olá, bem vindo. Essa é sua agenda------")
    print("---------------------------------------------")
    print("---------------------------------------------\n")

    opcao=input("Escolha uma opção:\n\n(1)Contatos\n(2)Agendar\n(3)Sair\n ")

    #try:
    opcao=int(opcao)
    if opcao<1 or opcao>3:
    
            print("opçao invalida: verifique o valor digitado")
            opcao=input("Escolha uma opção:\n\n(1)Contatos\n(2)Agendar\n(3)Sair\n ")
            
            
    if opcao==1:
        conn=mysql.connector.connect(user='root', password='123sorvete',host='localhost',database='agenda')
        mycursor=conn.cursor()
        mycursor.execute("SELECT * FROM contatos")
        Contatos()

    elif opcao==2:
        con=mysql.connector.connect(user='root', password='123sorvete',host='localhost',database='agenda')
        mycursor=con.cursor()
        mycursor.execute("SELECT * FROM agendamentos")
        TelaAgendar()

    elif opcao==3:
        sys.exit()
#---------------------------------------------------------------------------------------------------------------

def TelaAgendar():
    print("---------------------------------------------")
    print("---------------------------------------------")
    print("---------------AGENDAR TAREFAS---------------")
    print("---------------------------------------------")
    print("---------------------------------------------")


    opca=input("Escolha uma opção:\n[1]-Agendar tarefas\n[2]-Excluir Tarefas\n[3]-Fazer altereções\n[4]-Mostrar todos\n[5]-voltar\n")
    opca=int(opca)
    
    if opca<1 or opca>5:
           print("opçao invalida: verifique o valor digitado")
           opac=print("Escolha uma opção:\n[1]-Agendar tarefas\n[2]-Excluir Tarefas\n[3]-Fazer altereções\n[4]-voltar\n")

    if opca==1:
        conn=mysql.connector.connect(user='root', password='123sorvete',host='localhost',database='agenda')
        mycursor=conn.cursor()
        mycursor.execute("SELECT*FROM agendamentos")
        Agendar(now)

    elif opca==2:
        conn=mysql.connector.connect(user='root', password='123sorvete',host='localhost',database='agenda')
        mycursor=conn.cursor()
        mycursor.execute("SELECT*FROM agendamentos")
        ExcluirTarefa()

    elif opca==3:
        conn=mysql.connector.connect(user='root', password='123sorvete',host='localhost',database='agenda')
        mycursor=conn.cursor()
        mycursor.execute("SELECT*FROM agendamentos")
        FazerAlteracoes(now)
        
    elif opca==4:
        conn=mysql.connector.connect(user='root', password='123sorvete',host='localhost',database='agenda')
        mycursor=conn.cursor()
        mycursor.execute("SELECT*FROM agendamentos")
        MostrarTarefas()

    elif opca==5:
        TelaInicial()
    




           
#**************************************************************************************************
           
TelaInicial()















           
    
