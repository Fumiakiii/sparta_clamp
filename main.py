import tkinter as tk
from ui.interface import create_interface

if __name__ == '__main__':
    root = tk.Tk()
    root.title('スパルタアプリ')
    create_interface(root)
    root.mainloop() 