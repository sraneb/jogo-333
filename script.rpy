# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define G = Character("Genji")

define V = Character("Você ")

define H = Character ("Hanzo")

define L = Character ("Lula")

define c = Character ("Criadores")

image genji normal= "image/genji2.png"
image fundo ="image/bg fundo.jpg"
# The game starts here.

label start:

    play music "audio/sorry mom.mpeg"
    scene bg fundo2
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg fundo:
        zoom 2 

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show genji2:
        zoom 2
    # These display lines of dialogue.
    


    G "olá jogador,"
    G "Gostaria de me ajudar  a trazer a paz para esse mundo" 



menu:  
     "Sim":
        show genji3:
            zoom 2


        hide genji2

        G"Então pegue uma espada e me ajude a matar meu irmão "
        G"okay... eu ouvi rumores que ele esta no brasil"
        G"vamos para lá "
        
        scene bg rio
        show genji4:
            zoom 3
        G"chegamos ao rio aonde tem mais bala perdida do que estrela no céu"
        G" ouvi dizer que ele esta em alguma favela por aqui"
        L"olhaaa a pikanha"
        show pikanha:
            zoom 3
        hide genji4
        with pixellate
        hide pikanha
        show genji4 at right:
            zoom 2
        show lulinha:
            zoom 2
        G"Bom...se vc não quiser perder outro dedo me fala aonde esta o hanzo" 
        L"okok"
        L" ele esta dentro da favela"
        G"se for mentira eu volto para de pegar" 
        hide lulinha 
        hide genji4 
        scene bg favela:  
            zoom 0.5
        show genji3:
                zoom 2 
        G"demorou mas te encontrei meu irmão"
        show hanzo at right:
            zoom 2
        H"vc tem duas escolha meu irmão" 
        H"eu vou conseguir a honra que vc roubou de mim"  

        V"os dois parem de brigar pois eu to com preguiça de fazer o resto"   

        scene bg preto:
            zoom 10
        
        c"espero que tenha se divertindo"
        c"esperamos voce no nosso proximo jogo" 

      

     "Não":
        hide genji2
        show genji3:
            zoom 2

        G"ah sim... você ajudaria bastente!"
        G "Tchau!"

   



