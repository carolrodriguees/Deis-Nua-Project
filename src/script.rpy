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
define narrador2 = Character(None)
#Backgrounds
image rated1 = "00rated01.png"
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
image casarin2 = "1casarin02.png"
image casarin3out = "1casarin03.png"
image splash = "splash.png"
image splash2 = "splash2.png"
image splash3 = "splash3.png"
image white = Solid("#ffffff")
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
image movie = Movie(size=(1024, 786))
#Public var
init:
    $ centro = Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)

init python:
    menuBak = menu
    globalSave = MultiPersistent("fate.mot.com")
    gambTheme = True
    botaoSave = "menu"
    #titleMenu = globalSave.titleMenu
    
####################################################################

###################################################
label splashscreen:                      # Splash #
    scene black                          ##########
    #$ gambTheme = True
    if globalSave.splash:                #
        $ renpy.pause(2)                 #
    else:                                #
        $ renpy.pause(2, hard=True)      #
                                         #
    show splash at centro with fade      #
    if globalSave.splash:                #
        $ renpy.pause(3)                 #
    else:                                #
        $ renpy.pause(3, hard=True)      #
                                         #
    scene white with dissolve            #
    if globalSave.splash:                #
        $ renpy.pause(1)                 # 
    else:                                #
        $ renpy.pause(1, hard=True)      #
                                         #
    show splash2 at centro with fade     #
    if globalSave.splash:                #
        $ renpy.pause(3)                 #
    else:                                #
        $ renpy.pause(3, hard=True)      #
                                         #
    scene white with dissolve            #
    if globalSave.splash:                #
        $ renpy.pause(1)                 # 
    else:                                #
        $ renpy.pause(1, hard=True)      #
                                         #
    show splash3 at centro with fade     #
    if globalSave.splash:                #
        $ renpy.pause(3)                 #
    else:                                #
        $ renpy.pause(3, hard=True)      #
                                         #
    scene black                          #
    if globalSave.splash:                #
        $ renpy.pause(1)                 # 
    else:                                #
        $ renpy.pause(1, hard=True)      #             
return                                   #
##########################################

#Inicio
label start:
    $ gambTheme = False
    $ botaoSave = "inGame"
#############################################
    #$_game_menu_screen = None      # Pause # Total Fail!
    #show screen mymenu             #########
####################################
    
########################################################    
    $ globalSave.titleMenu = "default"     # Back Menu #
    $ globalSave.splash = True             #############
    $ globalSave.save()                    #
############################################
    
label inicio:
########################################################################    
    stop music fadeout 4                              # Telas de Aviso #
    scene fatestn with Dissolve(5)                    ##################
    $ renpy.pause(1) 
    scene rated1 with Dissolve(3)
    $ renpy.pause(3) 
    narrador "――――――――――――――――――――――――――\nAtenção!\n――――――――――――――――――――――――――\n\nEsta é uma obra de ficção.\n\nTodas as personagens que compõem esta história são fictícias e não têm nenhuma conexão com quaisquer indivíduos ou organizações reais.\n\nTodos as personagens que aparecem neste jogo possuem mais de 18 anos de idade."
    nvl clear
    narrador "Escolha com sabedoria!"
    nvl clear
    menu censura:
        "Fate/Stay Night (12+)":
            $ rated = "kids"
        "Fate/Stay Night (16+)":
            $ rated = "ecchi"
        "Fate/Stay Night (18+)":
            $ rated = "hentai"
    call introfate
### Prólogo Tohsaka Rin
return
