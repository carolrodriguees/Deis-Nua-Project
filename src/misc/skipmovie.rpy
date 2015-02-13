##########
# Videos #
##########

#Opening Fate
label videofate:
    $ videocheck = "fate"
    show movie
    play movie "videos/#introfate.ogv"
    jump pausevideo
        
#Opening Unlimited Blade Works
label videobone:
    $ videocheck = "bone"
    show movie
    play movie "videos/#introbone.ogv" 
    jump pausevideo
        
#Opening Haven's Feel
label videofeels:
    $ videocheck = "feels"
    show movie
    play movie "videos/#introfeels.ogv"
    jump pausevideo

#Método de pausa
label pausevideo:
    $ renpy.pause()
    if renpy.pause() == True:
        jump skipvideo

#Choice durante o vídeo
label skipvideo:
    menu video:
        "Seguir na história":
            stop movie
            hide movie
            return
        "Continuar vendo o vídeo":
            jump pausevideo
        "Reiniciar vídeo":
            if videocheck == "fate":
                jump videofate
            elif videocheck == "bone":
                jump videobone
            elif videocheck == "feels":
                jump videofeels
