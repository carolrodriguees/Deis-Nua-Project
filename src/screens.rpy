# Este archivo se encuentra en el dominio público. Puede ser modificado
# libremente como base para tus propias pantallas.

##############################################################################
# Diálogo
#
# Pantalla utilizada para presentar el diálogo en modo adv.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:

    # Valores por defecto de 'side_image' y 'two_window'
    default side_image = None
    default two_window = False

    # Opta entre las variantes de una ventana o dos ventanas.
    if not two_window:

        # Una ventana.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # Dos ventanas.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # Si hay una imagen lateral, la presenta sobre el texto.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Usa el menú de acceso rápido.
    use quick_menu


##############################################################################
# Elecciones
#
# Pantalla utilizada para presentar los menus dentro del juego.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)


##############################################################################
# Entrada
#
# Pantalla utilizada para la entrada de texto por parte del usuario.
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Pantalla utilizada para el diálogo y los menús en modo nvl.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl:

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Presenta el diálogo.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Presenta un menú, si lo hay.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu - Menú principal
#
# Pantalla utilizada para presentar el menú principal, cuando Ren'Py empieza
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu:

    # Esta linea asegura que las otras pantallas de menú son reemplazadas.
    tag menu

   ## add "navground.png"

    # The main menu buttons.
    window:
        style "mm_root"

################################################## Backgrounds Variados ##############################
    if globalSave.titleMenu == "saberApp":
        image "bg/0prologo03.png"

        ##############################################################################################

################################################## Botões Main Menu #######################################################################
    imagebutton idle "bt/btnewidle.png" hover "bt/btnewhover.png" xpos 120 ypos 650 focus_mask True action Start() activate_sound "menuselect.ogg" hover_sound "menuhover.ogg"
    imagebutton idle"bt/btloadidle.png" hover "bt/btloadhover.png" xpos 320 ypos 650 focus_mask True action ShowMenu('load') activate_sound "menuselect.ogg" hover_sound "menuhover.ogg"
    imagebutton idle "bt/btoptionidle.png" hover "bt/btoptionhover.png" xpos 520 ypos 650 focus_mask True action ShowMenu('preferences') activate_sound "menuselect.ogg" hover_sound "menuhover.ogg"
    imagebutton idle "bt/btexitidle.png" hover "bt/btexithover.png" xpos 720 ypos 650 focus_mask True action Quit(confirm=True) activate_sound "menuselect.ogg" hover_sound "menuhover.ogg"

        ###################################################################################################################################

    # Fondo del menú principal.

init -2:

    # Ajusta todos los botones del menú principal al mismo tamaño.
    style mm_button:
        size_group "mm"



##############################################################################
# Navegación
#
# Pantalla incluida en otras pantallas para presentar las opciones de
# navegación y el fondo en los menús del juego.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:

    # Fondo de los menús del juego.
    window:
        style "gm_root"
#################################################### Backgrounds Variados #########################################################################################################################################################

    imagebutton idle "bt/btbackidle.png" hover "bt/btbackhover.png" xpos 800 ypos 100 focus_mask  True action Return()
    imagebutton idle "bt/btoptionidle.png" hover "bt/btoptionhover.png" selected_idle "bt/btoptionselected.png" selected_hover "bt/btoptionselected.png" xpos 800 ypos 160 focus_mask  True action ShowMenu("preferences")
    imagebutton idle "bt/btsaveidle.png" hover "bt/btsavehover.png" selected_idle "bt/btsaveselected.png" selected_hover "bt/btsaveselected.png" insensitive "bt/btsaveground.png" xpos 800 ypos 220 focus_mask  True action ShowMenu("save")
    imagebutton idle "bt/btloadidle.png" hover "bt/btloadhover.png" selected_idle "bt/btloadselected.png" selected_hover "bt/btloadselected.png" xpos 800 ypos 280 focus_mask  True action ShowMenu("load")
    imagebutton idle "bt/btmainidle.png" hover "bt/btmainhover.png" insensitive "bt/btmainground.png" xpos 800 ypos 340 focus_mask  True action MainMenu()
    imagebutton idle "bt/bthelpidle.png" hover "bt/bthelphover.png" selected_idle "bt/bthelpselected.png" selected_hover "bt/bthelpselected.png" xpos 800 ypos 400 focus_mask True action ShowMenu("helps")
    imagebutton idle "bt/btexitidle.png" hover "bt/btexithover.png" xpos 800 ypos 460 focus_mask  True action Quit()

    ################################################################################################################################################################################################################################

    # Botones de navegación.
#    frame:
 #       style_group "gm_nav"
  #      xalign .98
   #     yalign .98
#
 #       has vbox
#
 #       textbutton _("Return") action Return()
  #      textbutton _("Preferences") action ShowMenu("preferences")
   #     textbutton _("Save Game") action ShowMenu("save")
    #    textbutton _("Load Game") action ShowMenu("load")
     #   textbutton _("Main Menu") action MainMenu()
      #  textbutton _("Help") action Help()
       # textbutton _("Quit") action Quit()

init -2:

    # Todos los botones del menú de navegación del mismo tamaño
    style gm_nav_button:
        size_group "gm_nav"

########################### Botões #######################################
screen botoes:

    imagebutton idle "bt/btbackidle.png" hover "bt/btbackhover.png" xpos 800 ypos 100 focus_mask  True action Return() activate_sound "menuselect.ogg"
    imagebutton idle "bt/btoptionidle.png" hover "bt/btoptionhover.png" selected_idle "bt/btoptionselected.png" selected_hover "bt/btoptionselected.png" xpos 800 ypos 160 focus_mask  True action ShowMenu("preferences") activate_sound "menuselect.ogg"
    #if botaoSave == "menu":
    #    imagebutton idle "bt/btsaveidle.png" hover "bt/btsavehover.png" selected_idle "bt/btsaveselected.png" selected_hover "bt/btsaveselected.png" insensitive "bt/btsaveground.png" xpos 800 ypos 220 focus_mask  True
    #else:
    imagebutton idle "bt/btsaveidle.png" hover "bt/btsavehover.png" selected_idle "bt/btsaveselected.png" selected_hover "bt/btsaveselected.png" insensitive "bt/btsaveground.png" xpos 800 ypos 220 focus_mask  True action ShowMenu("save2") activate_sound "menuselect.ogg"
    imagebutton idle "bt/btloadidle.png" hover "bt/btloadhover.png" selected_idle "bt/btloadselected.png" selected_hover "bt/btloadselected.png" xpos 800 ypos 280 focus_mask  True action ShowMenu("load") activate_sound "menuselect.ogg"
    imagebutton idle "bt/btmainidle.png" hover "bt/btmainhover.png" insensitive "bt/btmainground.png" xpos 800 ypos 340 focus_mask  True action MainMenu()  activate_sound "menuselect.ogg"
    imagebutton idle "bt/bthelpidle.png" hover "bt/bthelphover.png" selected_idle "bt/bthelpselected.png" selected_hover "bt/bthelpselected.png" xpos 800 ypos 400 focus_mask True action ShowMenu("helps") activate_sound "menuselect.ogg"
    imagebutton idle "bt/btexitidle.png" hover "bt/btexithover.png" xpos 800 ypos 460 focus_mask  True action Quit() activate_sound "menuselect.ogg"

########################## Fundo Alternante ##############################
screen fundo:

    if gambTheme:
        if globalSave.titleMenu == "saberApp":
            image "system/0prologo03_blur.png"
        else:
            image "system/titleopt.png"
    else:
        image "system/layeradd.png"


##############################################################################
# Guardar, Cargar
#
# Pantallas que permiten al usuario guardar y cargar las partidas.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Ya que guardar y cargar son muy similares, se combinan en una sola
# pantalla, selector de archivo ('file_picker'). Esa se usa desde
# simples pantallas de guardado y carga.

screen file_picker:

    frame:
        xpos 40
        ypos 50
        style "file_picker_frame"

        has vbox

        # Los botones superiores permiten al usuario escoger entre
        # páginas de archivos.
        hbox:
            style_group "file_picker_nav"

            textbutton _("Previous"):
                action FilePagePrevious()

            #textbutton _("Auto"):
            #    action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 8):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Next"):
                action FilePageNext()

        $ columns = 2
        $ rows = 5

        # Presenta una cuadrícula de espacios para archivos.
        grid columns rows:
            transpose True
            xfill False
            style_group "file_picker"
            xmaximum 600

            # Presenta diez espacios para archivos, numerados de 1 a 10.
            for i in range(1, columns * rows + 1):

                # Cada espacio es un botón.
                button:
                    xsize 325
                    ysize 70
                    ypadding 3
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Añade la captura de pantalla.
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)

###################### Save ###############################
screen save2:
    # Esta linea asegura que las otras pantallas de menú son reemplazadas.
    tag menu
    use fundo

    text "Salvar" xanchor 0.5 xpos 0.873 ypos 45

    use botoes
    use file_picker

###################### Load ###############################
screen load:

    # Esta linea asegura que las otras pantallas de menú son reemplazadas.
    tag menu

    use fundo

    text "Carregar" xanchor 0.5 xpos 0.873 ypos 45

    use botoes
    use file_picker

################################################################################################### Ignorar ####

screen load2:

    # Esta linea asegura que las otras pantallas de menú son reemplazadas.
    tag menu

    use navigation
    use file_picker

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text


################################################################################################################
# Opciones
#
# Pantalla que permite al usuario cambiar las opciones.
# http://www.renpy.org/doc/html/screen_special.html#preferences


screen helps:
    tag menu

    use fundo

    vbox:
        xpos 40
        ypos 50

        frame:
            ymargin 3
            has vbox
            text "                                                                       "
            text "                                                                       "
        frame:
            ymargin 3
            has vbox
            text "                                                                       "
            text "                                                                       "
        frame:
            ymargin 3
            has vbox
            text "                                                                       "
            text "                                                                       "
        frame:
            ymargin 3
            has vbox
            text "                                                                       "
            text "                                                                       "
        frame:
            ymargin 3
            has vbox
            text "                                                                       "
            text "                                                                       "
        frame:
            ymargin 3
            has vbox
            text "                                                                       "
            text "                                                                       "
        frame:
            ymargin 3
            has vbox
            text "                                                                       "
            text "                                                                       "
        frame:
            xpos 1.063
            ypos -1.1
            has vbox
            textbutton "Mais ajuda!" action Help()

    imagebutton idle "ajuda/right.png" hover "ajuda/right.png" xpos 170 ypos 63 focus_mask True
    imagebutton idle "ajuda/esc.png" hover "ajuda/esc.png" xpos 55 ypos 63 focus_mask True
    text "Pausa o jogo e mostra o menu." xanchor 1.0 xpos 0.74 ypos 0.1
    text "{color=#00f} ▪{/color}" xpos 124 ypos 0.1

    imagebutton idle "ajuda/return.png" hover "ajuda/return.png" xpos 55 ypos 159 focus_mask True
    imagebutton idle "ajuda/space.png" hover "ajuda/space.png" xpos 150 ypos 159 focus_mask True
    imagebutton idle "ajuda/left.png" hover "ajuda/left.png" xpos 295 ypos 159 focus_mask True
    text "Segue na história." xanchor 1.0 xpos 0.74 ypos 0.23
    text "{color=#00f} ▪{/color}" xpos 124 ypos 0.217
    text "{color=#00f} ▪{/color}" xpos 245 ypos 0.217

    imagebutton idle "ajuda/ctrl.png" hover "ajuda/ctrl.png" xpos 55 ypos 256 focus_mask True
    text "Pressionando, ativa o modo rápido." xanchor 1.0 xpos 0.74 ypos 0.35

    imagebutton idle "ajuda/tab.png" hover "ajuda/tab.png" xpos 55 ypos 354 focus_mask True
    text "Ativa ou Desativa o modo rápido." xanchor 1.0 xpos 0.74 ypos 0.475

    imagebutton idle "ajuda/scroll.png" hover "ajuda/scroll.png" xpos 70 ypos 446 focus_mask True
    text "Avança ou Retrocede na história." xanchor 1.0 xpos 0.74 ypos 0.60

    imagebutton idle "ajuda/h.png" hover "ajuda/h.png" xpos 55 ypos 543 focus_mask True
    imagebutton idle "ajuda/mid.png" hover "ajuda/mid.png" xpos 160 ypos 541 focus_mask True
    text "Oculta tudo e mostra o Backgroud." xanchor 1.0 xpos 0.74 ypos 0.73
    text "{color=#00f}▪{/color}" xpos 130 ypos 0.72

    imagebutton idle "ajuda/f.png" hover "ajuda/f.png" xpos 55 ypos 640 focus_mask True
    text "Alterna entre Janela e Tela Cheia." xanchor 1.0 xpos 0.74 ypos 0.85

    text "Ajuda" xanchor 0.5 xpos 0.873 ypos 45

    use botoes

## Tela de Pause
screen save:

    tag menu
    modal True

    image "system/layeradd.png"

    text "Pause" xanchor 0.5 xpos 0.873 ypos 45

    imagebutton idle "bt/btbackidle.png" hover "bt/btbackhover.png" xpos 800 ypos 100 focus_mask True action Return() activate_sound "menuselect.ogg" hover_sound "menuhover.ogg"
    imagebutton idle "bt/btoptionidle.png" hover "bt/btoptionhover.png" selected_idle "bt/btoptionselected.png" selected_hover "bt/btoptionselected.png" xpos 800 ypos 160 focus_mask  True action ShowMenu("preferences") activate_sound "menuselect.ogg" hover_sound "menuhover.ogg"
    imagebutton idle "bt/btsaveidle.png" hover "bt/btsavehover.png" selected_idle "bt/btsaveselected.png" selected_hover "bt/btsaveselected.png" insensitive "bt/btsaveground.png" xpos 800 ypos 220 focus_mask  True action ShowMenu("save2") activate_sound "menuselect.ogg" hover_sound "menuhover.ogg"
    imagebutton idle "bt/btloadidle.png" hover "bt/btloadhover.png" selected_idle "bt/btloadselected.png" selected_hover "bt/btloadselected.png" xpos 800 ypos 280 focus_mask  True action ShowMenu("load") activate_sound "menuselect.ogg" hover_sound "menuhover.ogg"
    imagebutton idle "bt/btmainidle.png" hover "bt/btmainhover.png" insensitive "bt/btmainground.png" xpos 800 ypos 340 focus_mask  True action MainMenu() activate_sound "menuselect.ogg" hover_sound "menuhover.ogg"
    imagebutton idle "bt/bthelpidle.png" hover "bt/bthelphover.png" selected_idle "bt/bthelpselected.png" selected_hover "bt/bthelpselected.png" xpos 800 ypos 400 focus_mask True action ShowMenu("helps") activate_sound "menuselect.ogg" hover_sound "menuhover.ogg"
    imagebutton idle "bt/btexitidle.png" hover "bt/btexithover.png" xpos 800 ypos 460 focus_mask  True action Quit() activate_sound "menuselect.ogg" hover_sound "menuhover.ogg"

    #key "K_ESCAPE" action Hide("pausegame")
    #window:
        #style "menu_pause"
        #id "my_id"
        #align (0.0, 0.0)
        #at my_transf
        #xmargin 10
        #ymargin 10
    #frame:
    #    xfill True
    #    xmargin 10
    #    ymargin 10
    #    hbox:
    #        text " Pause"




#screen mymenu:
#    key "mousedown_3" action If(renpy.get_screen("pausegame"), Hide("pausegame"), Show("pausegame"))
#    key "K_ESCAPE" action If(renpy.get_screen("pausegame"), Hide("pausegame"), Show("pausegame"))



######################################### Opções ######################################
screen preferences:

    tag menu

    # Incluye la navegación.
    use fundo

    text "Opções" xanchor 0.5 xpos 0.873 ypos 45

    use botoes

    # Coloca las columnas de navegación en una cuadrícula de anchura 3.
    grid 3 1:
        style_group "prefs"
        xfill True

        # Columna izquierda.
        vbox:
            xpos 100
            ypos 100

            frame:
                style_group "pref"
                has vbox

                label _("Display")
                textbutton _("Window") action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")

            #frame:
             #   style_group "pref"
              #  has vbox
#
 #               label _("Transitions")
  #              textbutton _("All") action Preference("transitions", "all")
   #             textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Joystick...") action Preference("joystick")

            frame:
                style_group "pref"
                has vbox

                label _("Velocidade do avanço automático")
                bar value Preference("auto-forward time")

            frame:
                style_group "pref"
                has vbox

                label _("Music Volume")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Sound Volume")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Test"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            if config.has_voice:
                frame:
                    style_group "pref"
                    has vbox

                    label _("Voice Volume")
                    bar value Preference("voice volume")

                    textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                    if config.sample_voice:
                        textbutton _("Test"):
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"

        vbox:
            #frame:
            style_group "pref"
            #    has vbox

              #  label _("Avanço Rápido")
               # textbutton _("Seen Messages") action Preference("skip", "seen")
                #textbutton _("All Messages") action Preference("skip", "all")

           # frame:
            #    style_group "pref"
             #   has vbox
#
 #               textbutton _("Begin Skipping") action Skip()

           # frame:
            #    style_group "pref"
             #   has vbox

              #  label _("After Choices")
               # textbutton _("Stop Skipping") action Preference("after choices", "stop")
               # textbutton _("Keep Skipping") action Preference("after choices", "skip")

         #   frame:
          #      style_group "pref"
           #     has vbox
#
 #               label _("Velocidade do avanço automático")
  #              bar value Preference("auto-forward time")

              #  if config.has_voice:
               #     textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")

        vbox:
            #frame:
            style_group "pref"
            #    has vbox
#
 #               label _("Music Volume")
  #              bar value Preference("music volume")
#
 #           frame:
  #              style_group "pref"
   #             has vbox
#
 #               label _("Sound Volume")
  #              bar value Preference("sound volume")
#
 #               if config.sample_sound:
  #                  textbutton _("Test"):
   #                     action Play("sound", config.sample_sound)
    #                    style "soundtest_button"

     #       if config.has_voice:
      #          frame:
       #             style_group "pref"
        #            has vbox
#
 #                   label _("Voice Volume")
  #                  bar value Preference("voice volume")
#
 #                   textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
  #                  if config.sample_voice:
   #                     textbutton _("Test"):
    #                        action Play("voice", config.sample_voice)
     #                       style "soundtest_button"



init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0


##############################################################################
# Pregunta Sí/No
#
# Pantalla que pregunta al usuario una pregunta Sí/No.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt:

    modal True

    #window:
    #    style "gm_root"
    image "system/exit_window.png"
    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        yalign .4
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5
            yalign 0.5

 #       hbox:
  #          xalign 0.5
   #         spacing 100

    imagebutton idle "bt/btsimidle.png" hover "bt/btsimhover.png" xpos 320 yalign 0.6 focus_mask True action yes_action activate_sound "menuselect.ogg" hover_sound "menuhover.ogg"
    imagebutton idle "bt/btnaoidle.png" hover "bt/btnaohover.png" xpos 520 yalign 0.6 focus_mask True action no_action activate_sound "menuselect.ogg" hover_sound "menuhover.ogg"
         #   textbutton _("Yes") action yes_action
    #        textbutton _("No") action no_action

    # Clic derecho y escape responden "no".
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"


##############################################################################
# Quick Menu - Menú de acceso rápido
#
# Pantalla incluida por defecto en la pantalla de diálogo, que añade acceso
# rápido a una serie de funciones útiles.
screen quick_menu:

    # Añade un menú de acceso rápido interno al juego.
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Save") action ShowMenu('save2')
        textbutton _("Quick Save") action QuickSave()
        textbutton _("Quick Load") action QuickLoad()
        textbutton _("Avanço Rápido") action Skip()
        textbutton _("Pular") action Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
       # textbutton _("Prefs") action ShowMenu('preferences')

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"
