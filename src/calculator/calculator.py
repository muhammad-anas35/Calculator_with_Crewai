class Calculator:
    """A simple calculator class that provides basic mathematical operations."""

    def __init__(self):
        """Initialize the calculator."""
        self.last_result = 0

    def add(self, x: float, y: float) -> float:
        """Add two numbers.
        
        Args:
            x (float): First number
            y (float): Second number
            
        Returns:
            float: Sum of x and y
        """
        self.last_result = x + y
        return self.last_result

    def subtract(self, x: float, y: float) -> float:
        """Subtract two numbers.
        
        Args:
            x (float): First number
            y (float): Second number
            
        Returns:
            float: Difference of x and y
        """
        self.last_result = x - y
        return self.last_result

    def multiply(self, x: float, y: float) -> float:
        """Multiply two numbers.
        
        Args:
            x (float): First number
            y (float): Second number
            
        Returns:
            float: Product of x and y
        """
        self.last_result = x * y
        return self.last_result

    def divide(self, x: float, y: float) -> float:
        """Divide two numbers.
        
        Args:
            x (float): First number
            y (float): Second number
            
        Returns:
            float: Quotient of x and y
            
        Raises:
            ValueError: If y is zero
        """
        if y == 0:
            raise ValueError("Cannot divide by zero")
        self.last_result = x / y
        return self.last_result

    def power(self, x: float, y: float) -> float:
        """Calculate x raised to the power of y.
        
        Args:
            x (float): Base number
            y (float): Exponent
            
        Returns:
            float: x raised to the power of y
        """
        self.last_result = x ** y
        return self.last_result

    def get_last_result(self) -> float:
        """Get the last calculated result.
        
        Returns:
            float: The last calculated result
        """
        return self.last_result

    def clear(self) -> None:
        """Clear the last result."""
        self.last_result = 0


def main():
    """Test function to demonstrate calculator usage."""
    # Create a calculator instance
    calc = Calculator()
    
    # Perform some calculations
    print("Testing Calculator Operations:")
    print("-" * 25)
    
    # Addition
    result = calc.add(5, 3)
    print(f"5 + 3 = {result}")
    
    # Subtraction
    result = calc.subtract(10, 4)
    print(f"10 - 4 = {result}")
    
    # Multiplication
    result = calc.multiply(6, 7)
    print(f"6 * 7 = {result}")
    
    # Division
    result = calc.divide(20, 5)
    print(f"20 / 5 = {result}")
    
    # Power
    result = calc.power(2, 3)
    print(f"2 ^ 3 = {result}")
    
    # Last result
    print(f"Last result: {calc.get_last_result()}")
    
    # Test division by zero error handling
    try:
        calc.divide(10, 0)
    except ValueError as e:
        print(f"Error caught: {e}")


if __name__ == "__main__":
    main()


