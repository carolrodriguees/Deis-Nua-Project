##############
# Introdução #
##############

define direitorapido = CropMove(0.3, "slideright")

#Início
label introfate:
    scene black
    with Pause(3)
    scene prologo01:
        zoom 2.0
        linear 3.0 zoom 1.0
    with Pause(2)
    show prologo01t at centro with dissolve
    with Pause(2)
    play music "0musicaprologo.ogg"
    
#Reflexão 1     
    scene prologo02 with flash
    narrador "Foi um impulso como um relâmpago."
    narrador "A ponta da lança empurrou para furar meu coração."
    narrador "Seria inútil tentar me esquivar."
    narrador "Sendo luz, é invisível ao olho humano."
    
#Lança    
    scene backtrans with direitorapido
    play sound "0vuts.ogg"
    show clang1
    with Pause(0.05)
    show clang2 with dissolve
    with Pause(0.1)
    show clang3 with vpunch
    with flash
    with Pause(0.1)
    scene white
    
#Clarão    
    narrador "\nMas..."
    narrador "O raio que tenta me furar..."
    narrador "....É repelido pela luz da lua que tenta me salvar."
    nvl clear
    play sound "0clang.ogg"
    narrador "Clang, um som bonito."
    narrador "\nNão, o som antes de mim é mais pesado do que o aço."
    narrador "A armadura que ela está usando não é bonito em tudo e não refinado como a noite fria."
    narrador "O som não era bonito em tudo."
    narrador "\nNa verdade, foi o som de aço."
    narrador "É justo que o cavaleiro é bonito o suficiente para transformá-lo em um som encantador como um sino."
    nvl clear
    
#Aparição Saber    
    scene white
    with Pause(1)
    show nevoa
    show prologo03 at Position(xpos = 0.5, xanchor=0.5, ypos=0.7, yanchor=0.5) behind nevoa with Dissolve(1)
    with Pause(1)
    
#Saber 1    
    voice "saber01-01.ogg"
    narrador '\n\n\n\n\n\n\n\n"_______ Eu lhe pergunto. É você o meu Mestre?"'
    narrador "\nEla pergunta em uma voz que ilumina a escuridão."
    
#Saber 2    
    scene prologo03 with Dissolve(2)
    with Pause(2)
    nvl clear
    voice "saber01-02.ogg"
    narrador '\n\n\n\n\n\n\n\n"Eu vim adiante em resposta à sua invocação.'
    voice "saber01-03.ogg"
    narrador 'A partir deste momento em diante, minha espada estará com você e seu destino estará comigo. Agora, o nosso contrato está completo."'
    nvl clear
    
#Reflexão 2
    narrador "\n\n\n\n\n\n\n\nSim, o contrato foi concluído."
    narrador "Quando ela me escolheu como seu Mestre..."
    narrador "Eu tenho certeza que eu jurei ajudá-la também."
    nvl clear
    narrador "O luar ainda ilumina a escuridão."
    narrador "Como se seguindo o exemplo do cavaleiro, o galpão fica em silêncio novamente."
    nvl clear
    narrador "O tempo parou."
    narrador "A cena dura menos de um segundo."
    narrador "\nMas..."
    narrador "Tenho certeza de que vou me lembrar dessa cena vividamente mesmo quando eu for para o inferno."
    nvl clear
    narrador "\n\n\n\n\n\n\n\nO rosto ligeiramente virado."
    narrador "Os tranquilos olhos verdes."
    narrador "No instante em que se torna uma eternidade."
    narrador "O equipamento azul simbolizando seus balanços no vento."
    nvl clear
    narrador "\n\n\n\n\n\n\n\n\n_______ Uma leve luz azul filtra."
    narrador "O cabelo dourado brilha à luz do luar."
    stop music fadeout 4
    
#Início Fate
    scene fate with Dissolve(1)
    nvl clear
    $ renpy.pause(3, hard=True)
    
    $ globalSave.titleMenu = "saberApp"
    $ globalSave.save()
    
    call prologorin
    
return
