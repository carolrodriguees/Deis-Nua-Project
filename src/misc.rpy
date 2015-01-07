
#Personagens

#Mestres
#define narrador = Character(None, kind=nvl)
#define rin = Character("Tohsaka Rin")
#define shirou = Character("Emiya Shirou")
#define kirei = Character("Kotomine Kirei")
#define professor = Character("Kuzuki Souichirou")
#define shinji = Character("Matou Shinji")
#define illya = Character("Illyasviel von Einzbern")

#Servos
#define saber = Character("Saber")
#define archer = Character("Archer")
#define lancer = Character("Lancer")
#define berserker = Character("Berserker")
#define rider = Character("Rider")
#define assassin = Character("Assassin")
#define caster = Character("Caster")

#Supporting
#define gilgamesh = Character("Gilgamesh")
#define leysritt = Character("Leysritt")
#define sella = Character("Sella")
#define emiya = Character("Emiya Kiritsugu")
#define tiger = Character("Fujimura Taiga")
#define kane = Character("Himuro Kane")
#define kaede = Character("Makidera Kaede")
#define sakura = Character("Matou Sakura")
#define ayako = Character("Mitsuzuri Ayako")
#define issei = Character("Ryuudou Issei")
#define yukika = Character("Saegusa Yukika")

# Botones del menú principal.
    #frame:
     #   style_group "mm"
      #  xalign .98
       # yalign .98
#
 #       has vbox
#
 #       textbutton _("Start Game") action Start()
  #      textbutton _("Load Game") action ShowMenu("load")
   #     textbutton _("Preferences") action ShowMenu("preferences")
    #    textbutton _("Help") action Help()
     #   textbutton _("Quit") action Quit(confirm=False)
