#Cliente TCP
import socket
import random
import time


conversa = random.choice(["Vc tem ?","Quero comprar.","Quanto custa ?","30 reais","blz transfere","e o arroz ta quanto ? ","25 o K","suaver transfero 200k"])
# Endereco IP do Servidor
SERVER = '127.0.0.1' 

# Porta que o Servidor esta escutando
PORT = 5002
tcp = socket.socket(socket.AF_INET,
socket.SOCK_STREAM)
dest = (SERVER, PORT)
tcp.connect(dest)
print ('Para sair use CTRL+X\n')

msg = conversa

while msg != '\x18':
    conversa = random.choice(["Login: leandro","Senha: reidopo", "tenta acessar ai", "acho que agora vai"])

    msg = conversa
    tcp.send(msg.encode())
    time.sleep(1)
    #msg = raw_input()
tcp.close()
