import argparse
import sys


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

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(
        description="Calculate the area of a triangle using base and height",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python triangle_area_cli.py 10 5
  python triangle_area_cli.py --base 7.5 --height 4.2
  python triangle_area_cli.py -b 12 --height 8
        """
    )
    
    # Add positional arguments
    parser.add_argument('base', nargs='?', type=float, 
                       help='Base of the triangle')
    parser.add_argument('height', nargs='?', type=float, 
                       help='Height of the triangle')
    
    # Add optional arguments (alternative way to specify base and height)
    parser.add_argument('-b', '--base', dest='base_opt', type=float,
                       help='Base of the triangle (alternative to positional argument)')
    parser.add_argument('--height', dest='height_opt', type=float,
                       help='Height of the triangle (alternative to positional argument)')
    
    # Add version option
    parser.add_argument('--version', action='version', version='Triangle Calculator 1.0')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Determine base and height values
    base = args.base if args.base is not None else args.base_opt
    height = args.height if args.height is not None else args.height_opt
    
    # Validate inputs
    if base is None or height is None:
        print("Error: Both base and height are required.")
        print("\nUsage examples:")
        print("  python triangle_area_cli.py 10 5")
        print("  python triangle_area_cli.py --base 10 --height 5")
        print("  python triangle_area_cli.py -b 10 --height 5")
        sys.exit(1)
    
    # Validate that values are positive
    if base <= 0 or height <= 0:
        print("Error: Base and height must be positive numbers.")
        sys.exit(1)
    
    
    try:
        # Calculate area
        area = triangle_area(base, height)
        
        # Display result
        print(f"Triangle area calculation:")
        print(f"Base: {base}")
        print(f"Height: {height}")
        print(f"Area: {area:.2f}")
        
    except Exception as e:
        print(f"Error calculating area: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()