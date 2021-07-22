liquid1_volume = float(input("Please enter the volume of first liquid: "))
liquid1_percent = float(input("Please enter alc_percentage of first liquid: "))
liquid2_size = float(input("Please enter the size of second liquid unit: "))
liquid2_percent = float(input("Please enter alc_percentage of second liquid: "))

num_units = liquid1_volume*liquid1_percent/(liquid2_size*liquid2_percent)

print(f"The amount of liquid 1 corresponds to {num_units} units of liquid2.")