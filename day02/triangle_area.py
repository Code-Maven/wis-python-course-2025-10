from shapes import triangle_area

# Example usage
if __name__ == "__main__":
    #pass
    #...
    # Get base and height from user input
    try:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        
        # Calculate and display the area
        area = triangle_area(base, height)
        print(f"Triangle with base {base} and height {height} has area: {area}")
        
    except ValueError:
        print("Please enter valid numbers for base and height.")