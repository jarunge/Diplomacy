########################################################################
#################    Territories    ####################################
supply_centers = [
    'London', 'Liverpool', 'Edinburgh', 'Brest', 'Marseilles', 'Kiel', 'Denmark', 'Holland',
    'Portugal', 'Spain', 'Belgium', 'Norway', 'Sweden', 'Finland', 'St. Petersburg', 'Constantinople',
    'Smyrna', 'Rumania', 'Bulgaria', 'Greece', 'Serbia', 'Trieste', 'Venice', 'Naples', 'Rome',
    'Munich', 'Berlin', 'Vienna', 'Warsaw', 'Moscow', 'Sevastopol', 'Ankara'
]

Empty_land = [
    #  Western
    "Clyde", "Yorkshire", "Wales", 
    "Picardy", "Burgundy", "Gascony"
    "Ruhr", "Finlland"
    # Midline
    "North Africa", "Piedmont", "Tyrolia", "Bohemia", "Silesia", "Prussia", "Livonia", 
    "Apulia", "Tuscany", 
    # Eastern
    "Tuscany", "Apulia", 
    "Syria", "Armenia", "Ukraine", "Galicia", "Albania"
]

coastal_land = [
    "Clyde", "Edinburgh", "Yorkshire", "Wales", "London", "Liverpool", 
    "Marseilles", "Spain", "Portugal", "Gascony", "Brest", "Picardy", 
    "Belgium", "Holland", "Denmark", "Kiel", "Berlin"
    "Norway", "Sweden", "Finland", "St. Petersburg", "Livonia", "Prussia", 
    "Sevastopol", "Rumania", "Bulgaria", "Armenia",
    "Constantinople", "Smyrna", "Ankara", "Armenia", 
    "Greece", "Albania", "Trieste", 
    "Venice", "Piedmont", "Tuscany", "Rome", "Naples", "Apulia", 
    "Tunis", "North Africa"
]

sea_territories = [
    # North
    "North Atlantic", "Irish Sea", "English Channel", "Mid-Atlantic Ocean", 
    "North Sea", "Norwegian Sea", "Skagerrak", "Helgoland Bight", "Barents Sea",
    "Baltic Sea", "Gulf of Bothnia",
    # South
    "Gulf of Lyon", "Western Mediterranean", "Tyrrhenian Sea", 
    "Ionian Sea", "Adriatic Sea", 
    "Aegean Sea", "Eastern Mediterranean", 
    "Black Sea"
]

#############################################################################
################   Connections between Territories     ######################
#############################################################################

# Connections between supply centers
supply_center_connections = [
    # Western
    ('London', 'Liverpool'), ('Liverpool', 'Edinburgh'), 
    ('Brest', 'Paris'),
    ('Spain', 'Marseilles'), ('Spain', 'Portugal'), 
    ('Belgium', 'Holland'),
    ('Kiel', 'Holland'), ('Kiel', 'Denmark'), ('Kiel', 'Berlin'), ('Kiel', 'Munich'),
    ('Sweden', 'Denmark'), ('Sweden', 'Norway'), 
    ('St Petersburg', 'Norway'), ('St. Petersburg', 'Moscow'),
    # Eastern
    ('Ankara', 'Smyrna'), ('Ankara, Constantinople'), ('Constantinople', 'Smyrna'),
    ('Bulgaria', 'Constantinople'), ('Bulgaria', 'Rumania'), ('Bulgaria', 'Serbia'), ('Bulgaria', 'Greece'),
    ('Sevastopol', 'Rumania'), ('Sevastopol', 'Moscow'),
    ('Warsaw', 'Moscow'), ('Budapest', 'Rumania'),
    ('Serbia', 'Trieste'), ('Serbia', 'Budapest'), ('Serbia', 'Rumania'), ('Serbia', 'Greece'),
    ('Sevastopol', 'Rumania'), ('Rumania', 'Bulgaria'), ('Rumania', 'Serbia'),
    ('Vienna', 'Trieste'), ('Vienna', 'Budapest'), ('Vienna', 'Venice'),
    ('Rome', 'Venice'), ('Rome', 'Naples')
]

supply_empty_connections = [
    # Western
    ('Liverpool', 'Clyde'), ('Liverpool', 'Wales'), ('Liverpool', 'Yorkshire'),
    ('Edinburgh', 'Clyde'), ('Edinburgh', 'Yorkshire'), 
    ('London', 'Wales'), ('London', 'Yorkshire'),
    ('Brest', 'Gascony'), ('Brest', 'Picardy'),
    ('Paris', 'Gascony'), ('Paris', 'Burgundy'), ('Paris', 'Picardy'),
    ('Marseilles', 'Gascony'), ('Marseilles', 'Burgundy'), ('Marseilles', 'Piedmont'),
    ('Spain', 'Gascony'),
    ('Belgium', 'Picardy'), ('Belgium', 'Burgundy'),
    ('Holland', 'Ruhr'), 
    ('Kiel', 'Ruhr'), 
    ('Munich', 'Ruhr'), ('Munich', 'Burgundy'), 
    ('Munich', 'Tyrolia'), ('Munich', 'Bohemia'), ('Munich', 'Silesia'), 
    ('Sweden', 'Finland'), ('Norway', 'Finland'), 
    ('St Petersburg', 'Finland'), ('St Petersburg', 'Livonia'),
    # Eastern
    ('Ankara', 'Armenia'), 
    ('Smryna', 'Armenia'), ('Smryna', 'Syria'),
    ('Sevastopol', 'Armenia'), ('Sevastopol', 'Ukraine'),
    ('Moscow', 'Livonia'), ('Moscow', 'Ukraine'),
    ('Warsaw', 'Galicia'), ('Warsaw', 'Prussia'), ('Warsaw', 'Silesia'),
    ('Warsaw', 'Ukraine'), ('Warsaw', 'Livonia'),
    ('Serbia', 'Albania'), 
    ('Budapest', 'Galicia'), 
    ('Vienna', 'Galicia'), ('Vienna', 'Bohemia'), ('Vienna', 'Tyrolia'),
    ('Trieste', 'Albania'), ('Trieste', 'Tyrolia'),
    ('Venice', 'Tyrolia'), ('Venice', 'Piedmont'),
    ('Venice', 'Apulia'), ('Venice', 'Tuscany'),
    ('Rome', 'Tuscany'), ('Rome', 'Apulia'), 
    ('Naples', 'Apulia'),
    ('Tunis', 'North Africa')
]


coastal_supply_connections = [
    # Western
    ('Liverpool', 'Irish Sea'), ('Liverpool', 'North Atlantic Ocean'),
    ('Edinburgh', 'North Sea'), ('Edinburgh', 'Norwegian Sea'),
    ('London', 'North Sea'), ('London', 'English Channel'),
    ('Brest', 'Mid-Atlantic Ocean'), ('Brest', 'English Channel'), 
    ('Portugal', 'Mid-Atlantic Ocean'), 
    ('Spain', 'Mid-Atlantic Ocean'), ('Spain', 'Gulf of Lyon'), ('Spain', 'Western Mediterranean'),
    ('Marseilles', 'Gulf of Lyon'), 
    ('Belgium', 'North Sea'), ('Belgium', 'English Channel'),
    ('Holland', 'North Sea'), ('Holland', 'Heligoland Bight'),
    ('Kiel', 'Heligoland Bight'), ('Kiel', 'Baltic Sea'),
    ('Denmark', 'Heligoland Bight'), ('Denmark', 'North Sea'), 
    ('Denmark', 'Skagerrak'), ('Denmark', 'Baltic Sea'),
    ('Norway', 'North Sea'), ('Norway', 'Norwegian Sea'), ('Norway', 'Skagerrak'), ('Norway', 'Barents Sea'),
    ('Sweden', 'Skagerrak'), ('Sweden', 'Baltic Sea'), ('Sweden', 'Gulf of Bothnia'),
    ('St Petersburg', 'Gulf of Bothnia'), ('St Petersburg', 'Norwegian Sea'),
    # Eastern
    ('Ankara', 'Black Sea'), 
    ('Constantinople', 'Black Sea'), ('Constantinople', 'Aegean Sea'), 
    ('Smyrna', 'Aegean Sea'), ('Smyrna', 'Eastern Mediterranean'),
    ('Sevastopol', 'Black Sea'), ('Rumania', 'Black Sea'), ('Bulgaria', 'Black Sea'),
    ('Greece', 'Aegean Sea'), ('Greece', 'Ionian Sea'), 
    ('Triesete', 'Adriatic Sea'), ('Venice', 'Adriatic Sea'),
    ('Naples', 'Ionian Sea'), ('Naples', 'Tyrrhenian Sea'),
    ('Rome', 'Tyrrhenian Sea'), 
    ('Tunis', 'Tyrrhenian Sea'), ('Tunis', 'Western Mediterranean'), ('Tunis', 'Ionian Sea'),
]

coastal_empty_connections = [
    # Western
    ('Clyde', 'North Atlantic Ocean'), ('Clyde', 'Norwegian Sea'),
    ('Yorkshire', 'North Sea'),
    ('Wales', 'Irish Sea'), ('Wales', 'English Channel'),
    ('Gascony', 'Mid-Atlantic Ocean'), 
    ('Picardy', 'English Channel'), 
    ('Finland', 'Gulf of Bothnia'), 
    # Midline
    ('North Africa', 'Western Mediterranean'), ('North Africa', 'Mid-Atlantic Ocean'),
    ('Piedmont', 'Gulf of Lyon'), 
    ('Prussia', 'Baltic Sea'), 
    ('Livonia', 'Baltic Sea'), ('Livonia', 'Gulf of Bothnia')
    # Eastern
    ('Armenia', 'Black Sea'), 
    ('Syria', 'Eastern Mediterranean'),
    ('Albania', 'Ionian Sea'), ('Albania', 'Adriatic Sea'),
    ('Apulia', 'Ionian Sea'), ('Apulia', 'Adriatic Sea'), 
    ('Tuscany', 'Tyrrhenian Sea'), ('Tuscany', 'Gulf of Lyon')
]

sea_connections = [
    # North
    ("North Atlantic Ocean", "Mid-Atlantic Ocean"), ("North Atlantic Ocean", "Irish Sea"), ("North Atlantic Ocean", "Norwegian Sea"),
    ("Irish Sea", "Mid-Atlantic Ocean"),("Irish Sea", "English Channel"),
    ("Mid-Atlantic Ocean", "English Channel"), ("Mid-Atlantic Ocean", "Western Mediterranean"),
    ("North Sea", "Norwegian Sea"), ("North Sea", "English Channel"), 
    ("North Sea", "Skagerrak"), ("North Sea", "Heligoland Bight"), 
    ("Barents Sea", "Norwegian Sea"), ("Balitc Sea", "Gulf of Bothnia"), 
    # South
    ("Gulf of Lyon", "Western Mediterranean"), ("Gulf of Lyon", "Tyrrhenian Sea"),
    ("Western Mediterranean", "Tyrrhenian Sea"), 
    ("Ionian Sea", "Tyrrhenian Sea"), ("Ionian Sea", "Adriatic Sea"), 
    ("Ionian Sea", "Aegean Sea"), ("Ionian Sea", "Eastern Mediterranean"),
    ("Aegean Sea", "Eastern Mediterranean")
]
