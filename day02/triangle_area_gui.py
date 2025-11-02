import tkinter as tk
from tkinter import ttk, messagebox


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


class TriangleAreaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Triangle Area Calculator")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="Triangle Area Calculator", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Base input
        ttk.Label(main_frame, text="Base:", font=("Arial", 12)).grid(row=1, column=0, sticky=tk.W, pady=5)
        self.base_entry = ttk.Entry(main_frame, font=("Arial", 12), width=15)
        self.base_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Height input
        ttk.Label(main_frame, text="Height:", font=("Arial", 12)).grid(row=2, column=0, sticky=tk.W, pady=5)
        self.height_entry = ttk.Entry(main_frame, font=("Arial", 12), width=15)
        self.height_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Calculate button
        self.calculate_btn = ttk.Button(main_frame, text="Calculate Area", 
                                       command=self.calculate_area)
        self.calculate_btn.grid(row=3, column=0, columnspan=2, pady=20)
        
        # Result display
        ttk.Label(main_frame, text="Result:", font=("Arial", 12, "bold")).grid(row=4, column=0, sticky=tk.W, pady=5)
        self.result_label = ttk.Label(main_frame, text="", font=("Arial", 12), 
                                     foreground="blue", background="lightgray", 
                                     relief="sunken", padding=5)
        self.result_label.grid(row=4, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Clear button
        self.clear_btn = ttk.Button(main_frame, text="Clear", command=self.clear_fields)
        self.clear_btn.grid(row=5, column=0, columnspan=2, pady=10)
        
        # Configure grid weights
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Bind Enter key to calculate
        root.bind('<Return>', lambda event: self.calculate_area())
        
        # Focus on base entry
        self.base_entry.focus()
    
    def calculate_area(self):
        """Calculate and display the triangle area"""
        try:
            # Get values from entries
            base_str = self.base_entry.get().strip()
            height_str = self.height_entry.get().strip()
            
            # Check if fields are empty
            if not base_str or not height_str:
                messagebox.showerror("Error", "Please enter both base and height values.")
                return
            
            # Convert to float
            base = float(base_str)
            height = float(height_str)
            
            # Check for negative values
            if base <= 0 or height <= 0:
                messagebox.showerror("Error", "Base and height must be positive numbers.")
                return
            
            # Calculate area
            area = triangle_area(base, height)
            
            # Display result
            self.result_label.config(text=f"{area:.2f}")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for base and height.")
    
    def clear_fields(self):
        """Clear all input fields and result"""
        self.base_entry.delete(0, tk.END)
        self.height_entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.base_entry.focus()


def main():
    # Create the main window
    root = tk.Tk()
    
    # Create the application
    app = TriangleAreaGUI(root)
    
    # Start the GUI event loop
    root.mainloop()


if __name__ == "__main__":
    main()