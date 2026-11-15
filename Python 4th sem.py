from datetime import datetime

# List: Acts as our main database to hold multiple items (movies)
movie_inventory = []

# SET CONCEPT: A global set to store movie titles in lowercase. 
movie_names_set = set()

def shared_get_valid_input(prompt):
    """Utility to ensure the user does not enter blank inputs."""
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("  🌸 Input cannot be blank. Let's try that again!")

def setup_load_initial_movies():
    """Pre-loads data before user makes a choice."""
    
    admin_1c_add_movie("Dhurandhar", "Aditya Dhar", 2025, "Hindi", "10:00 AM, 02:30 PM", 50, 200, 350)
    admin_1c_add_movie("Game Changer", "Shankar", 2025, "Telugu", "11:15 AM, 04:00 PM", 40, 150, 300)
    admin_1c_add_movie("Jana Nayagan", "H. Vinoth", 2026, "Tamil", "09:00 AM, 01:00 PM", 30, 180, 320)

# =================================================================================
# [1] ADMIN FLOW FUNCTIONS
# =================================================================================

# [1A] Admin Dashboard (Entry Point for Admin)
def admin_1a_dashboard():
    print("\n  ✅ Welcome back, Mr. Owner.")
    while True:
        print("""
  =============================================
  🔐   OWNER DASHBOARD
  =============================================
  1. View Movies    3. Delete Movie
  2. Add Movie      4. Log Out""")
        match input("  Select (1-4): ").strip():
            case "1": 
                admin_1b_display_movies()
            case "2":
                t = shared_get_valid_input(" Title: ")
                d = shared_get_valid_input(" Director: ")
                y = shared_get_valid_input(" Year: ")
                l = shared_get_valid_input(" Language: ")
                tm = shared_get_valid_input(" Timings: ")
                qty = shared_get_valid_input(" Capacity: ")
                p2 = shared_get_valid_input(" 2D Price: ")
                pp = shared_get_valid_input(" Premier Price: ")
                
                if y.isdigit() and qty.isdigit() and p2.isdigit() and pp.isdigit():
                    
                    admin_1c_add_movie(t, d, int(y), l, tm, int(qty), int(p2), int(pp))
                    print("  ✅ Added successfully (if not duplicate).")
                
                else: 
                    print("  ⚠️ Year, Capacity, and Prices must be numbers.")
            case "3": 
                admin_1d_delete_movie()
            case "4": 
                break
            case _: 
                print("  ⚠️ Invalid choice.")

# [1B] Admin View Movies
def admin_1b_display_movies():
    if not movie_inventory:
        print("\n  🌸 We currently have no movies showing. Please check back later!")
        return      # immediately exit the function and go back to wherever the function was called from.
    
    print(f"\n  {'ID':<4} {'Title':<20} {'Language':<12} {'Director':<18} {'Year':<6} {'Booked / Total'}")
    print(f"  {'-' * 85}")
    for index, movie in enumerate(movie_inventory, start=1):
        director, year = movie["info"]
        print(f"  {index:<4} {movie['title']:<20} {movie['language']:<12} {director:<18} {year:<6} {movie['booked_tickets']} / {movie['total_tickets']}")

# [1C] Admin Add Movie
def admin_1c_add_movie(title, director, year, language, timings, total_tickets, price_2d, price_premier):
    if title.lower() in movie_names_set:
        print(f"  ⚠️ '{title}' is already in the database!")
        return

    movie_names_set.add(title.lower())
    movie_inventory.append({
        "title": title, "language": language, "timings": timings,
        "total_tickets": total_tickets, "booked_tickets": 0,
        "price_2d": price_2d, "price_premier": price_premier,
        "info": (director, year) 
    })

# [1D] Admin Delete Movie
def admin_1d_delete_movie():
    print("\n  --- 🗑️ Delete a Movie ---")
    if not movie_inventory: 
        print("\n  ⚠️ The collection is empty.")
        return
        
    title_input = shared_get_valid_input("  Enter exact movie title to delete (or 'home'): ").lower()
    if title_input == "home": return
        
    for movie in movie_inventory:
        if movie["title"].lower() == title_input:
            if input("  Confirm delete? (yes/no): ").strip().lower() in ["yes", "y"]:
                movie_names_set.remove(movie["title"].lower())
                movie_inventory.remove(movie)
                print("  ✅ Movie deleted.")
            return
    print("  ❌ Movie not found.")

# =================================================================================
# [2] CUSTOMER FLOW FUNCTIONS
# =================================================================================

# [2A] Customer Portal (Entry Point for Customer)
def customer_2a_portal():
    customer_2b_display_movies()
    while True:
        print("""
  =============================================
  🍿  CUSTOMER MENU
  =============================================
  1. View Movies       3. Search Movie
  2. Book Ticket       4. Return Home""")
        match input("  How can we help? (1-4): ").strip():
            case "1": customer_2b_display_movies()
            case "2": customer_2c_book_ticket()
            case "3": customer_2d_search_movie()
            case "4": break
            case _: print("  🌸 Oops! Invalid choice.")

# [2B] Customer View Movies
def customer_2b_display_movies():
    if not movie_inventory:
        print("\n  🌸 We currently have no movies showing. Please check back later!")
        return

    unique_langs = {movie["language"] for movie in movie_inventory}
    print(f"\n  🍿 Available today in: {', '.join(unique_langs)}")
    # print(movie_inventory)
    print(f"  {'ID':<4} {'Title':<20} {'Language':<12} {'Timings':<22} {'2D':<7} {'Premier':<9} {'Available Seats'}")
    print(f"  {'-' * 95}")
    for index, movie in enumerate(movie_inventory, start=1):
        avail = movie['total_tickets'] - movie['booked_tickets']
        status = f"{avail} seats" if avail > 0 else "Sold Out"
        print(f"  {index:<4} {movie['title']:<20} {movie['language']:<12} {movie['timings']:<22} ₹{movie['price_2d']:<6} ₹{movie['price_premier']:<8} {status}")
    print(f"  {'-' * 95}")

# [2C] Customer Book Ticket
def customer_2c_book_ticket():
    print("\n  --- 🎟️ Book Your Tickets ---")
    selected_movie = None
    
    while True:
        t_input = shared_get_valid_input("  Enter the movie name (or just a part of it) to book (or 'home'): ").lower()
        if t_input == "home": return

        matches = [m for m in movie_inventory if t_input in m["title"].lower()]
                 # decalred in loop like int m in c++
        if len(matches) == 0:
            print("  🌸 We couldn't find that movie. Let's try again.")
        elif len(matches) > 1:
            print("  🌸 Multiple movies found. Please be more specific:")
            for m in matches: print(f"     - {m['title']}")
        else:
            selected_movie = matches[0]
            break

    avail = selected_movie["total_tickets"] - selected_movie["booked_tickets"]
    if avail == 0:
        print(f"\n  😔 We are so sorry, but '{selected_movie['title']}' is fully sold out.")
        return
        
    print(f"\n  Excellent! Booking '{selected_movie['title']}'.\n  🕒 Timings:")
    timings_list = [t.strip() for t in selected_movie["timings"].split(",")]
    for i, t in enumerate(timings_list, start=1): print(f"     {i}. {t}")
        
    while True:
        tc = input(f"  Which show timing? (1-{len(timings_list)}): ").strip()
        if tc.isdigit() and 1 <= int(tc) <= len(timings_list):
            pref_timing = timings_list[int(tc) - 1]
            break
        print("  🌸 Invalid choice.")

    print(f"\n  1. Standard 2D (₹{selected_movie['price_2d']})\n  2. Premier (₹{selected_movie['price_premier']})")
    while True:
        type_choice = input("  Experience preference (1 or 2): ").strip()
        if type_choice in ["1", "2"]:
            price = selected_movie['price_2d'] if type_choice == "1" else selected_movie['price_premier']
            s_type = "Standard 2D" if type_choice == "1" else "Premier"
            break
        print("  🌸 Please choose 1 or 2.")

    while True:
        qty_str = input(f"  How many tickets? (Available: {avail}): ").strip()
        if qty_str.isdigit() and 0 < int(qty_str) <= avail:
            qty = int(qty_str)
            break
        print("  🌸 Please enter a valid available quantity.")
            
    print(f"\n  --- 🧾 Order Summary ---\n  Movie: {selected_movie['title']}\n  Time: {pref_timing}\n  Class: {s_type}\n  Seats: {qty}\n  Total: ₹{qty * price}")
    
    while True:
        confirm = input("\n  Confirm booking? (yes/no): ").strip().lower()
        if confirm in ["yes", "y"]:
            selected_movie["booked_tickets"] += qty
            print("  🎉 Wonderful! Your tickets are booked. Returning home.")
            return 
        elif confirm in ["no", "n"]:
            print("  🌸 Booking cancelled. Returning home.")
            return

# [2D] Customer Search Movie
def customer_2d_search_movie():
    print("\n  --- 🔍 Find a Movie ---")
    keyword = shared_get_valid_input("  Please enter a movie name to search (or type 'home'): ").lower()
    if keyword == "home": return
        
    found = False
    for movie in movie_inventory:
        if keyword in movie["title"].lower():
            d, y = movie["info"]
            avail = movie['total_tickets'] - movie['booked_tickets']
            print(f"\n  🎬 {movie['title']} ({movie['language']}) | Director: {d}\n  🕒 Timings: {movie['timings']}")
            print(f"  ✨ 2D: ₹{movie['price_2d']} | Premier: ₹{movie['price_premier']} | Status: {'Available' if avail > 0 else 'Sold Out'}")
            found = True
            
    if not found: print(f"  🌸 We couldn't find any movie matching '{keyword}'.")

# =================================================================================
# [3] MAIN EXECUTION
# =================================================================================

def main():
    # Setup initial background data
    setup_load_initial_movies()
    
    while True:
        print("""
            🌟  MAIN GATEWAY - 'Welcome to StarLight Cinemas' 🌟 
 
  1. Admin Login    
  2. Customer Portal  
  3. Exit"""
        )
        match input("  Select access level (1-3): ").strip():
            case "1":
                if input("  Password: ").strip() == "itsme12": 
                    admin_1a_dashboard()
                else: 
                    print("  ❌ Access Denied.")
            case "2": 
                customer_2a_portal()
            case "3": 
                print("\n  🌸 Have a wonderful day!\n")
                break
            case _: 
                print("  🌸 Invalid option.")

#----------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    now = datetime.now()
    current_date = now.strftime("%d-%b-%Y")
    print(f" 📅  Date: {current_date}")
    
    main()
