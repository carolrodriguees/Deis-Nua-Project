##########################################################################################################
## Fate/Stay Night [Deis Nua] ############################################################################
## Início do projeto [24/11/2014] ########################################################################
## Remake do jogo em estilo visual novel Fate/Stay Night com o objetivo de traduzí-lo para o português. ##
## Este projeto não tem nenhum vínculo direto com a produtora original e não possui fins lucrativos. #####
## O projeto está sob total responsabilidade do desenvolvedor, William Tumeo. ############################
##########################################################################################################

###################################################################################################
## Informações de Port                                                                           ##
## Windows x64 [OK] - Mínimo: Celeron Dual-Core 1.1Ghz; Mínimo vídeo: Intel Dual-Core 2.0Ghz.    ##
## Linux x64 [OK] - Versão testada: Distribuição Ubuntu w/ 2.0Ghz.                               ##
## Android [OK~] - Versão testada: 3.5" w/ 1.0Ghz (dificuldade na leitura); 4.8" Galaxy S3 (Ok); ##
## x.x" Moto G (fonte pequena).                                                                  ##
## Macintosh [Pendente]                                                                          ##
###################################################################################################
#Personagens
define narrador = Character(None, kind=nvl)

#Backgrounds
image fatestn = "titleopt.png"
image prologo01 = "0prologo01.png"
image prologo02 = "0prologo02.png"
image prologo01t = "0prologo01-texto.png"
image prologo03 = "0prologo03.png"
image nevoa = "0nevoa.png"
image backtrans = "0clang00.png"
image clang1 = "0clang01.png"
image clang2 = "0clang02.png"
image clang3 = "0clang03.png"
image fate = "0fate.png"
image prologorin = "1prologo01.png"
image casarin1blur = "1casarin01-blur.png"
image casarin1 = "1casarin01.png"
image blackmagi = "1blackmagi.png"
image splash = "splash.png"
image splash2 = "splash2.png"
image splash3 = "splash3.png"
image white = Solid("#ffffff")
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
#Public var
init:
    $ centro = Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)
  
####################################################################

#Splash
label splashscreen:
    scene black
    with Pause(2)
    show splash at centro with fade 
    with Pause(3)
    scene white with dissolve
    with Pause(1)
    show splash2 at centro with fade
    with Pause(3)
    scene white with dissolve
    with Pause(1)
    show splash3 at centro with fade
    with Pause(3)
    scene black
    with Pause(1)
return

#Inicio
label start:
    stop music
    scene fatestn with Dissolve(2)
    narrador "―――――――――――――――\nAtenção!\n―――――――――――――――\nEsta é uma obra de ficção.\nTodas as configurações desta história são fictícias e não têm nenhuma conexão com quaisquer indivíduos ou organizações reais.\nTodos os personagens que aparecem neste jogo tem mais de 18 anos de idade."
    nvl clear
    menu censura:
        narrador "―――――――――――――――\nEscolha com sabedoria!\n―――――――――――――――?"
        
        "Fate/Stay Night (12+)":
            call introfate
        "Fate/Stay Night (16+)":
            call introfate
        "Fate/Stay Night (18+)":
            call introfate
#    $ renpy.movie_cutscene("introfate.ogv")
#    $ renpy.movie_cutscene("introbone.ogv")
#    $ renpy.movie_cutscene("introfeels.ogv")
### Prólogo Tohsaka Rin
return
