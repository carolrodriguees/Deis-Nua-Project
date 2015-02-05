#######################
# Prólogo Tohsaka Rin #
#######################

#Início
label prologorin:
    play music quietVoice
    scene white with dissolve
    narrador "Esta é uma história de dez anos atrás."
#Rin Black    
    scene black with dissolve
    nvl clear
    narrador "...Eu estou vendo alguém que eu conheço muito bem."
    narrador "Um homem alto, com um rosto profundamente os recursos, que ao meu conhecimento nunca contou uma piada, está batendo na minha cabeça."
    narrador "Não, isso não está certo."
    narrador "Eu acho que ele não sabe quanta força de usar. Assim, para ser mais preciso, ele está agarrando minha cabeça e esmagou-a ao redor."
    
    nvl clear
    narrador "Eu acho que é de se esperar."
    narrador "Afinal, essa é a primeira vez que ele já deu um tapinha na minha cabeça."
    
#Rin ZoomIn
    scene prologorin:
        xanchor 0.2
        yanchor 0.2
        zoom 2.0
    with Dissolve(2)
    nvl clear
    narrador '"Eu vou ter que ir agora . Você sabe o que fazer agora , certo?"'
    
    nvl clear
    narrador 'Eu respondo a voz profunda, com um educado "sim".'
    narrador "O homem batendo na minha cabeça se inclina uma vez, deixa para ir, e se levanta."
    
    nvl clear
    narrador "...Então, foi isso."
    narrador "Se eu soubesse que, em seguida, que foi o nosso último momento juntos, eu teria feito rir com as minhas melhores piadas."
    narrador "Eu tinha praticado contando piadas muito, na esperança de que eu poderia trazer um sorriso a sua sepultura face."
    narrador "Eu acho que você poderia dizer que eu estava triste que eu não poderia dizer-lhe qualquer um deles."
    
#Rin ZoomOut
    scene prologorin with Dissolve(2)
    nvl clear
    narrador '"Coloque a Associação em sua dívida pelo tempo que você amadurecer. Eu vou deixar você decidir o que fazer depois disso. Você deve ser capaz de cuidar de si mesmo."'
    
    nvl clear
    narrador "Mesmo que ele disse essas coisas, eu acho que ele ainda estava preocupado."
    narrador "Ele me contou sobre as jóias de família , as jóias herdadas do mestre, e como gerenciar o porão."
    narrador "Como ele estava me contando todas as coisas que eu ainda não conhecia, eu percebi mesmo como uma criança."
    narrador "\n_____ Muito rovavelmente..."
    narrador "Ele não iria voltar."
    
#Rin Black
    scene black with dissolve
    nvl clear
    narrador "...A guerra tinha começado."
    narrador "Não uma guerra entre os países, mas sim uma guerra entre pessoas."
    narrador "Mas os únicos em guerra eram sete pessoas."
    narrador 'Em uma situação como essa, a palavra "guerra" deve ser inadequada, mas aqui é uma história diferente, como os de conflito são magos.'
    narrador "Os sete magos, cada um de uma facção diferente, tinha começado a completar por razões desconhecidas e matou outro em caminhos desconhecidos."
    
    nvl clear
    narrador "O homem que está diante de mim era um deles."
    narrador "Ele também estava em uma posição para matar ou ser morto."
    narrador "Ele deve ter sabido de maneira mais intensa do que eu fiz que seu tempo estava próximo."
    
#Rin ZoomOut
    scene prologorin with dissolve
    nvl clear
    narrador '"Rin, o Santo Graal aparece eventualmente. É nosso dever como a família Tohsaka para ganhá-la. Mre importante, se você quiser ser um mago, você não pode evitá-lo."'
    
    nvl clear
    narrador "Mais uma vez,"
    narrador "ele acariciou minha cabeça, e saiu."
    narrador "Esse foi o fim."
    narrador "Essa foi a última vez que eu vi o homem, que entrou na guerra do Santo Graal como um mestre e morreu. O homem que foi meu professor, assim como meu pai."
    
#Rin Black
    scene black with dissolve
    nvl clear
    narrador '"Tome cuidado, Pai."'

    nvl clear
    narrador "Vejo-o fora educadamente."
    narrador "Eu sabia que estava a ponto de chorar, mas eu não derramei nenhuma lágrima."
    
    nvl clear
    narrador "Eu o amava."
    narrador "Ele foi um grande pai e um grande mago."
    narrador "Entre magi, há pessoas só obstinados."
    narrador "Em todo o mundo, eu não acho que alguém tinha um personagem melhor do que a dele."
    narrador "Ele me ensinou como professora e me amava como um pai."
    
    nvl clear
    narrador "É por isso que eu decidi..."
    narrador "Para escolher o meu caminho de acordo com o que ele me deixou no final."
    
#Rin ZoomIn
    scene prologorin:
        xanchor 0.2
        yanchor 0.2
        zoom 2.0
    with Dissolve(2)
    nvl clear
    narrador '\'_______Rin, o Santo Graal aparece eventualmente. É nosso dever como a família Tohsaka para ganhá-la. Mre importante, se você quiser ser um mago, você não pode evitá-lo._______\''
    
    nvl clear
    narrador "No final, ele me deixou essas palavras como um mago e não como um pai."
    narrador "É por isso que, naquele momento, o meu caminho foi determinada."
    narrador '"_______Tudo certo. Vou fazer o meu melhor para ser um mago adequada_______"'
    narrador "É natural para um estudante de seguir as palavras de seu professor."
    narrador "Desde então, através de muitas voltas e mais voltas... Eu, Tohsaka Rin, amadureceram."

    stop music fadeout 3.0
    nvl clear
    narrador "Tem sido 10 anos desde o dia de inverno em que o meu pai foi para a guerra."
    narrador "Eu mesmo não estava esperando por esse momento, mas estou animado."
    narrador "Isso é natural."
    narrador "O evento que eu nunca ter esquecido está prestes a começar_______"
    
#Fim Prólogo
    call rin1_1

return