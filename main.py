import random
import tkinter as tk
from tkinter import font
from tkinter import ttk
import cases_list





drops_rates = {
    "Blue": 79.92,
    "Purple": 15.98,
    "Pink": 3.20,
    "Red": .64,
    "Gold": .26
}

# FLOATS RANGE FROM: 0.00000000000001 - 0.99999999999999 (14 DIGITS)
floats = {
    "Battle Scarred": [0.44, 1.0],
    "Well Worn": [0.37, 0.44],
    "Field Tested": [0.15, 0.37],
    "Minimal Wear": [0.07, 0.15],
    "Factory New": [0.00, 0.07]
}



cases = 0
total_spent = 0
key_price = 2.49
inventory = []
inventory_value = 0
profit = 0
roi = 0
lowest_float_value = 0.0
blues = 0
purples = 0
pinks = 0
pink_dry_streak = 0
average_pink_dry_streak_list = []
reds = 0
first_red = []
red_dry_streak = 0
average_red_dry_streak_list = []
golds = 0
first_gold = []
gold_dry_steak = 0
average_gold_dry_streak_list = []
most_valuable = None
best_drop_text = None

kilowatt_count = 0
horizon_count = 0
revolution_count = 0
spectrum_count = 0
recoil_count = 0

top_ten = []
top_ten_floats = []

average_float_list = []
average_float = 0.0

total_blues_value = 0
total_purples_value = 0
total_pinks_value = 0
total_reds_value = 0
total_golds_value = 0

blue_pct = f"{(blues / cases) * 100:.2f}" if cases > 0 else "0.00"
purple_pct = f"{(purples / cases) * 100:.2f}" if cases > 0 else "0.00"
pink_pct = f"{(pinks / cases) * 100:.2f}" if cases > 0 else "0.00"
red_pct = f"{(reds / cases) * 100:.2f}" if cases > 0 else "0.00"
gold_pct = f"{(golds / cases) * 100:.2f}" if cases > 0 else "0.00"

battle_scarred_count = 0
well_worn_count = 0
field_tested_count = 0
minimal_wear_count = 0
factory_new_count = 0

battle_scarred_st = 0
well_worn_st = 0
field_tested_st = 0
minimal_wear_st = 0
factory_new_st = 0

blue_st = 0
purple_st = 0
pink_st = 0
red_st = 0
gold_st = 0




root = tk.Tk()
root.title("CS2 CASE SIM")
root.geometry("1920x1080")  
root.configure(bg="#1e1e1e")

root.grid_rowconfigure(0, weight=0)  # top section fixed
root.grid_rowconfigure(1, weight=1)  # inventory section expands

root.grid_columnconfigure(0, weight=1)


style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", background="#2b2b2b", foreground="white", fieldbackground="#2b2b2b", rowheight=25)
style.map("Treeview", background=[("selected", "#4a4a4a")])


# Top Frame for Stats & Button
top_frame = tk.Frame(root, background="red")
top_frame.grid(row=0, column=0)

top_frame.grid_columnconfigure(0, weight=1)  # stats
top_frame.grid_columnconfigure(1, weight=1)  # sim stats
top_frame.grid_columnconfigure(2, weight=1)  # top ten

top_frame.grid_columnconfigure(3, weight=0)  # controls
top_frame.grid_columnconfigure(4, weight=0)  # buttons

bottom_frame = tk.Frame(root, background="yellow")
bottom_frame.grid(row=1, column=0, sticky='nesw')

bottom_frame.grid_rowconfigure(0, weight=1)
bottom_frame.grid_columnconfigure(0, weight=1)

main_stats_frame = tk.Frame(top_frame, background="pink")
main_stats_frame.grid(row=0, column=0, sticky='nesw')
stats_text = tk.Text(
    main_stats_frame,
    width=90,
    height=40,
    bg="#1e1e1e",
    fg="white",
    borderwidth=0,
    
)

stats_text.grid(row=0, column=0, sticky='nesw')


sim_stats_frame = tk.Frame(top_frame, background="pink")
sim_stats_frame.grid(row=0, column=1, sticky='nesw')
sim_stats_text = tk.Text(
    sim_stats_frame,
    width=90,
    height=40,
    bg="#1e1e1e",
    fg="white",
    borderwidth=0,
    
)

sim_stats_text.grid(row=0, column=0, sticky='nesw')




# Stats Labels
# stat_font = font.Font(family="Weghorst-Italic", size=14)
# stats_label = tk.Label(
#     top_frame, 
#     text="Total Spent: $0.00 \n Inventory Value: $0.00 \n ROI: 0% \n Cases: 0 \n\n Lowest Float: N/A \n Average Float: 0 \n\n Blues: 0 (0%) | $0 \n\n Purples: 0 (0%) | $0 \n\n Pinks: 0 (0%) | $0 \n Pink Dry Streak: 0 \n Average Pink Dry Streak: 0 \n\n Reds: 0 (0%) | $0 \n First Red: 0 \n Total Spent for First Red: $0 \n Red Dry Streak: 0 \n Average Red Dry Streak: 0 \n\n Golds: 0 (0%) | $0 \n First Gold: 0 \n Total Spent for First Gold: $0 \n Gold Dry Steak: 0 \n Average Gold Dry Steak: 0 \n\n Battle Scarred: 0 \n Well-Worn: 0 \n Field Tested: 0 \n Minimal Wear: 0 \n Factory New: 0", 
#     font=(stat_font), 
#     fg="#ecf0f1", 
#     bg="#1e1e1e",
#     justify="center"
# )
# stats_label.pack(side="left", anchor="center", expand=True, fill="both")

# mass_open_label = tk.Label(
#     top_frame,
#     text="MASS OPENING: \n\n Players: 0 \n Cases: 0 \n Total Cases Opened: 0 \n Total Spent: $0 \n Total Blues: 0 \n Total Purples: 0 \n Total Pinks: 0 \n Total Reds: 0 \n Total Golds: 0",
#     font=(stat_font), 
#     fg="#ecf0f1", 
#     bg="#1e1e1e",
#     justify="center"
# )
# mass_open_label.pack(side="right", anchor="center", expand=True, fill="both")

top_ten_frame = tk.Frame(top_frame, 
                         background="green",
                         width=300,
                         height=300)
top_ten_frame.grid(row=0, column=2, sticky='nsew')
top_ten_text = tk.Text(
    top_ten_frame,
    width=90,
    height=40,
    bg="#1e1e1e",
    fg="white",
    borderwidth=0,   
)
top_ten_text.grid(row=0, column=0, sticky='nesw')
top_ten_floats_text = tk.Text(
    top_ten_frame,
    width=90,
    height=40,
    bg="#1e1e1e",
    fg="white",
    borderwidth=0,   
)
top_ten_text.grid(row=1, column=0, sticky='nesw')






player_entry_frame = tk.Frame(top_frame, background="purple")
player_entry_frame.grid(row=0, column=3, sticky='nesw')

players_entry_label = tk.Label(player_entry_frame, text="Players", fg="#ecf0f1", 
    bg="#1e1e1e",)
players_entry_label.grid(row=0, column=0, sticky='nesw', padx=5, pady=5)
players_entry_input = tk.IntVar(player_entry_frame)
players_entry = tk.Entry(player_entry_frame, textvariable=players_entry_input)
players_entry.grid(row=1, column=0, sticky='nesw', padx=5, pady=5)

cases_entry_label = tk.Label(player_entry_frame, text="Cases", fg="#ecf0f1", 
    bg="#1e1e1e",)
cases_entry_label.grid(row=2, column=0, sticky='nesw', padx=5, pady=5)
cases_entry_input = tk.IntVar(player_entry_frame)
cases_entry = tk.Entry(player_entry_frame, textvariable=cases_entry_input)
cases_entry.grid(row=3, column=0, sticky='nesw', padx=5, pady=5)

skip_animation_var = tk.BooleanVar(value=False)

skip_checkbox = tk.Checkbutton(
    player_entry_frame,
    text="Skip Animation",
    variable=skip_animation_var,
    font=("Arial", 10, "bold"),
    fg="#ecf0f1",
    bg="#1e1e1e",
    activebackground="#1e1e1e",
    activeforeground="#ecf0f1",
    selectcolor="#2b2b2b" # Changes the check box square background color
)
skip_checkbox.grid(row=4, column=0, sticky='nesw', padx=5, pady=5)



animation_running = False
ticker_items = []
current_offset = 0
velocity = 0
winning_item_data = None

TIER_COLORS = {
    "Blue": "#5c75cd",
    "Purple": "#9d0aff",
    "Pink": "#e17cf8",
    "Red": "#eb3434",
    "Gold": "#e0a91b"
}

# anim_frame = tk.Frame(root, bg="#1a1a1a", height=120)
# anim_frame.pack(fill="x", padx=20, pady=10)


# roll_canvas = tk.Canvas(anim_frame, width=700, height=100, bg="#222222", highlightthickness=2, highlightbackground="#3a3a3a")
# roll_canvas.pack(anchor="center")


# roll_canvas.create_line(350, 0, 350, 100, fill="#eb3434", width=3, tags="needle")




# Inventory Display Setup (The List View)
tree_frame = tk.Frame(bottom_frame)
tree_frame.grid(row=0, column=0, sticky='nesw')

tree_frame.grid_rowconfigure(0, weight=1)
tree_frame.grid_columnconfigure(0, weight=1)

# Scrollbar for list view
tree_scroll = ttk.Scrollbar(tree_frame)


# Columns
columns = ("item", "tier", "wear", "float", "price", "total spent")
inventory_list = ttk.Treeview(tree_frame, columns=columns, show="headings", yscrollcommand=tree_scroll.set)
tree_scroll.config(command=inventory_list.yview)


# Format Column Headers and Widths
inventory_list.heading("item", text="Weapon Skin")
inventory_list.heading("tier", text="Tier")
inventory_list.heading("wear", text="Wear Condition")
inventory_list.heading("float", text="Float Value")
inventory_list.heading("price", text="Value")
inventory_list.heading("total spent", text="Total Spent")

inventory_list.column("item", width=180, anchor="w")
inventory_list.column("tier", width=70, anchor="center")
inventory_list.column("wear", width=110, anchor="center")
inventory_list.column("float", width=140, anchor="center")
inventory_list.column("price", width=70, anchor="center")
inventory_list.column("total spent", width=50, anchor="e")

# Color tags for rarity highlighting
inventory_list.tag_configure("Blue", foreground="#5c75cd")
inventory_list.tag_configure("Purple", foreground="#9d0aff")
inventory_list.tag_configure("Pink", foreground="#e17cf8")
inventory_list.tag_configure("Red", foreground="#eb3434")
inventory_list.tag_configure("Gold", foreground="#e0a91b")

inventory_list.grid(row=0, column=0, sticky="nsew")

tree_scroll.grid(row=0, column=1, sticky="ns")


def update_top_ten():
    global top_ten, top_ten_floats

    

    if not inventory:
        top_ten_text.insert(tk.END, "No items yet.")
        return

    top_ten = sorted(
        inventory,
        key=lambda item: item["Price"],
        reverse=True
    )[:10]

    top_ten_floats = sorted(
        inventory,
        key=lambda item: item["Float"],
        reverse=False
    )[:10]

    top_ten_text.insert(tk.END, "TOP 10 MOST VALUABLE\n\n")

    for rank, item in enumerate(top_ten, start=1):
        if item["Tier"] == "Blue":
            top_ten_text.insert(
                tk.END,
                f"{rank}. {item['Item']}: ", "Blue"
            )
            top_ten_text.insert(
                tk.END,
                f"{item['Float']:.8f} | ", "defaults"
            )
            top_ten_text.insert(
                tk.END,
                f" ${item['Price']:,.2f}\n", "money"
            )
        elif item["Tier"] == "Purple":
            top_ten_text.insert(
                tk.END,
                f"{rank}. {item['Item']}: ", "Purple"
            )
            top_ten_text.insert(
                tk.END,
                f"{item['Float']:.8f} | ", "defaults"
            )
            top_ten_text.insert(
                tk.END,
                f" ${item['Price']:,.2f}\n", "money"
            )
        elif item["Tier"] == "Pink":
            top_ten_text.insert(
                tk.END,
                f"{rank}. {item['Item']}: ", "Pink"
            )
            top_ten_text.insert(
                tk.END,
                f"{item['Float']:.8f} | ", "defaults"
            )
            top_ten_text.insert(
                tk.END,
                f" ${item['Price']:,.2f}\n", "money"
            )
        elif item["Tier"] == "Red":
            top_ten_text.insert(
                tk.END,
                f"{rank}. {item['Item']}: ", "Red"
            )
            top_ten_text.insert(
                tk.END,
                f"{item['Float']:.8f} | ", "defaults"
            )
            top_ten_text.insert(
                tk.END,
                f" ${item['Price']:,.2f}\n", "money"
            )
        else:
            top_ten_text.insert(
                tk.END,
                f"{rank}. {item['Item']}: ", "Gold"
            )
            top_ten_text.insert(
                tk.END,
                f"{item['Float']:.8f} | ", "defaults"
            )
            top_ten_text.insert(
                tk.END,
                f" ${item['Price']:,.2f}\n", "money"
            )

    top_ten_text.insert(tk.END, "\n\n")


    top_ten_text.insert(tk.END, "TOP 10 LOWEST FLOATS \n\n")

    for rank, item in enumerate(top_ten_floats, start=1):
        if item["Tier"] == "Blue":
            top_ten_text.insert(
                tk.END,
                f"{rank}. {item['Item']}: ", "Blue"
            )
            top_ten_text.insert(
                tk.END,
                f"{item['Float']:.14f}\n", "defaults"
            )
        elif item["Tier"] == "Purple":
            top_ten_text.insert(
                tk.END,
                f"{rank}. {item['Item']}: ", "Purple"
            )
            top_ten_text.insert(
                tk.END,
                f"{item['Float']:.14f}\n", "defaults"
            )
        elif item["Tier"] == "Pink":
            top_ten_text.insert(
                tk.END,
                f"{rank}. {item['Item']}: ", "Pink"
            )
            top_ten_text.insert(
                tk.END,
                f"{item['Float']:.14f}\n", "defaults"
            )
        elif item["Tier"] == "Red":
            top_ten_text.insert(
                tk.END,
                f"{rank}. {item['Item']}: ", "Red"
            )
            top_ten_text.insert(
                tk.END,
                f"{item['Float']:.14f}\n", "defaults"
            )
        else:
            top_ten_text.insert(
                tk.END,
                f"{rank}. {item['Item']}: ", "Gold"
            )
            top_ten_text.insert(
                tk.END,
                f"{item['Float']:.14f}\n", "defaults"
            )
            


def update_ui_stats():
    """Updates the statistics label text at the top."""
    global total_spent, inventory_value, cases, blues, purples, pinks, reds, golds, first_red, first_gold, profit, most_valuable, best_drop_text
    global total_blues_value, total_purples_value, total_pinks_value, total_reds_value, total_golds_value
    global pink_dry_streak, red_dry_streak, gold_dry_steak, average_pink_dry_streak_list, average_red_dry_streak_list, average_gold_dry_streak_list, average_float_list
    global battle_scarred_count, well_worn_count, field_tested_count, minimal_wear_count, factory_new_count, roi, lowest_float_value
    global blue_pct, purple_pct, pink_pct, red_pct, gold_pct
    global kilowatt_count, horizon_count, revolution_count, spectrum_count, recoil_count

    most_valuable = highest_price()

    
    
    
    if total_spent > 0:
        roi = ((inventory_value - total_spent) / total_spent) * 100

    best_drop = lowest_float()

    if best_drop:
        lowest_float_value = best_drop["Float"]
        best_drop_text = f"{best_drop['Item']}: {lowest_float_value}"
    else:
        lowest_float_value = "N/A"
        best_drop_text = "N/A"


    avg_pink_dry_streak = (sum(average_pink_dry_streak_list) / len(average_pink_dry_streak_list)) if len(average_pink_dry_streak_list) > 0 else 0

    avg_red_dry_streak = (sum(average_red_dry_streak_list) / len(average_red_dry_streak_list)) if len(average_red_dry_streak_list) > 0 else 0

    avg_gold_dry_streak = (sum(average_gold_dry_streak_list) / len(average_gold_dry_streak_list)) if len(average_gold_dry_streak_list) > 0 else 0

    avg_float = (
    sum(average_float_list) / len(average_float_list)
    if average_float_list
    else 0
    )


    stats_text.delete("1.0", tk.END)
    sim_stats_text.delete("1.0", tk.END)
    top_ten_text.delete("1.0", tk.END)
    top_ten_floats_text.delete("1.0", tk.END)



    # PLAYER UI STATS
    sim_stats_text.tag_configure("money", foreground="#2ecc71")
    sim_stats_text.tag_configure("blues", foreground="#5c75cd")
    sim_stats_text.tag_configure("purples", foreground="#9d0aff")
    sim_stats_text.tag_configure("pinks", foreground="#e17cf8")
    sim_stats_text.tag_configure("reds", foreground="#eb3434")
    sim_stats_text.tag_configure("golds", foreground="#e0a91b")
    sim_stats_text.tag_configure("defaults", foreground="white")
    
    stats_text.tag_configure("money", foreground="#2ecc71")
    stats_text.tag_configure("blues", foreground="#5c75cd")
    stats_text.tag_configure("purples", foreground="#9d0aff")
    stats_text.tag_configure("pinks", foreground="#e17cf8")
    stats_text.tag_configure("reds", foreground="#eb3434")
    stats_text.tag_configure("golds", foreground="#e0a91b")
    stats_text.tag_configure("defaults", foreground="white")

    top_ten_text.tag_configure("Blue", foreground="#5c75cd")
    top_ten_text.tag_configure("Purple", foreground="#9d0aff")
    top_ten_text.tag_configure("Pink", foreground="#e17cf8")
    top_ten_text.tag_configure("Red", foreground="#eb3434")
    top_ten_text.tag_configure("Gold", foreground="#e0a91b")
    top_ten_text.tag_configure("money", foreground="#2ecc71")
    top_ten_text.tag_configure("defaults", foreground="white")

    top_ten_floats_text.tag_configure("blues", foreground="#5c75cd")
    top_ten_floats_text.tag_configure("purples", foreground="#9d0aff")
    top_ten_floats_text.tag_configure("pinks", foreground="#e17cf8")
    top_ten_floats_text.tag_configure("reds", foreground="#eb3434")
    top_ten_floats_text.tag_configure("golds", foreground="#e0a91b")
    top_ten_floats_text.tag_configure("money", foreground="#2ecc71")
    top_ten_floats_text.tag_configure("defaults", foreground="white")
    

    # TOTAL SPENT: $0.00
    stats_text.insert(tk.END, "Total Spend: ")
    stats_text.insert(tk.END, f"${total_spent:,.2f}\n", "money")

    # INVENTORY VALUE: $0.00
    stats_text.insert(tk.END, "Inventory Value: ")
    stats_text.insert(tk.END, f"${inventory_value:,.2f}\n", "money")

    # PROFIT: $0
    stats_text.insert(tk.END, f"Profit: ")

    if profit > 0:
        stats_text.insert(tk.END, f"${round(profit, 2):,}\n", "money")
    elif profit < 0:
        stats_text.insert(tk.END, f"${round(profit, 2):,}\n", "reds")
    else:
        stats_text.insert(tk.END, f"${round(profit, 2):,}\n", "defaults")

    # ROI: 0%
    stats_text.insert(tk.END, f"ROI: ")
    if roi > 0:
        stats_text.insert(tk.END, f"{round((((inventory_value - total_spent) / total_spent) * 100), 2) if total_spent > 0 else 0}%\n", "money")
    elif roi < 0:
        stats_text.insert(tk.END, f"{round((((inventory_value - total_spent) / total_spent) * 100), 2) if total_spent > 0 else 0}%\n", "reds")
    else:
        stats_text.insert(tk.END, f"{round((((inventory_value - total_spent) / total_spent) * 100), 2) if total_spent > 0 else 0}%\n", "defaults")

    # CASES: 0
    stats_text.insert(tk.END, f"Cases: {cases}\n\n")


    stats_text.insert(tk.END, f"Crates Opened:\n", "defaults")
    stats_text.insert(tk.END, f"Kilowatt: {kilowatt_count:,}\n")
    stats_text.insert(tk.END, f"Horizon: {horizon_count:,}\n")
    stats_text.insert(tk.END, f"Revolution: {revolution_count:,}\n")
    stats_text.insert(tk.END, f"Spectrum: {spectrum_count:,}\n")
    stats_text.insert(tk.END, f"Recoil: {recoil_count:,}\n\n")

    # AVERAGE FLOAT: 0
    stats_text.insert(tk.END, f"Average Float: {round(sum(average_float_list) / len(average_float_list), 14) if len(average_float_list) > 0 else 0.0}\n\n")

    # BLUES: 0 (0%) | $0
    sim_stats_text.insert(tk.END, f"Blues: {blues} ({blue_pct}%) | ", "blues")
    sim_stats_text.insert(tk.END, f"${total_blues_value:,.2f}\n", "money")
    sim_stats_text.insert(tk.END, f"Blue StatTraks: {blue_st:,} ({round((blue_st / blues) * 100, 2) if blues > 0 else 0}%)\n\n", "blues")

    # PURPLES: 0 (0%) | $0
    sim_stats_text.insert(tk.END, f"Purples: {purples} ({purple_pct}%) | ", "purples")
    sim_stats_text.insert(tk.END, f"${total_purples_value:,.2f}\n", "money")
    sim_stats_text.insert(tk.END, f"Purple StatTraks: {purple_st:,} ({round((purple_st / purples) * 100, 2) if purples > 0 else 0}%)\n\n", "purples")

    # PINKS: 0 (0%) | $0
    sim_stats_text.insert(tk.END, f"Pinks: {pinks} ({pink_pct}%) | ", "pinks")
    sim_stats_text.insert(tk.END, f"${total_pinks_value:,.2f}\n", "money")
    sim_stats_text.insert(tk.END, f"Pink StatTraks: {pink_st:,} ({round((pink_st / pinks) * 100, 2) if pinks > 0 else 0}%)\n", "pinks")
    # PINK DRY STREAK: 0
    sim_stats_text.insert(tk.END, f"Pink Dry Streak: {pink_dry_streak:,}\n", "pinks")
    # AVERAGE PINK DRY STREAK: 0
    sim_stats_text.insert(tk.END, f"Average Pink Dry Streak: {round((sum(average_pink_dry_streak_list) / len(average_pink_dry_streak_list)), 2) if len(average_pink_dry_streak_list) > 0 else 0}\n\n", "pinks")

    # REDS: 0 (0%) | $0
    sim_stats_text.insert(tk.END, f"Reds: {reds} ({red_pct}%) | ", "reds")
    sim_stats_text.insert(tk.END, f"${total_reds_value:,.2f}\n", "money")
    sim_stats_text.insert(tk.END, f"Red StatTraks: {red_st:,} ({round((red_st / reds) * 100, 2) if reds > 0 else 0}%)\n", "reds")
    # FIRST RED: 0
    sim_stats_text.insert(tk.END, f"First Red: {first_red[0] if first_red != [] else 0}\n", "reds")
    # TOTAL SPENT FOR FIRST RED: $0
    sim_stats_text.insert(tk.END, f"Total Spend for First Red: ", "reds")
    sim_stats_text.insert(tk.END, f"${(first_red[0] * (cases_list.kilowatt_case_base_price + key_price)) if reds > 0 else 0:,.2f}\n", "money")
    # RED DRY STREAK: 0
    sim_stats_text.insert(tk.END, f"Red Dry Streak: {red_dry_streak:,}\n", "reds")
    # AVERAGE RED DRY STREAK: 0
    sim_stats_text.insert(tk.END, f"Average Red Dry Streak: {round((sum(average_red_dry_streak_list) / len(average_red_dry_streak_list)), 2) if len(average_red_dry_streak_list) > 0 else 0}\n", "reds")
    # COST PER RED: $0
    sim_stats_text.insert(tk.END, f"Cost per Red: ", "reds")
    sim_stats_text.insert(tk.END, f"${round(total_spent / reds, 2) if reds > 0 else round(total_spent, 2)}\n\n", "money")

    # GOLDS: 0 (0%) | $0
    sim_stats_text.insert(tk.END, f"Golds: {golds} ({gold_pct}%) | ", "golds")
    sim_stats_text.insert(tk.END, f"${total_golds_value:,.2f}\n", "money")
    sim_stats_text.insert(tk.END, f"Gold StatTraks: {gold_st:,} ({round((gold_st / golds) * 100, 2) if golds > 0 else 0}%) \n", "golds")
    # FIRST GOLD: 0
    sim_stats_text.insert(tk.END, f"First Gold: {first_gold[0] if first_gold else 0}\n", "golds")
    # TOTAL SPENT FOR FIRST GOLD: $0
    sim_stats_text.insert(tk.END, f"Total Spent for First Gold: ", "golds")
    sim_stats_text.insert(tk.END, f"${(first_gold[0] * (cases_list.kilowatt_case_base_price + key_price)) if golds > 0 else 0:,.2f}\n", "money")
    # GOLD DRY STREAK: 0
    sim_stats_text.insert(tk.END, f"Gold Dry Streak: {gold_dry_steak:,}\n", "golds")
    # AVERAGE GOLD DRY STREAK: 0
    sim_stats_text.insert(tk.END, f"Average Gold Dry Streak: {round((sum(average_gold_dry_streak_list) / len(average_gold_dry_streak_list)), 2) if len(average_gold_dry_streak_list) > 0 else 0}\n", "golds")
    # COST PER GOLD: $0
    sim_stats_text.insert(tk.END, f"Cost per Gold: ", "golds")
    sim_stats_text.insert(tk.END, f"${round(total_spent / golds, 2) if golds > 0 else round(total_spent, 2):,}\n\n", "money")

    # BATTLE SCARRED: 0
    sim_stats_text.insert(tk.END, f"Battle Scarred: {battle_scarred_count:,} ({round((battle_scarred_count / cases) * 100, 2) if cases > 0 else 0}%) \n", "blues")
    sim_stats_text.insert(tk.END, f"Battle Scarred StatTrak: {battle_scarred_st:,} ({round((battle_scarred_st / battle_scarred_count) * 100) if battle_scarred_count > 0 else 0}%)\n", "blues")
    # WELL-WORN: 0
    sim_stats_text.insert(tk.END, f"Well-Worn: {well_worn_count:,} ({round((well_worn_count / cases) * 100, 2) if cases > 0 else 0}%)\n", "purples")
    sim_stats_text.insert(tk.END, f"Well-Worn StatTrak: {well_worn_st:,} ({round((well_worn_st / well_worn_count) * 100) if well_worn_count > 0 else 0}%)\n", "purples")
    # FIELD TESTED: 0
    sim_stats_text.insert(tk.END, f"Field Tested: {field_tested_count:,} ({round((field_tested_count / cases) * 100, 2) if cases > 0 else 0}%)\n", "pinks")
    sim_stats_text.insert(tk.END, f"Field Tested StatTrak: {field_tested_st:,} ({round((field_tested_st / field_tested_count) * 100) if field_tested_count > 0 else 0}%)\n", "pinks")
    # MINIMAL WEAR: 0
    sim_stats_text.insert(tk.END, f"Minimal Wear: {minimal_wear_count:,} ({round((minimal_wear_count / cases) * 100, 2) if cases > 0 else 0}%)\n", "reds")
    sim_stats_text.insert(tk.END, f"Minimal Wear StatTrak: {minimal_wear_st:,} ({round((minimal_wear_st / minimal_wear_count) * 100) if minimal_wear_count > 0 else 0}%)\n", "reds")
    # FACTORY NEW: 0
    sim_stats_text.insert(tk.END, f"Factory New: {factory_new_count:,} ({round((factory_new_count / cases) * 100, 2) if cases > 0 else 0}%)\n", "golds")
    sim_stats_text.insert(tk.END, f"Factory New StatTrak: {factory_new_st:,} ({round((factory_new_st / factory_new_count) * 100) if factory_new_count > 0 else 0}%)\n\n", "golds")


    profit = inventory_value - total_spent
    update_top_ten()


    ev_kilowatt = expected_case_value(cases_list.kilowatt_case)
    ev_horizon = expected_case_value(cases_list.horizon_case)
    ev_revolution = expected_case_value(cases_list.revolution_case)
    ev_spectrum = expected_case_value(cases_list.spectrum_case)
    ev_recoil = expected_case_value(cases_list.recoil_case)

    stats_text.insert(tk.END, "\nExpected Value (EV):\n", "defaults")
    stats_text.insert(
        tk.END,
        f"Kilowatt Case EV: ${ev_kilowatt:.2f}\n",
        "money"
    )
    stats_text.insert(
        tk.END,
        f"Net EV (Kilowatt): ${(ev_kilowatt - (cases_list.kilowatt_case_base_price + key_price)):.2f}\n\n",
        "money" if ev_kilowatt > (cases_list.kilowatt_case_base_price + key_price) else "reds"

    )
    stats_text.insert(
        tk.END,
        f"Horizon Case EV: ${ev_horizon:.2f}\n",
        "money"
    )
    stats_text.insert(
        tk.END,
        f"Net EV (Horizon): ${(ev_horizon - (cases_list.horizon_case_base_price + key_price)):.2f}\n\n",
        "money" if ev_horizon > (cases_list.horizon_case_base_price + key_price) else "reds"

    )
    stats_text.insert(
        tk.END,
        f"Revolution Case EV: ${ev_revolution:.2f}\n",
        "money"
    )
    stats_text.insert(
        tk.END,
        f"Net EV (Revolution): ${(ev_revolution - (cases_list.revolution_case_base_price + key_price)):.2f}\n\n",
        "money" if ev_revolution > (cases_list.revolution_case_base_price + key_price) else "reds"

    )
    stats_text.insert(
        tk.END,
        f"Spectrum Case EV: ${ev_spectrum:.2f}\n",
        "money"
    )
    stats_text.insert(
        tk.END,
        f"Net EV (Spectrum): ${(ev_spectrum - (cases_list.spectrum_case_base_price + key_price)):.2f}\n\n",
        "money" if ev_spectrum > (cases_list.spectrum_case_base_price + key_price) else "reds"

    )
    stats_text.insert(
        tk.END,
        f"Recoil Case EV: ${ev_recoil:.2f}\n",
        "money"
    )
    stats_text.insert(
        tk.END,
        f"Net EV (Recoil): ${(ev_recoil - (cases_list.recoil_case_base_price + key_price)):.2f}\n\n",
        "money" if ev_recoil > (cases_list.recoil_case_base_price + key_price) else "reds"

    )

    # stats_label.config(text=f"Total Spent: ${total_spent:,.2f} \n Inventory Value: ${inventory_value:,.2f} \n Return: {roi:,.1f}% \n Cases: {cases:,} \n\n Lowest Float: {best_drop_text} \n Average Float: {avg_float} \n\n Blues: {blues:,} ({blue_pct}%) | ${total_blues_value:,.2f} \n\n Purples: {purples:,} ({purple_pct}%) | ${total_purples_value:,.2f} \n\n Pinks: {pinks:,} ({pink_pct}%) | ${total_pinks_value:,.2f} \n Pink Dry Streak: {pink_dry_streak} \n Average Pink Dry Streak: {avg_pink_dry_streak:.2f} \n\n Reds: {reds:,} ({red_pct}%) | ${total_reds_value:,.2f} \n First Red: {first_red[0] if reds > 0 else 0} \n Total Spent for First Red: ${(first_red[0] * (kilowatt_case_base_price + key_price)) if reds > 0 else 0:,.2f} \n Red Dry Streak: {red_dry_streak} \n Average Red Dry Streak: {avg_red_dry_streak:.2f} \n\n Golds: {golds:,} ({gold_pct}%) | ${total_golds_value:,.2f} \n First Gold: {first_gold[0] if golds > 0 else 0} \n Total Spent for First Gold: ${(first_gold[0] * (kilowatt_case_base_price + key_price)) if golds > 0 else 0:,.2f} \n Gold Dry Steak: {gold_dry_steak} \n Average Gold Dry Streak: {avg_gold_dry_streak:.2f} \n\n Battle Scarred: {battle_scarred_count} \n Well-Worn: {well_worn_count} \n Field Tested: {field_tested_count} \n Minimal Wear: {minimal_wear_count} \n Factory New: {factory_new_count}", justify="center")


def mass_open():
    # Bring in all the global tracking counters
    global inventory_value, total_spent, cases, blues, purples, pinks, reds, golds, total_blues_value, total_purples_value, total_pinks_value, total_reds_value, total_golds_value
    global battle_scarred_count, well_worn_count, field_tested_count, minimal_wear_count, factory_new_count
    
    # 1. Grab inputs safely from the Entry widgets
    try:
        num_players = players_entry_input.get()
        cases_per_player = cases_entry_input.get()
    except (tk.TclError, ValueError):
        # Fallback safety if the user leaves input blank or types text
        return

    # Calculate total workload for this mass simulation
    total_mass_cases = num_players * cases_per_player
    if total_mass_cases <= 0:
        return

    # 2. Local batch counters (speeds up calculation significantly)
    batch_blues = 0
    batch_purples = 0
    batch_pinks = 0
    batch_reds = 0
    batch_golds = 0
    batch_value = 0.0

    # Hold items to append to treeview in a single fast loop
    batch_drops = []

    # 3. Mass loop simulation
    for _ in range(total_mass_cases):
        cases += 1  # Increment global case tracker
        
        # Roll Tier
        random_number = random.uniform(0, 100)
        tier_choice = ""
        for tier, chance in drops_rates.items():
            if random_number <= chance:
                tier_choice = tier
                break
            random_number -= chance

        # Update local batch counters based on the roll
        if tier_choice == "Blue":
            batch_blues += 1
            blues += 1
        elif tier_choice == "Purple":
            batch_purples += 1
            purples += 1
        elif tier_choice == "Pink":
            batch_pinks += 1
            pinks += 1
        elif tier_choice == "Red":
            batch_reds += 1
            reds += 1
        elif tier_choice == "Gold":
            batch_golds += 1
            golds += 1

        # Gather weapons matching rolled tier
        matching_weapons = []

        for item, collection in cases_list.kilowatt_case.items():
            if collection[0] == tier_choice:
                gun_min_float = collection[2][0] if len(collection[2]) > 1 else 0.0
                gun_max_float = collection[2][1] if len(collection[2]) > 1 else 1.0
                matching_weapons.append((item, collection[1][0], collection[1][1], gun_min_float, gun_max_float))

        gun_choice, min_price, max_price, gun_min_float, gun_max_float = random.choice(matching_weapons)
        wear_float = round(random.uniform(gun_min_float, gun_max_float), 14)

        if wear_float < 0.07: wear_label = "Factory New"
        elif wear_float < 0.15: wear_label = "Minimal Wear"
        elif wear_float < 0.38: wear_label = "Field-Tested"
        elif wear_float < 0.45: wear_label = "Well-Worn"
        else: wear_label = "Battle Scarred"

        skin_price = calculate_skin_price(wear_float, min_price, max_price)
        batch_value += skin_price

        stattrak_roll = random.uniform(0, 100)

        if tier_choice == "Blue":
            total_blues_value += skin_price
            if stattrak_roll < 7.99:
                gun_choice = "StatTrak " + gun_choice

        elif tier_choice == "Purple":
            total_purples_value += skin_price
            if stattrak_roll < 1.60:
                gun_choice = "StatTrak " + gun_choice
        elif tier_choice == "Pink":
            total_pinks_value += skin_price
            if stattrak_roll < 0.32:
                gun_choice = "StatTrak " + gun_choice
        elif tier_choice == "Red":
            total_reds_value += skin_price
            if stattrak_roll < 0.064:
                gun_choice = "StatTrak " + gun_choice
        elif tier_choice == "Gold":
            total_golds_value += skin_price
            if stattrak_roll < 0.026:
                gun_choice = "StatTrak " + gun_choice
            
        
        # formatted_float = f"{wear_float:.14f}"
        # formatted_price = f"${skin_price:.2f}"

        # Store for lists
        drop_data = (gun_choice, tier_choice, wear_label, wear_float, skin_price)
        batch_drops.append(drop_data)
        inventory.append({
            "Item": gun_choice, "Tier": tier_choice, "Wear": wear_label, 
            "Float": float(wear_float), "Price": float(skin_price)
        })

    # 4. Calculate batch totals and update global states
    batch_spent = total_mass_cases * (cases_list.kilowatt_case_base_price + key_price)
    total_spent += batch_spent
    inventory_value += batch_value



    # 6. Update the newly added Mass Open Stat Label
    # mass_open_label.config(
    #     text=f"MASS OPENING:\n\n"
    #          f"Players: {num_players:,}\n"
    #          f"Cases Per Player: {cases_per_player:,}\n"
    #          f"Total Batch Cases: {total_mass_cases:,}\n"
    #          f"Batch Spent: ${batch_spent:,.2f}\n\n"
    #          f"Blues: {batch_blues:,} | Purples: {batch_purples:,}\n"
    #          f"Pinks: {batch_pinks:,} | Reds: {batch_reds:,}\n"
    #          f"Golds: {batch_golds:,}\n"
    # )

    # 7. Refresh your regular single-opening HUD label at the top center
    update_ui_stats()


def calculate_skin_price(float_value, min_price, max_price):
    """
    Calculates item value based on its float.
    Lower float = cleaner wear = higher price.
    """
    price_range = max_price - min_price
    
    # Calculate price inversely proportional to the float
    price = max_price - (float_value * price_range)
    
    # Round to 2 decimal places for currency
    return round(price, 2)


def roll_random_tier():
    """Generates a random roll and returns a tier string based on drop rates."""
    random_number = random.uniform(0, 100)
    for tier, chance in drops_rates.items():
        if random_number <= chance:
            return tier
        random_number -= chance


def open_case(case_type="kilowatt"):
    global animation_running, ticker_items, current_offset, velocity, winning_item_data, average_dry_streak_list, profit, best_drop_text
    global inventory_value, total_spent, cases, blues, purples, pinks, reds, golds
    global total_blues_value, total_purples_value, total_pinks_value, total_reds_value, total_golds_value
    global pink_dry_streak, average_pink_dry_streak_list, red_dry_streak, average_red_dry_streak_list, gold_dry_steak, average_gold_dry_streak_list, average_float_list
    global battle_scarred_count, well_worn_count, field_tested_count, minimal_wear_count, factory_new_count
    global kilowatt_count, horizon_count, revolution_count, spectrum_count, recoil_count
    global blue_st, purple_st, pink_st, red_st, gold_st, battle_scarred_st, well_worn_st, field_tested_st, minimal_wear_st, factory_new_st
    
    if animation_running:
        return

    # 1. Roll the winner tier
    tier_choice = roll_random_tier()

    # 2. Gather weapons matching the winner tier
    matching_weapons = []

    # Select case based on parameter
    if case_type == "horizon":
        case_pool = cases_list.horizon_case
        case_base_price = cases_list.horizon_case_base_price
        horizon_count += 1
    elif case_type == "kilowatt":
        case_pool = cases_list.kilowatt_case
        case_base_price = cases_list.kilowatt_case_base_price
        kilowatt_count += 1
    elif case_type == "revolution":
        case_pool = cases_list.revolution_case
        case_base_price = cases_list.revolution_case_base_price
        revolution_count += 1
    elif case_type == "spectrum":
        case_pool = cases_list.spectrum_case
        case_base_price = cases_list.spectrum_case_base_price
        spectrum_count += 1
    elif case_type == "recoil":
        case_pool = cases_list.recoil_case
        case_base_price = cases_list.recoil_case_base_price
        recoil_count += 1

    # OPEN SELECTED CASE
    for item, collection in case_pool.items():
        if collection[0] == tier_choice:
            # Only add items that have price data
            if len(collection[1]) > 1:
                gun_min_float = collection[2][0] if len(collection[2]) > 1 else 0.0
                gun_max_float = collection[2][1] if len(collection[2]) > 1 else 1.0
                matching_weapons.append((item, collection[1][0], collection[1][1], gun_min_float, gun_max_float))


    # Pick the weapon data
    gun_choice, min_price, max_price, gun_min_float, gun_max_float = random.choice(matching_weapons)
    wear_float = round(random.uniform(gun_min_float, gun_max_float), 14)
    average_float_list.append(wear_float)

    
    if wear_float < 0.07: 
        wear_label = "Factory New"
        factory_new_count += 1
    elif wear_float < 0.15: 
        wear_label = "Minimal Wear"
        minimal_wear_count += 1
    elif wear_float < 0.38: 
        wear_label = "Field-Tested"
        field_tested_count += 1
    elif wear_float < 0.45: 
        wear_label = "Well-Worn"
        well_worn_count += 1
    else: 
        wear_label = "Battle Scarred"
        battle_scarred_count += 1

    if wear_label == "Battle Scarred":
        skin_price = case_pool[gun_choice][1][0]
    elif wear_label == "Well-Worn":
        skin_price = case_pool[gun_choice][1][1]
    elif wear_label == "Field-Tested":
        skin_price = case_pool[gun_choice][1][2]
    elif wear_label == "Minimal Wear":
        skin_price = case_pool[gun_choice][1][3]
    else:
        skin_price = case_pool[gun_choice][1][4]


    
    # STATTRAK ROLL
    stattrak_roll = random.uniform(0, 100)



    # skin_price = calculate_skin_price(wear_float, min_price, max_price)
    
    winning_item_data = {
        "Item": gun_choice, 
        "Tier": tier_choice, 
        "Wear": wear_label,
        "Float": wear_float, 
        "Price": skin_price
    }

    if tier_choice == "Gold":
        average_gold_dry_streak_list.append(gold_dry_steak)
        gold_dry_steak = 0
        pink_dry_streak += 1
        red_dry_streak += 1
    elif tier_choice == "Red":
        average_red_dry_streak_list.append(red_dry_streak)
        red_dry_streak = 0
        pink_dry_streak += 1
        gold_dry_steak += 1
    elif tier_choice == "Pink":
        average_pink_dry_streak_list.append(pink_dry_streak)
        pink_dry_streak = 0
        red_dry_streak += 1
        gold_dry_steak += 1
    else:  # Blue or Purple
        pink_dry_streak += 1
        red_dry_streak += 1
        gold_dry_steak += 1

    # ================= THE SKIP CHECKPOINT =================
    if skip_animation_var.get():
        
        cases += 1
        stattrak_roll = random.uniform(0, 100)

        if tier_choice == "Blue":
            total_blues_value += skin_price
            blues += 1
            if stattrak_roll < 7.99:

                match wear_label:
                    case "Battle Scarred":
                        battle_scarred_st += 1
                    case "Well-Worn":
                        well_worn_st += 1
                    case "Field-Tested":
                        field_tested_st += 1
                    case "Minimal Wear":
                        minimal_wear_st += 1
                    case "Factory New":
                        factory_new_st += 1

                gun_choice = "StatTrak " + gun_choice
                blue_st += 1
        elif tier_choice == "Purple":
            total_purples_value += skin_price
            purples += 1
            if stattrak_roll < 1.60:

                match wear_label:
                    case "Battle Scarred":
                        battle_scarred_st += 1
                    case "Well-Worn":
                        well_worn_st += 1
                    case "Field-Tested":
                        field_tested_st += 1
                    case "Minimal Wear":
                        minimal_wear_st += 1
                    case "Factory New":
                        factory_new_st += 1

                gun_choice = "StatTrak " + gun_choice
                purple_st += 1
        elif tier_choice == "Pink":
            pinks += 1
            total_pinks_value += skin_price
            if stattrak_roll < 0.32:

                match wear_label:
                    case "Battle Scarred":
                        battle_scarred_st += 1
                    case "Well-Worn":
                        well_worn_st += 1
                    case "Field-Tested":
                        field_tested_st += 1
                    case "Minimal Wear":
                        minimal_wear_st += 1
                    case "Factory New":
                        factory_new_st += 1

                gun_choice = "StatTrak " + gun_choice
                pink_st += 1
        elif tier_choice == "Red":
            reds += 1
            first_red.append(cases)
            total_reds_value += skin_price
            if stattrak_roll < 0.064:

                match wear_label:
                    case "Battle Scarred":
                        battle_scarred_st += 1
                    case "Well-Worn":
                        well_worn_st += 1
                    case "Field-Tested":
                        field_tested_st += 1
                    case "Minimal Wear":
                        minimal_wear_st += 1
                    case "Factory New":
                        factory_new_st += 1

                gun_choice = "StatTrak " + gun_choice
                red_st += 1
        elif tier_choice == "Gold":
            golds += 1
            first_gold.append(cases)
            total_golds_value += skin_price
            if stattrak_roll < 0.026:

                match wear_label:
                    case "Battle Scarred":
                        battle_scarred_st += 1
                    case "Well-Worn":
                        well_worn_st += 1
                    case "Field-Tested":
                        field_tested_st += 1
                    case "Minimal Wear":
                        minimal_wear_st += 1
                    case "Factory New":
                        factory_new_st += 1

                gun_choice = "StatTrak " + gun_choice
                gold_st += 1

        inventory_value += skin_price
        total_spent += case_base_price + key_price
        formatted_price = f"${skin_price:.2f}"
        
        inventory.append(winning_item_data)
        
        inventory_list.insert(
            "", 0, 
            values=(gun_choice, tier_choice, wear_label, f"{wear_float:.14f}", formatted_price, "$" + str(round(total_spent, 2))),
            tags=(tier_choice,)
        )
        
        update_lowest_float_markers(gun_choice)
        update_ui_stats()
        return
    # =======================================================

    
    ticker_items = []
    for i in range(45):  
        if i == 35:
            ticker_items.append((gun_choice, tier_choice))
        else:
            
            filler_tier = roll_random_tier()
            
            filler_pool = []
            for item, collection in case_pool.items():
                if collection[0] == filler_tier:
                    filler_pool.append((item, filler_tier))
            
            rand_filler_item = random.choice(filler_pool)
            ticker_items.append(rand_filler_item)

    # Mathematical Physics Targeting
    card_width = 130
    card_gap = 10
    total_card_step = card_width + card_gap  
    
    random_nudge = random.uniform(-45, 45)
    target_destination = (35 * total_card_step) + (card_width / 2) + random_nudge
    
    current_offset = 0
    velocity = target_destination * (1 - 0.965)

    profit = inventory_value - total_spent
    print(profit)
    
    animation_running = True
    animate_ticker()


def lowest_float():
    if not inventory:
        return None
    
    lowest = min(inventory, key=lambda x: float(x["Float"]))
    return lowest

def highest_price():
    if not inventory:
        return None

    highest = max(inventory, key=lambda x: float(x["Price"]))
    return highest


def update_lowest_float_markers(gun_choice):
    """
    Updates treelist display for all items matching gun_choice.
    Adds "✧ Lowest Float ✧" marker to the item with lowest float for this weapon.
    Removes marker from any previously marked items of the same weapon.
    """
    # Find lowest float for this weapon in inventory
    matching = [item for item in inventory if item["Item"] == gun_choice]
    if not matching:
        return
    
    lowest_float_val = min(matching, key=lambda x: float(x["Float"]))["Float"]
    lowest_numeric = float(lowest_float_val)
    
    # Update all treelist entries for this weapon
    for item_id in inventory_list.get_children():
        item_values = list(inventory_list.item(item_id, 'values'))
        if item_values[0] == gun_choice:  # Same weapon name
            float_col = item_values[3]
            # Remove any existing marker
            float_clean = float_col.replace(" ✧ Lowest Float ✧", "")
            float_numeric = float(float_clean)
            
            # Add marker only if this is the lowest
            if float_numeric == lowest_numeric:
                item_values[3] = f"{float_clean} ✧ Lowest Float ✧"
            else:
                item_values[3] = float_clean
            
            inventory_list.item(item_id, values=tuple(item_values))

def expected_item_value(min_price, max_price, fmin, fmax):
    avg_float = (fmin + fmax) / 2
    return max_price - (max_price - min_price) * avg_float


def expected_tier_value(case, tier):
    items = [v for v in case.values() if v[0] == tier]

    total = 0
    for item in items:
        min_price = item[1][0]
        max_price = item[1][-1]
        fmin, fmax = item[2]

        total += expected_item_value(min_price, max_price, fmin, fmax)

    return total / len(items)


def expected_case_value(case):
    return (
        0.032 * expected_tier_value(case, "Pink") +
        0.0064 * expected_tier_value(case, "Red") +
        0.0026 * expected_tier_value(case, "Gold")
    )

def reset():
    global cases, total_spent, inventory, inventory_value, profit, roi, lowest_float_value
    global blues, purples, pinks, pink_dry_streak, average_pink_dry_streak_list, reds, first_red, red_dry_streak, average_red_dry_streak_list, golds, first_gold, gold_dry_steak, average_gold_dry_streak_list
    global average_float_list, average_float, total_blues_value, total_purples_value, total_pinks_value, total_reds_value, total_golds_value
    global battle_scarred_count, well_worn_count, field_tested_count, minimal_wear_count, factory_new_count, inventory_list


    cases = 0
    total_spent = 0
    inventory = []
    inventory_value = 0
    profit = 0
    roi = 0
    lowest_float_value = 0.0
    blues = 0
    purples = 0
    pinks = 0
    pink_dry_streak = 0
    average_pink_dry_streak_list = []
    reds = 0
    first_red = []
    red_dry_streak = 0
    average_red_dry_streak_list = []
    golds = 0
    first_gold = []
    gold_dry_steak = 0
    average_gold_dry_streak_list = []

    average_float_list = []
    average_float = 0.0

    total_blues_value = 0
    total_purples_value = 0
    total_pinks_value = 0
    total_reds_value = 0
    total_golds_value = 0

    

    battle_scarred_count = 0
    well_worn_count = 0
    field_tested_count = 0
    minimal_wear_count = 0
    factory_new_count = 0



    inventory_list.delete(*inventory_list.get_children())
    update_ui_stats()

    


def animate_ticker():
    global current_offset, velocity, animation_running, inventory_value, total_spent, cases, blues, purples, pinks, reds, golds, first_red, first_gold
    global total_blues_value, total_purples_value, total_pinks_value, total_reds_value, total_golds_value
    global pink_dry_streak, red_dry_streak, gold_dry_steak, average_pink_dry_streak_list, average_red_dry_streak_list, average_gold_dry_streak_list, average_float_list
    global battle_scarred_count, well_worn_count, field_tested_count, minimal_wear_count, factory_new_count
    
    # roll_canvas.delete("skin_card")
    
    current_offset += velocity
    velocity *= 0.965  # Constant friction decay rate

    card_width = 130
    card_gap = 10
    total_card_step = card_width + card_gap

    # Rendering Loop
    for idx, (name, tier) in enumerate(ticker_items):
        # Position card relative to the center screen viewport needle (at X = 350)
        x_pos = (idx * total_card_step) - current_offset + 350
        
        if -150 < x_pos < 850:
            card_color = TIER_COLORS.get(tier, "#222222")
            
            # Draw weapon card frame
            # roll_canvas.create_rectangle(x_pos, 10, x_pos + card_width, 90, fill="#2b2b2b", outline=card_color, width=2, tags="skin_card")
            
            # Draw labels inside the frame safely
            if "|" in name:
                weapon_type = name.split("|")[0].strip()
                short_name = name.split("|")[1].strip()
            else:
                weapon_type = "Special Item"
                short_name = name
                
    #         roll_canvas.create_text(x_pos + 65, 35, text=weapon_type, fill="#888888", font=("Arial", 8, "bold"), tags="skin_card")
    #         roll_canvas.create_text(x_pos + 65, 55, text=short_name, fill="white", font=("Arial", 9, "bold"), tags="skin_card", width=110, justify="center")

    # roll_canvas.tag_raise("needle")

    # Stop the ticker thread loop once velocity drops down
    if velocity > 0.05:
        root.after(15, animate_ticker)
    else:
        # Finalize and award tracking counters once the item stops moving
        animation_running = False
        
        # Determine which case was opened by checking winning item
        if winning_item_data["Item"] in cases_list.kilowatt_case:
            case_base_price = cases_list.kilowatt_case_base_price
        else:
            case_base_price = cases_list.horizon_case_base_price
        
        cases += 1
        tier_choice = winning_item_data["Tier"]
        
        if tier_choice == "Blue": blues += 1
        elif tier_choice == "Purple": purples += 1
        elif tier_choice == "Pink": pinks += 1
        elif tier_choice == "Red":
            reds += 1
            first_red.append(cases)
        elif tier_choice == "Gold":
            golds += 1
            first_gold.append(cases)

        inventory_value += winning_item_data["Price"]
        total_spent += case_base_price + key_price
        formatted_price = f"${winning_item_data['Price']:.2f}"
        
        inventory.append(winning_item_data)
        
        inventory_list.insert(
            "", 0, 
            values=(winning_item_data["Item"], tier_choice, winning_item_data["Wear"], f"{winning_item_data['Float']}", formatted_price, "$" + str(round(total_spent, 2))),
            tags=(tier_choice,)
        )
        
        update_lowest_float_markers(winning_item_data["Item"])
        update_ui_stats()

cases_buttons_frame = tk.Frame(top_frame, background="blue")
cases_buttons_frame.grid(row=0, column=4, sticky='nesw')


# Action Button
open_kilowatt_case_button = tk.Button(
    cases_buttons_frame, 
    text=f"OPEN KILOWATT CASE (${round(cases_list.kilowatt_case_base_price + key_price, 2)})", 
    command=lambda: open_case("kilowatt"),
    font=("Arial", 12, "bold"),
    bg="#2ecc71",
    fg="white",
    activebackground="#27ae60",
    activeforeground="white",
    bd=0,
    pady=10
)
open_horizon_case_button = tk.Button(
    cases_buttons_frame, 
    text=f"OPEN HORIZON CASE (${round(cases_list.horizon_case_base_price + key_price, 2)})", 
    command=lambda: open_case("horizon"),
    font=("Arial", 12, "bold"),
    bg="#2ecc71",
    fg="white",
    activebackground="#27ae60",
    activeforeground="white",
    bd=0,
    pady=10
)
open_revolution_case_button = tk.Button(
    cases_buttons_frame, 
    text=f"OPEN REVOLUTION CASE (${round(cases_list.revolution_case_base_price + key_price, 2)})", 
    command=lambda: open_case("revolution"),
    font=("Arial", 12, "bold"),
    bg="#2ecc71",
    fg="white",
    activebackground="#27ae60",
    activeforeground="white",
    bd=0,
    pady=10
)
open_spectrum_case_button = tk.Button(
    cases_buttons_frame, 
    text=f"OPEN SPECTRUM CASE (${round(cases_list.spectrum_case_base_price + key_price, 2)})", 
    command=lambda: open_case("spectrum"),
    font=("Arial", 12, "bold"),
    bg="#2ecc71",
    fg="white",
    activebackground="#27ae60",
    activeforeground="white",
    bd=0,
    pady=10
)
open_recoil_case_button = tk.Button(
    cases_buttons_frame, 
    text=f"OPEN RECOIL CASE (${round(cases_list.recoil_case_base_price + key_price, 2)})", 
    command=lambda: open_case("recoil"),
    font=("Arial", 12, "bold"),
    bg="#2ecc71",
    fg="white",
    activebackground="#27ae60",
    activeforeground="white",
    bd=0,
    pady=10
)
open_kilowatt_case_button.pack(pady=15, fill="x", padx=20)
open_horizon_case_button.pack(pady=15, fill="x", padx=20)
open_revolution_case_button.pack(pady=15, fill="x", padx=20)
open_spectrum_case_button.pack(pady=15, fill='x', padx=20)
open_recoil_case_button.pack(pady=15, fill='x', padx=20)

# mass_frame = tk.Frame(top_frame, background="red")
# mass_frame.pack()
mass_open_button = tk.Button(player_entry_frame, text="Mass Open", command=mass_open)
mass_open_button.grid(row=5, column=0, sticky='nsew', padx=5, pady=5)
reset_button = tk.Button(player_entry_frame, text="Reset", command=reset)
reset_button.grid(row=6, column=0, sticky='nsew', padx=5, pady=5)


update_ui_stats()
root.mainloop()
