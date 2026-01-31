import length
import volume
import weight
import os 

options = {
    "1": ("Length", length.run),
    "2": ("Volume", volume.run),
    "3": ("Weight", weight.run),
}

print("\nSelect measurement type:\n")

for k, (name, _) in options.items():
    print(f"{k}. {name}")

choice = input("\nEnter choice: ")

if choice in options:
    os.system("clear")
    options[choice][1]()   # calls the selected run() function
else:
    print("Invalid selection")
