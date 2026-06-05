import random
import tkinter as tk
from tkinter import font
from tkinter import ttk




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
root.geometry("1920x1080")  
root.configure(bg="#1e1e1e") 


style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", background="#2b2b2b", foreground="white", fieldbackground="#2b2b2b", rowheight=25)
style.map("Treeview", background=[("selected", "#4a4a4a")])


# Top Frame for Stats & Button
top_frame = tk.Frame(root, bg="#1e1e1e")
top_frame.pack(pady=15, fill="x", padx=20, anchor="center")


# Stats Labels
stat_font = font.Font(family="Weghorst-Italic", size=14)
stats_label = tk.Label(
    top_frame, 
    text="Total Spent: $0.00 \n Inventory Value: $0.00 \n ROI: 0% \n Cases: 0 \n\n Lowest Float: N/A \n\n Blues: 0 | $0 \n\n Purples: 0 | $0 \n\n Pinks: 0 | $0 \n\n Reds: 0 | $0 \n First Red: 0 \n Total Spent for First Red: $0 \n\n Golds: 0 | $0 \n First Gold: 0 \n Total Spent for First Gold: $0", 
    font=(stat_font), 
    fg="#ecf0f1", 
    bg="#1e1e1e",
    justify="center"
)
stats_label.pack(side="left", anchor="center", expand=True, fill="both")

mass_open_label = tk.Label(
    top_frame,
    text="MASS OPENING: \n\n Players: 0 \n Cases: 0 \n Total Cases Opened: 0 \n Total Spent: $0 \n Total Blues: 0 \n Total Purples: 0 \n Total Pinks: 0 \n Total Reds: 0 \n Total Golds: 0",
    font=(stat_font), 
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

skip_animation_var = tk.BooleanVar(value=False)

skip_checkbox = tk.Checkbutton(
    top_frame,
    text="Skip Animation",
    variable=skip_animation_var,
    font=("Arial", 10, "bold"),
    fg="#ecf0f1",
    bg="#1e1e1e",
    activebackground="#1e1e1e",
    activeforeground="#ecf0f1",
    selectcolor="#2b2b2b" # Changes the check box square background color
)
skip_checkbox.pack(pady=5)



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

anim_frame = tk.Frame(root, bg="#1a1a1a", height=120)
anim_frame.pack(fill="x", padx=20, pady=10)


roll_canvas = tk.Canvas(anim_frame, width=700, height=100, bg="#222222", highlightthickness=2, highlightbackground="#3a3a3a")
roll_canvas.pack(anchor="center")


roll_canvas.create_line(350, 0, 350, 100, fill="#eb3434", width=3, tags="needle")






# Inventory Display Setup (The List View)
tree_frame = tk.Frame(root)
tree_frame.pack(pady=10, fill="both", expand=True, padx=20)

# Scrollbar for list view
tree_scroll = ttk.Scrollbar(tree_frame)
tree_scroll.pack(side="right", fill="y")

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

    stats_label.config(text=f"Total Spent: ${total_spent:,.2f} \n Inventory Value: ${inventory_value:,.2f} \n Return: {roi:,.1f}% \n Cases: {cases:,} \n\n Lowest Float: {best_drop_text} \n\n Blues: {blues:,} | ${total_blues_value:,.2f} \n\n Purples: {purples:,} | ${total_purples_value:,.2f} \n\n Pinks: {pinks:,} | ${total_pinks_value:,.2f} \n\n Reds: {reds:,} | ${total_reds_value:,.2f} \n First Red: {first_red[0] if reds > 0 else 0} \n Total Spent for First Red: ${(first_red[0] * (kilowatt_case_base_price + key_price)) if reds > 0 else 0:,.2f} \n\n Golds: {golds:,} | ${total_golds_value:,.2f} \n First Gold: {first_gold[0] if golds > 0 else 0} \n Total Spent for First Gold: ${(first_gold[0] * (kilowatt_case_base_price + key_price)) if golds > 0 else 0:,.2f}", justify="center")


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
             f"Blues: {batch_blues:,} | Purples: {batch_purples:,}\n"
             f"Pinks: {batch_pinks:,} | Reds: {batch_reds:,}\n"
             f"Golds: {batch_golds:,}\n"
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


def roll_random_tier():
    """Generates a random roll and returns a tier string based on drop rates."""
    random_number = random.uniform(0, 100)
    for tier, chance in drops_rates.items():
        if random_number <= chance:
            return tier
        random_number -= chance


def open_case():
    global animation_running, ticker_items, current_offset, velocity, winning_item_data
    global inventory_value, total_spent, cases, blues, purples, pinks, reds, golds
    global total_blues_value, total_purples_value, total_pinks_value, total_reds_value, total_golds_value
    
    if animation_running:
        return

    # 1. Roll the winner tier
    tier_choice = roll_random_tier()

    # 2. Gather weapons matching the winner tier
    matching_weapons = []
    for item, collection in kilowatt_case.items():
        if collection[0] == tier_choice:
            matching_weapons.append((item, collection[1][0], collection[1][1]))

    # Pick the weapon data
    gun_choice, min_price, max_price = random.choice(matching_weapons)
    wear_float = round(random.uniform(0, 1), 14)
    
    if wear_float < 0.07: wear_label = "Factory New"
    elif wear_float < 0.15: wear_label = "Minimal Wear"
    elif wear_float < 0.38: wear_label = "Field-Tested"
    elif wear_float < 0.45: wear_label = "Well-Worn"
    else: wear_label = "Battle Scarred"

    skin_price = calculate_skin_price(wear_float, min_price, max_price)
    
    winning_item_data = {
        "Item": gun_choice, 
        "Tier": tier_choice, 
        "Wear": wear_label,
        "Float": f"{wear_float:.14f}", 
        "Price": skin_price
    }

    # ================= THE SKIP CHECKPOINT =================
    if skip_animation_var.get():
        
        cases += 1
        if tier_choice == "Blue": 
            blues += 1
            total_blues_value += skin_price
        elif tier_choice == "Purple": 
            total_purples_value += skin_price
            purples += 1
        elif tier_choice == "Pink": 
            total_pinks_value += skin_price
            pinks += 1
        elif tier_choice == "Red":
            total_reds_value += skin_price
            reds += 1
            first_red.append(cases)
        elif tier_choice == "Gold":
            total_golds_value += skin_price
            golds += 1
            first_gold.append(cases)

        inventory_value += skin_price
        total_spent += kilowatt_case_base_price + key_price
        formatted_price = f"${skin_price:.2f}"
        
        inventory_list.insert(
            "", 0, 
            values=(gun_choice, tier_choice, wear_label, f"{wear_float:.14f}", formatted_price, "$" + str(round(total_spent, 2))),
            tags=(tier_choice,)
        )
        inventory.append(winning_item_data)
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
            for item, collection in kilowatt_case.items():
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
    
    animation_running = True
    animate_ticker()


def lowest_float():
    if not inventory:
        return None
    
    lowest = min(inventory, key=lambda x: float(x["Float"]))
    return lowest


def animate_ticker():
    global current_offset, velocity, animation_running, inventory_value, total_spent, cases, blues, purples, pinks, reds, golds
    
    roll_canvas.delete("skin_card")
    
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
            roll_canvas.create_rectangle(x_pos, 10, x_pos + card_width, 90, fill="#2b2b2b", outline=card_color, width=2, tags="skin_card")
            
            # Draw labels inside the frame safely
            if "|" in name:
                weapon_type = name.split("|")[0].strip()
                short_name = name.split("|")[1].strip()
            else:
                weapon_type = "Special Item"
                short_name = name
                
            roll_canvas.create_text(x_pos + 65, 35, text=weapon_type, fill="#888888", font=("Arial", 8, "bold"), tags="skin_card")
            roll_canvas.create_text(x_pos + 65, 55, text=short_name, fill="white", font=("Arial", 9, "bold"), tags="skin_card", width=110, justify="center")

    roll_canvas.tag_raise("needle")

    # Stop the ticker thread loop once velocity drops down
    if velocity > 0.05:
        root.after(15, animate_ticker)
    else:
        # Finalize and award tracking counters once the item stops moving
        animation_running = False
        
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
        total_spent += kilowatt_case_base_price + key_price
        formatted_price = f"${winning_item_data['Price']:.2f}"
        
        inventory_list.insert(
            "", 0, 
            values=(winning_item_data["Item"], tier_choice, winning_item_data["Wear"], winning_item_data["Float"], formatted_price, "$" + str(total_spent)),
            tags=(tier_choice,)
        )
        
        inventory.append(winning_item_data)
        update_ui_stats()


# Action Button
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
