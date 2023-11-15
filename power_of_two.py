while True:
    try:
        # Get user input for a whole number
        num = int(input("Enter a whole number: "))

        # Validate that the number is non-negative
        if num < 0:
            print("Please enter a non-negative whole number.")
            continue  # Restart the loop to prompt the user again

        # Calculate and display the square (power of 2) for numbers from 0 to the input
        for i in range(num + 1):
            print(f"{i}^2 = {i*i}")

        break  # Exit the loop as the input was valid

    except ValueError:
        print("Invalid input. Please enter a whole number.")
