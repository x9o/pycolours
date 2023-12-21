import os

class fade():
    def emerald(text: str):
        os.system("")
        faded = ""
        if len(text) <= 18:
            decrement = 10
        else:
            decrement = 4
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

    def chroma(text: str):
        os.system("")  # Enable ANSI escape sequences for coloring in Windows
        faded = ""
        if len(text) <= 18:
            decrement = 10
        else:
            decrement = 5
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

    def flame(text: str):
        os.system(""); faded = ""
        if len(text) <= 18:
            decrement = 10
        else:
            decrement = 5
        for line in text.splitlines():
            green = 250
            for character in line:
                green -= decrement
                if green < 0:
                    green = 0
                faded += (f"\033[38;2;255;{green};0m{character}\033[0m")
            faded += "\n"
        return faded
    
    def shadow(text: str):
        if len(text) <= 18:
            decrement = 10
        else:
            decrement = 4
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
    

    def gold(text: str):
        os.system("")  # Enable ANSI escape sequences for coloring in Windows
        faded = ""
        if len(text) <= 18:
            decrement = 10
        else:
            decrement = 5
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
    

def test():
    print(fade.flame(
    """

    ███████╗██╗░░░░░░█████╗░███╗░░░███╗███████╗
    ██╔════╝██║░░░░░██╔══██╗████╗░████║██╔════╝
    █████╗░░██║░░░░░███████║██╔████╔██║█████╗░░
    ██╔══╝░░██║░░░░░██╔══██║██║╚██╔╝██║██╔══╝░░
    ██║░░░░░███████╗██║░░██║██║░╚═╝░██║███████╗
    ╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝"""))
    print(fade.flame("Lorem Iaudoaifojsi fjsdogjiojviufiua nfsfgfdsohbjsofighsjihojdifogjdfigo"))
    print(fade.chroma("""


    ░█████╗░██╗░░██╗██████╗░░█████╗░███╗░░░███╗░█████╗░
    ██╔══██╗██║░░██║██╔══██╗██╔══██╗████╗░████║██╔══██╗
    ██║░░╚═╝███████║██████╔╝██║░░██║██╔████╔██║███████║
    ██║░░██╗██╔══██║██╔══██╗██║░░██║██║╚██╔╝██║██╔══██║
    ╚█████╔╝██║░░██║██║░░██║╚█████╔╝██║░╚═╝░██║██║░░██║
    ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝
                    
                    """))
    print(fade.chroma("Lorem Iaudoaifojsi fjsdogjiojviufiua nfsfgfdsohbjsofighsjihojdifogjdfigo"))
    print(fade.shadow("""
    ░██████╗██╗░░██╗░█████╗░██████╗░░█████╗░░██╗░░░░░░░██╗
    ██╔════╝██║░░██║██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║
    ╚█████╗░███████║███████║██║░░██║██║░░██║░╚██╗████╗██╔╝
    ░╚═══██╗██╔══██║██╔══██║██║░░██║██║░░██║░░████╔═████║░
    ██████╔╝██║░░██║██║░░██║██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░
    ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░
                    """))
    print(fade.shadow("Lorem Iaudoaifojsi fjsdogjiojviufiua nfsfgfdsohbjsofighsjihojdifogjdfigo"))
    print(fade.gold("""
    ░██████╗░░█████╗░██╗░░░░░██████╗░
    ██╔════╝░██╔══██╗██║░░░░░██╔══██╗
    ██║░░██╗░██║░░██║██║░░░░░██║░░██║
    ██║░░╚██╗██║░░██║██║░░░░░██║░░██║
    ╚██████╔╝╚█████╔╝███████╗██████╔╝
    ░╚═════╝░░╚════╝░╚══════╝╚═════╝░
                """))
    print(fade.gold("Lorem Iaudoaifojsi fjsdogjiojviufiua nfsfgfdsohbjsofighsjihojdifogjdfigo"))
    print(fade.emerald("""
    ███████╗███╗░░░███╗███████╗██████╗░░█████╗░██╗░░░░░██████╗░
    ██╔════╝████╗░████║██╔════╝██╔══██╗██╔══██╗██║░░░░░██╔══██╗
    █████╗░░██╔████╔██║█████╗░░██████╔╝███████║██║░░░░░██║░░██║
    ██╔══╝░░██║╚██╔╝██║██╔══╝░░██╔══██╗██╔══██║██║░░░░░██║░░██║
    ███████╗██║░╚═╝░██║███████╗██║░░██║██║░░██║███████╗██████╔╝
    ╚══════╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═════╝░"""))
    print(fade.emerald("Lorem Iaudoaifojsi fjsdogjiojviufiua nfsfgfdsohbjsofighsjihojdifogjdfigo"))



test()


