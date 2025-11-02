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
    # Test the function with some example values
    base = 10
    height = 5
    
    area = triangle_area(base, height)
    print(f"Triangle with base {base} and height {height} has area: {area}")
    
    # Another example
    base2 = 7.5
    height2 = 4.2
    area2 = triangle_area(base2, height2)
    print(f"Triangle with base {base2} and height {height2} has area: {area2}")