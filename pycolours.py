import os
import time

xl = len("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

class fade():


    def help():
        c = fade.chroma("Chroma Animation - fade.chroma_animation()", 6)
        chroma = fade.chroma("Chroma - << fade.chroma(text, intensity) >> ", 7)
        flame = fade.flame("Flame - << fade.chroma(text, intensity) >>", 6)
        shadow = fade.shadow("Shadow - << fade.shadow(text, intensity) >>", 3)
        gold = fade.gold("Gold - << fade.gold(text, intensity) >>", 5)
        emerald = fade.emerald("Emerald - << fade.emerald(text, intensity) >>", 6)
        wave = fade.wave("Wave - << fade.wave(text, intensity) >>", 10)
        glowr = fade.emerald("<< [!] Specifiying the intensity is recommended. >>")
        flmer = fade.flame("<< [-]  System will automatically pick an intensity if omitted. >>", 4)
        flmb = fade.flame("<< [!] Beta >>", 15)
        goldc = fade.gold("""
        - fade.help()
        - fade.test()
                          """, 10)
        

        print(f"""
        <<<< Colours >>>>
              
        
        {chroma}

        {flame}   

        {shadow}
        
        {gold}

        {emerald}
        
        {wave}


        ----------------------------------------------------------------------------------


        {flmer}
        
        {glowr}

      
        ----------------------------------------------------------------------------------

        <<<< Animations >>>>


        {c} 

        {flmb}

        ----------------------------------------------------------------------------------

        <<<< Commands >>>>

        {goldc}

              """)

    def wave(text: str, dec: int = None):
        if dec == None:
            if len(text) <= 18:
                decrement = 16
            elif len(text) > 280:
                decrement = 6
            else:
                decrement = 6
            
        else:
            decrement = dec
        os.system("")
        faded = ""
        for line in text.splitlines():
            green = 10
            for charcter in line:
                faded += (f"\033[38;2;0;{green};255m{charcter}\033[0m")
                green += decrement
                if green > 255:
                    green = 255
            faded += "\n"
        return faded


    def emerald(text: str, dec: int = None):
        os.system("")
        faded = ""
        if dec == None:
            if len(text) <= 18:
                decrement = 10
            else:
                decrement = 3
        else:
            decrement = dec
        for line in text.splitlines():
            red = 255
            blue = 255
            for character in line:
                faded += (f"\033[38;2;{red};255;{blue}m{character}\033[0m")
                red -= decrement
                blue -= decrement
                if red < 0:
                    red = 0
                if blue < 0:
                    blue = 0
            faded += "\n"
        return faded

    def chroma(text: str, dec: int = None):
        os.system("")  
        faded = ""
        if dec == None:
            if len(text) <= 18:
                decrement = 10
            else:
                decrement = 5
        else:
            decrement = dec
        for line in text.splitlines():
            blue = 255
            red = 0
            for character in line:
                blue -= decrement
                red += decrement
                if blue < 0:
                    blue = 0
                if red > 255:
                    red = 255
                faded += (f"\033[38;2;{red};0;{blue}m{character}\033[0m")
            faded += "\n"
        return faded

    def flame(text: str, dec: int = None):
        os.system(""); faded = ""
        if dec == None:
            if len(text) <= 18:
                decrement = 10
            else:
                decrement = 5
        else:
            decrement = dec
        for line in text.splitlines():
            green = 250
            for character in line:
                green -= decrement
                if green < 0:
                    green = 0
                faded += (f"\033[38;2;255;{green};0m{character}\033[0m")
            faded += "\n"
        return faded
    
    def shadow(text: str, dec: int = None):
        if dec == None:
            if len(text) <= 18:
                decrement = 10
            else:
                decrement = 4
        else:
            decrement = dec
        os.system(""); faded = ""
        for line in text.splitlines():
            white = 255
            for character in line:
                white -= decrement
                if white < 0:
                    white = 0
                faded += (f"\033[38;2;{white};{white};{white}m{character}\033[0m")
            faded += "\n"
        return faded
    

    def gold(text: str, dec: int = None):
        os.system("")  # Enable ANSI escape sequences for coloring in Windows
        faded = ""
        if dec == None:
            if len(text) <= 18:
                decrement = 10
            else:
                decrement = 5
        else:
            decrement = dec
        for line in text.splitlines():
            red = 255
            green = 165
            blue = 0
            for character in line:
                red += decrement
                green += decrement
                blue += decrement
                if red > 255:
                    red = 255
                if green > 255:
                    green = 255
                if blue > 255:
                    blue = 255
                faded += (f"\033[38;2;{red};{green};{blue}m{character}\033[0m")
            faded += "\n"
        return faded
    

    def chroma_animation(text: str, duration: float, frequency: float):
        os.system("") 
        faded = ""
        if len(text) <= 18:
            decrement = 10
        else:
            decrement = 5
        
        while True:
            start_time = time.time()
            elapsed_time = 0
            
            while elapsed_time < duration:
                elapsed_time = time.time() - start_time
                offset = elapsed_time * decrement
                
                
                for line in text.splitlines():
                    blue = 255
                    red = 0
                    for character in line:
                        blue -= offset
                        red += offset
                        if blue < 0:
                            blue = 0
                        if red > 255:
                            red = 255
                        faded += (f"\033[38;2;{int(red)};0;{int(blue)}m{character}\033[0m")
                    faded += "\n"
                os.system("cls")
                print(faded)
                faded = ""
                if elapsed_time >= duration:
                    break
                time.sleep(frequency)


    

    def test():
        global xl
        print(fade.flame(
        """

        ███████╗██╗░░░░░░█████╗░███╗░░░███╗███████╗
        ██╔════╝██║░░░░░██╔══██╗████╗░████║██╔════╝
        █████╗░░██║░░░░░███████║██╔████╔██║█████╗░░
        ██╔══╝░░██║░░░░░██╔══██║██║╚██╔╝██║██╔══╝░░
        ██║░░░░░███████╗██║░░██║██║░╚═╝░██║███████╗
        ╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝"""))
        
        sl = len("A a hot glowing body of ignited gas that is generated by something on fire.")
        print(fade.flame(f"A a hot glowing body of ignited gas that is generated by something on fire. Characters: {sl}"))
        print(fade.flame(f"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX Characters: {xl}"))
        print(fade.chroma("""


        ░█████╗░██╗░░██╗██████╗░░█████╗░███╗░░░███╗░█████╗░
        ██╔══██╗██║░░██║██╔══██╗██╔══██╗████╗░████║██╔══██╗
        ██║░░╚═╝███████║██████╔╝██║░░██║██╔████╔██║███████║
        ██║░░██╗██╔══██║██╔══██╗██║░░██║██║╚██╔╝██║██╔══██║
        ╚█████╔╝██║░░██║██║░░██║╚█████╔╝██║░╚═╝░██║██║░░██║
        ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝
                        
                        """))
        tl = len("The intensity or purity of a color, representing its departure from a neutral gray of the same lightness.")

        print(fade.chroma(f"The intensity or purity of a color, representing its departure from a neutral gray of the same lightness. Characters: {tl}"))
        print(fade.chroma(f"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX Characters: {xl}"))
        print(fade.shadow("""
        ░██████╗██╗░░██╗░█████╗░██████╗░░█████╗░░██╗░░░░░░░██╗
        ██╔════╝██║░░██║██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║
        ╚█████╗░███████║███████║██║░░██║██║░░██║░╚██╗████╗██╔╝
        ░╚═══██╗██╔══██║██╔══██║██║░░██║██║░░██║░░████╔═████║░
        ██████╔╝██║░░██║██║░░██║██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░
        ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░
                        """))
        
        al = len("A dark area or shape produced by an object blocking light, creating a contrast between illuminated and non-illuminated regions.")
        print(fade.shadow(f"A dark area or shape produced by an object blocking light, creating a contrast between illuminated and non-illuminated regions. Characters: {al}"))
        print(fade.shadow(f"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX Characters: {xl}"))
        print(fade.gold("""
        ░██████╗░░█████╗░██╗░░░░░██████╗░
        ██╔════╝░██╔══██╗██║░░░░░██╔══██╗
        ██║░░██╗░██║░░██║██║░░░░░██║░░██║
        ██║░░╚██╗██║░░██║██║░░░░░██║░░██║
        ╚██████╔╝╚█████╔╝███████╗██████╔╝
        ░╚═════╝░░╚════╝░╚══════╝╚═════╝░
                    """))
        gl = len("Warm, metallic yellow hue that resembles the appearance of the metal gold.")
        print(fade.gold(f"Warm, metallic yellow hue that resembles the appearance of the metal gold. Characters: {gl}"))
        print(fade.gold(f"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX Characters: {xl}"))
        print(fade.emerald("""
        ███████╗███╗░░░███╗███████╗██████╗░░█████╗░██╗░░░░░██████╗░
        ██╔════╝████╗░████║██╔════╝██╔══██╗██╔══██╗██║░░░░░██╔══██╗
        █████╗░░██╔████╔██║█████╗░░██████╔╝███████║██║░░░░░██║░░██║
        ██╔══╝░░██║╚██╔╝██║██╔══╝░░██╔══██╗██╔══██║██║░░░░░██║░░██║
        ███████╗██║░╚═╝░██║███████╗██║░░██║██║░░██║███████╗██████╔╝
        ╚══════╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═════╝░"""))
        el = len("A rich green hue reminiscent of the gemstone emerald.")
        print(fade.emerald(f"A rich green hue reminiscent of the gemstone emerald. Characters: {el}"))
        print(fade.emerald(f"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX Characters: {xl}"))
        print(fade.wave("""
                                
        ░██╗░░░░░░░██╗░█████╗░██╗░░░██╗███████╗
        ░██║░░██╗░░██║██╔══██╗██║░░░██║██╔════╝
        ░╚██╗████╗██╔╝███████║╚██╗░██╔╝█████╗░░
        ░░████╔═████║░██╔══██║░╚████╔╝░██╔══╝░░
        ░░╚██╔╝░╚██╔╝░██║░░██║░░╚██╔╝░░███████╗
        ░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝"""))
        wl = len("The great great great great great great great great great blue oceanic sea.")
        print(fade.wave(f"The great great great great great great great great great blue oceanic sea. Characters: {wl}"))
        print(fade.wave(f"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX Characters: {xl}"))



    def animations():

        text = """


        ░█████╗░██╗░░██╗██████╗░░█████╗░███╗░░░███╗░█████╗░
        ██╔══██╗██║░░██║██╔══██╗██╔══██╗████╗░████║██╔══██╗
        ██║░░╚═╝███████║██████╔╝██║░░██║██╔████╔██║███████║
        ██║░░██╗██╔══██║██╔══██╗██║░░██║██║╚██╔╝██║██╔══██║
        ╚█████╔╝██║░░██║██║░░██║╚█████╔╝██║░╚═╝░██║██║░░██║
        ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝
                        
                        """

        duration = 10  # Animation duration in seconds
        speed = 0.01
        
        fade.chroma_animation(text, duration, speed)
