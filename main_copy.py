import random
import tkinter as tk
from tkinter import ttk  # Import ttk for modern widgets like Treeview

# ... (Keep all your dictionary definitions and calculate_skin_price function exactly the same)
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

# ITEM, RATE, PRICE
kilowatt_case_base_price = 0.30
kilowatt_case = {
    "Nova | Dark Sigil": ["Blue", [0.12, 0.63]],
    "Dual Berettas | Hideout": ["Blue", [0.12, 0.66]],
    "UMP-45 | Motorized": ["Blue", [0.09, 0.70]],
    "XM1014 | Irezumi": ["Blue", [0.09, 0.73]],
    "Tec-9 | Slag": ["Blue", [0.12, 1.32]],
    "SSG 08 | Dezastre": ["Blue", [0.10, 1.33]],
    "MAC-10 | Light Box": ["Blue", [0.12, 1.44]],
    "Sawed-Off | Analog Input": ["Purple", [0.59, 2.04]],
    "MP7 | Just Smile": ["Purple", [0.55, 5.67]],
    "Five-SeveN | Hybrid": ["Purple", [0.55, 6.29]],
    "Glock-18 | Block-18": ["Purple", [0.65, 3.26]],
    "M4A4 | Etch Lord": ["Purple", [0.57, 11.06]],
    "Zeus x27 | Olympus": ["Pink", [4.40, 13.00]],
    "USP-S | Jawbreaker": ["Pink", [4.50, 36.07]],
    "M4A1-S | Black Lotus": ["Pink", [6.80, 23.74]],
    "AWP | Chrome Cannon": ["Red", [37.00, 126.22]],
    "AK-47 | Inheritance": ["Red", [50.30, 194.08]],
    "Kukri Knife | Forest DDPAT": ["Gold", [64.65, 192.81]],
    "Kukri Knife | Boreal Forest": ["Gold", [63.76, 140.00]],
    "Kukri Knife | Safari Mesh": ["Gold", [62.81, 184.53]],
    "Kukri Knife | Stained": ["Gold", [94.22, 143.76]],
    "Kukri Knife | Scorched": ["Gold", [66.86, 179.07]],
    "Kukri Knife | Urban Masked": ["Gold", [67.68, 273.31]],
    "Kukri Knife | Night Stripe": ["Gold", [72.81, 197.00]],
    "Kukri Knife | Vanilla": ["Gold", [146.24, 146.24]],
    "Kukri Knife | Blue Steel": ["Gold", [111.94, 199.56]],
    "Kukri Knife | Slaughter": ["Gold", [184.00, 206.70]],
    "Kukri Knife | Case Hardened": ["Gold", [138.07, 280.00]],
    "Kukri Knife | Fade": ["Gold", [265.00, 307.78]],
    "Kukri Knife | Crimson Web": ["Gold", [108.99, 969.69]],
}

cases = 0
total_spent = 0
key_price = 2.49
inventory = []
inventory_value = 0
blues = 0
purples = 0
pinks = 0
reds = 0
first_red = []
golds = 0
first_gold = []

total_blues_value = 0
total_purples_value = 0
total_pinks_value = 0
total_reds_value = 0
total_golds_value = 0


root = tk.Tk()
root.title("CS2 CASE SIM")
root.geometry("1920x1080")  # Made slightly wider to comfortably fit the 14-digit floats
root.configure(bg="#1e1e1e")  # Dark theme background

# Apply a clean, modern style layout
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", background="#2b2b2b", foreground="white", fieldbackground="#2b2b2b", rowheight=25)
style.map("Treeview", background=[("selected", "#4a4a4a")])

# Top Frame for Stats & Button
top_frame = tk.Frame(root, bg="#1e1e1e")
top_frame.pack(pady=15, fill="x", padx=20, anchor="center")

# Real-time Stats Labels
stats_label = tk.Label(
    top_frame, 
    text="Total Spent: $0.00 \n Inventory Value: $0.00 \n ROI: 0% \n Cases: 0 \n\n Lowest Float: N/A \n\n Blues: 0 \n Blues Value: $0 \n\n Purples: 0 \n Purples Value: $0 \n\n Pinks: 0 \n Pinks Value: $0 \n\n Reds: 0 \n Reds Value: $0 \n First Red: 0 \n Total Spent for First Red: $0 \n\n Golds: 0 \n Golds Value: $0 \n First Gold: 0 \n Total Spent for First Gold: $0", 
    font=("Arial", 11, "bold"), 
    fg="#ecf0f1", 
    bg="#1e1e1e",
    justify="center"
)
stats_label.pack(side="left", anchor="center", expand=True, fill="both")

mass_open_label = tk.Label(
    top_frame,
    text="MASS OPENING: \n\n Players: 0 \n Cases: 0 \n Total Cases Opened: 0 \n Total Spent: $0 \n Total Blues: 0 \n Total Purples: 0 \n Total Pinks: 0 \n Total Reds: 0 \n Total Golds: \n",
    font=("Arial", 11, "bold"), 
    fg="#ecf0f1", 
    bg="#1e1e1e",
    justify="center"
)
mass_open_label.pack(side="right", anchor="center", expand=True, fill="both")

players_entry_label = tk.Label(top_frame, text="Players", fg="#ecf0f1", 
    bg="#1e1e1e",)
players_entry_label.pack()
players_entry_input = tk.IntVar(top_frame)
players_entry = tk.Entry(top_frame, textvariable=players_entry_input)
players_entry.pack()

cases_entry_label = tk.Label(top_frame, text="Cases", fg="#ecf0f1", 
    bg="#1e1e1e",)
cases_entry_label.pack()
cases_entry_input = tk.IntVar(top_frame)
cases_entry = tk.Entry(top_frame, textvariable=cases_entry_input)
cases_entry.pack()

# Inventory Display Setup (The List View)
tree_frame = tk.Frame(root)
tree_frame.pack(pady=10, fill="both", expand=True, padx=20)

# Create Scrollbar for the list view
tree_scroll = ttk.Scrollbar(tree_frame)
tree_scroll.pack(side="right", fill="y")

# Define Columns
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

inventory_list.pack(fill="both", expand=True)

# Color tags for rarity highlighting
inventory_list.tag_configure("Blue", foreground="#5c75cd")
inventory_list.tag_configure("Purple", foreground="#9d0aff")
inventory_list.tag_configure("Pink", foreground="#e17cf8")
inventory_list.tag_configure("Red", foreground="#eb3434")
inventory_list.tag_configure("Gold", foreground="#e0a91b")

def update_ui_stats():
    """Updates the statistics label text at the top."""
    roi = 0
    if total_spent > 0:
        roi = (inventory_value / total_spent) * 100

    best_drop = lowest_float()
    if best_drop:
        best_drop_text = f"{best_drop["Item"]}: {best_drop["Float"]}"
    else:
        best_drop_text = "N/A"

    stats_label.config(text=f"Total Spent: ${total_spent:,.2f} \n Inventory Value: ${inventory_value:,.2f} \n Return: {roi:,.1f}% \n Cases: {cases} \n\n Lowest Float: {best_drop_text} \n\n Blues: {blues} \n Blues Value: ${total_blues_value:,.2f} \n\n Purples: {purples} \n Purples Value: ${total_purples_value:,.2f} \n\n Pinks: {pinks} \n Pinks Value: ${total_pinks_value:,.2f} \n\n Reds: {reds} \n Reds Value: ${total_reds_value:,.2f} \n First Red: {first_red[0] if reds > 0 else 0} \n Total Spent for First Red: ${(first_red[0] * (kilowatt_case_base_price + key_price)) if reds > 0 else 0:,.2f} \n\n Golds: {golds} \n Golds Value: ${total_golds_value:,.2f} \n First Gold: {first_gold[0] if golds > 0 else 0} \n Total Spent for First Gold: ${(first_gold[0] * (kilowatt_case_base_price + key_price)) if golds > 0 else 0:,.2f}", justify="center")

def mass_open():
    # Bring in all the global tracking counters
    global inventory_value, total_spent, cases, blues, purples, pinks, reds, golds, total_blues_value, total_purples_value, total_pinks_value, total_reds_value, total_golds_value
    
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
            first_red.append(cases)
        elif tier_choice == "Gold":
            batch_golds += 1
            golds += 1
            first_gold.append(cases)

        # Gather weapons matching rolled tier
        matching_weapons = []
        for item, collection in kilowatt_case.items():
            if collection[0] == tier_choice:
                matching_weapons.append((item, collection[1][0], collection[1][1]))

        gun_choice, min_price, max_price = random.choice(matching_weapons)
        wear_float = round(random.uniform(0, 1), 14)

        if wear_float < 0.07: wear_label = "Factory New"
        elif wear_float < 0.15: wear_label = "Minimal Wear"
        elif wear_float < 0.38: wear_label = "Field-Tested"
        elif wear_float < 0.45: wear_label = "Well-Worn"
        else: wear_label = "Battle Scarred"

        skin_price = calculate_skin_price(wear_float, min_price, max_price)
        batch_value += skin_price

        if tier_choice == "Blue":
            total_blues_value += skin_price
        elif tier_choice == "Purple":
            total_purples_value += skin_price
        elif tier_choice == "Pink":
            total_pinks_value += skin_price
        elif tier_choice == "Red":
            total_reds_value += skin_price
        elif tier_choice == "Gold":
            total_golds_value += skin_price
            
        
        formatted_float = f"{wear_float:.14f}"
        formatted_price = f"${skin_price:.2f}"

        # Store for lists
        drop_data = (gun_choice, tier_choice, wear_label, formatted_float, formatted_price)
        batch_drops.append(drop_data)
        inventory.append({
            "Item": gun_choice, "Tier": tier_choice, "Wear": wear_label, 
            "Float": formatted_float, "Price": formatted_price
        })

    # 4. Calculate batch totals and update global states
    batch_spent = total_mass_cases * (kilowatt_case_base_price + key_price)
    total_spent += batch_spent
    inventory_value += batch_value



    # 6. Update the newly added Mass Open Stat Label
    mass_open_label.config(
        text=f"MASS OPENING:\n\n"
             f"Players: {num_players:,}\n"
             f"Cases Per Player: {cases_per_player:,}\n"
             f"Total Batch Cases: {total_mass_cases:,}\n"
             f"Batch Spent: ${batch_spent:,.2f}\n\n"
             f"Blues: {batch_blues} | Purples: {batch_purples}\n"
             f"Pinks: {batch_pinks} | Reds: {batch_reds}\n"
             f"Golds: {batch_golds}\n"
    )

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



def open_case():
    global inventory_value, total_spent, cases, blues, purples, pinks, reds, golds, total_blues_value, total_purples_value, total_pinks_value, total_reds_value, total_golds_value
    cases += 1
    
    random_number = random.uniform(0, 100)
    tier_choice = ""

    for tier, chance in drops_rates.items():
        if random_number <= chance:
            tier_choice = tier
            break
        random_number -= chance

    if tier == "Blue":
        blues += 1
    elif tier == "Purple":
        purples += 1
    elif tier == "Pink":
        pinks += 1
    elif tier == "Red":
        reds += 1
        first_red.append(cases)
    else:
        golds += 1
        first_gold.append(cases)


    matching_weapons = []
    for item, collection in kilowatt_case.items():
        if collection[0] == tier_choice:
            matching_weapons.append((item, collection[1][0], collection[1][1]))

    gun_choice, min_price, max_price = random.choice(matching_weapons)
    wear_float = round(random.uniform(0, 1), 14)

    if wear_float < 0.07: wear_label = "Factory New"
    elif wear_float < 0.15: wear_label = "Minimal Wear"
    elif wear_float < 0.38: wear_label = "Field-Tested"
    elif wear_float < 0.45: wear_label = "Well-Worn"
    else: wear_label = "Battle Scarred"

    skin_price = calculate_skin_price(wear_float, min_price, max_price)
    inventory_value += skin_price
    total_spent += kilowatt_case_base_price + key_price

    if tier == "Blue":
        total_blues_value += skin_price
    elif tier == "Purple":
        total_purples_value += skin_price
    elif tier == "Pink":
        total_pinks_value += skin_price
    elif tier == "Red":
        total_reds_value += skin_price
    else:
        total_golds_value += skin_price


    # Formatted variants for clean text display
    formatted_float = f"{wear_float:.14f}"
    formatted_price = f"${skin_price:.2f}"
    case_return = (skin_price - (kilowatt_case_base_price + key_price)) / (kilowatt_case_base_price + key_price) * 100
    formatted_return = f"{case_return:.2f}%"

    drop = {
        "Item": gun_choice,
        "Tier": tier_choice,
        "Wear": wear_label,
        "Float": formatted_float,
        "Price": formatted_price + "(" + formatted_return + ")",
        "Total Spent": total_spent
    }
    inventory.append(drop)


    # INSERT INTO THE LIST VIEW (Inserts at the very top index 0 so newest drops appear first)
    inventory_list.insert(
        "", 
        0, 
        values=(gun_choice, tier_choice, wear_label, formatted_float, formatted_price + " (" + formatted_return + ")", "$" + str(round(total_spent, 2))),
        tags=(tier_choice,)  # Applies the color rarity tag matching the skin tier
    )

    # Refresh the top HUD stats
    update_ui_stats()


def lowest_float():
    if not inventory:
        return None
    
    lowest = min(inventory, key=lambda x: float(x["Float"]))
    return lowest


# Action Button at the bottom
open_case_button = tk.Button(
    root, 
    text="OPEN KILOWATT CASE ($2.79)", 
    command=open_case,
    font=("Arial", 12, "bold"),
    bg="#2ecc71",
    fg="white",
    activebackground="#27ae60",
    activeforeground="white",
    bd=0,
    pady=10
)
open_case_button.pack(pady=15, fill="x", padx=20)
mass_open_button = tk.Button(top_frame, text="Mass Open", command=mass_open)
mass_open_button.pack(pady=10)

root.mainloop()
