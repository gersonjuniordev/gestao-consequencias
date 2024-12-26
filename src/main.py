import customtkinter as ctk
from interface import GestaoApp

def main():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
    
    app = GestaoApp()
    app.mainloop()

if __name__ == "__main__":
    main() 