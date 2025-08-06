def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(n-1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n-1, auxiliary, destination, source)


try:
    n = int(input("Enter the number of disks: "))
    if n <= 0:
        print("Number of disks must be positive.")
    else:
        tower_of_hanoi(n, 'A', 'C', 'B')
except ValueError:
    print("Please enter a valid integer.")
