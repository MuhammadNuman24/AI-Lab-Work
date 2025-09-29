# Define a dictionary for adjacent provinces
adjacent_provinces = {
    "Punjab": ["Sindh", "Khyber Pakhtunkhwa", "Islamabad", "Azad Kashmir"],
    "Sindh": ["Punjab", "Balochistan"],
    "Khyber Pakhtunkhwa": ["Punjab", "Islamabad", "Gilgit-Baltistan", "Afghanistan"],
    "Balochistan": ["Sindh", "Punjab", "Iran", "Afghanistan"],
    "Islamabad": ["Punjab", "Khyber Pakhtunkhwa"],
    "Gilgit-Baltistan": ["Khyber Pakhtunkhwa", "Azad Kashmir"],
    "Azad Kashmir": ["Punjab", "Khyber Pakhtunkhwa", "Gilgit-Baltistan", "India"]
}

# Define a list for coastal provinces
coastal_provinces = ["Sindh", "Balochistan"]

def get_adjacent_provinces(province):
    """Return adjacent provinces for a given province."""
    return adjacent_provinces.get(province, [])

def is_coastal_province(province):
    """Check if a province is coastal."""
    return province in coastal_provinces

def main():
    print("Geography Analysis of Pakistan's Provinces")
    print("-----------------------------------------")
    
    province = input("Enter a province of Pakistan: ")
    
    print(f"\nAdjacent provinces to {province}:")
    print(get_adjacent_provinces(province))
    
    print(f"\nIs {province} a coastal province?")
    print(is_coastal_province(province))

if __name__ == "__main__":
    main()
