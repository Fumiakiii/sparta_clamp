import tkinter as tk

# Function to create the main interface

def create_interface(root):
    # Create a frame for the title
    title_frame = tk.Frame(root)
    title_frame.pack(pady=10)
    
    # Title label
    title_label = tk.Label(title_frame, text='スパルタアプリ', font=('Helvetica', 24, 'bold'))
    title_label.pack()
    
    # Create a frame for level descriptions
    level_frame = tk.Frame(root)
    level_frame.pack(pady=20)
    
    # Level 1 description
    level1_label = tk.Label(level_frame, text='レベル1: 八幡平市のふるさと納税を購入', font=('Helvetica', 16))
    level1_label.pack(anchor='w')
    
    # Level 2 description
    level2_label = tk.Label(level_frame, text='レベル2: ランダムで仮想通貨を購入', font=('Helvetica', 16))
    level2_label.pack(anchor='w')
    
    # Level 3 description
    level3_label = tk.Label(level_frame, text='レベル3: スパルタアプリへの課金', font=('Helvetica', 16))
    level3_label.pack(anchor='w') 