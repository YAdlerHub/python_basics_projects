import math

def evaluate_expression(expression):
    """Evaluates a mathematical expression with support for power (^) and square root (sqrt)."""
    try:
        # Replace power operator (^) with Python's exponentiation operator (**)
        expression = expression.replace("^", "**")
        
        # Replace 'sqrt' with 'math.sqrt' to allow square root calculations
        expression = expression.replace("sqrt(", "math.sqrt(")
        
        # Evaluate the mathematical expression safely
        result = eval(expression, {"math": math, "__builtins__": {}})
        
        return result
    except Exception as e:
        return f"❌ Error: Invalid expression ({e})"

def calculator():
    print("\n🔢 Advanced Calculator - Enter any mathematical expression")
    print("💡 Supports +, -, *, /, %, ^ (power), sqrt(x) (square root), and parentheses ()")
    
    while True:
        expression = input("\n➡️ Enter expression (or 'exit' to quit): ").strip().lower()
        
        if expression == "exit":
            print("👋 Thank you! Goodbye!")
            break
        
        result = evaluate_expression(expression)
        print(f"✅ Result: {result}")

# Run the calculator
if __name__ == "__main__":
    calculator()
