def triangle_area(base, height):
    """
    Calculate the area of a triangle using base and height.
    
    Formula: Area = (base * height) / 2
    
    Args:
        base (float): The base of the triangle
        height (float): The height of the triangle
    
    Returns:
        float: The area of the triangle
    """
    area = (base * height) / 2
    return area


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