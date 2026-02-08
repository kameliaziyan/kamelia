# Class Exercises: Classes

## General Requirements

- Do not use any Generative-AI (like ChatGPT) tools to solve these exercises. The purpose is to practice your own skills. You can use Generative-AI tools to help you understand concepts, but not to generate the solution code.
- Provide unit tests where asked using the `pytest` framework.
- All the unit tests should be in a Python package called `tests`. Use a separate Python module for each exercise test suite.
- The unit test module should be called by convention `test_<subject>.py`
- Adhere to Python coding standards PEP-8
- Use Type Hints for function arguments and return values
- If the functions is long (beyond 15 lines of code), divide into more functions.
- Linting and Formatting Requirements - The Solution and the test code must be:
  - Formatted with `black` formatter before submission.
  - Pass `flake8` checks before submission. Use `wps explain <error code>` to understand the error and how to write correctly.
  - Pass `mypy` type checks before submission.
- Navigate to the `linter-config` directory to find the `setup.cfg` file with the linters configuration. Copy all files to the root of your exercise directory to use the same configuration for your exercises.
---

## Exercise 1: E-commerce System with Multiple Inheritance

**Description:**
Create a class hierarchy that demonstrates multiple inheritance in a real-world e-commerce scenario. You'll implement classes that handle different aspects of an online store: inventory management, discount pricing, and shipping calculations. The final `Product` class will inherit from multiple base classes and override methods appropriately.

**Requirements:**
- Create a base class `Item` with:
  - Instance attributes: `name` (str), `base_price` (float), `weight` (float in kg)
  - Method `get_info() -> str` that returns a formatted string with item details

- Create a mixin class `DiscountMixin` with:
  - Instance attribute: `discount_percent` (float, default 0)
  - Method `get_price() -> float` that returns the price after applying discount

- Create a mixin class `ShippingMixin` with:
  - Class attribute: `shipping_rate_per_kg` = 5.0 (dollars per kg)
  - Method `get_shipping_cost() -> float` that calculates shipping based on weight

- Create a class `Product` that inherits from `Item`, `DiscountMixin`, and `ShippingMixin`:
  - Override the `get_info()` method to include discount and shipping information
  - Implement a method `get_total_cost() -> float` that returns price + shipping
  - The constructor should accept: name, base_price, weight, and optional discount_percent

- Create a class `DigitalProduct` that inherits from `Item` and `DiscountMixin` only:
  - Override `get_info()` to mention it's a digital product (no shipping)
  - The constructor should accept: name, base_price, and optional discount_percent
  - Weight should be set to 0.0

- Include comprehensive type hints for all methods
- Write at least 3 unit tests that verify:
  - MRO (Method Resolution Order) works correctly
  - Method overriding functions as expected
  - Different combinations of inherited behavior work correctly

**Example:**

```python
# Physical product with discount
laptop = Product("Laptop", 1000.0, 2.5, discount_percent=10)
print(laptop.get_price())  # Output: 900.0
print(laptop.get_shipping_cost())  # Output: 12.5
print(laptop.get_total_cost())  # Output: 912.5
print(laptop.get_info())
# Output: "Product: Laptop, Price: $900.00, Shipping: $12.50, Total: $912.50"

# Digital product (no shipping)
ebook = DigitalProduct("Python Guide", 29.99, discount_percent=20)
print(ebook.get_price())  # Output: 23.992
print(ebook.get_info())
# Output: "Digital Product: Python Guide, Price: $23.99 (no shipping)"
```

---

## Exercise 2: Vector Class with Operator Overloading

**Description:**
Create a `Vector2D` class that represents a 2D vector and implements various dunder methods for operator overloading. This will help you understand how Python's special methods work and how to make your classes behave like built-in types.

**Requirements:**
- Create a `Vector2D` class with:
  - Instance attributes: `x` (float), `y` (float)
  - `__init__(self, x: float, y: float)` - constructor
  - `__str__(self) -> str` - returns string representation like "Vector2D(3.0, 4.0)"
  - `__repr__(self) -> str` - returns the same as `__str__`
  - `__eq__(self, other: object) -> bool` - checks if two vectors are equal
  - `__add__(self, other: "Vector2D") -> "Vector2D"` - adds two vectors
  - `__sub__(self, other: "Vector2D") -> "Vector2D"` - subtracts two vectors
  - `__mul__(self, scalar: float) -> "Vector2D"` - multiplies vector by a scalar
  - `__abs__(self) -> float` - returns the magnitude (length) of the vector
  - `magnitude(self) -> float` - returns the magnitude using the Pythagorean theorem
  - `dot(self, other: "Vector2D") -> float` - returns the dot product of two vectors

- The `__eq__` method should handle comparison with non-Vector2D objects gracefully (return False)
- Include comprehensive type hints for all methods
- Write at least 3 unit tests that verify:
  - Operator overloading works correctly
  - Comparison and equality work as expected
  - Edge cases (zero vector, negative components, etc.) are handled

**Example:**

```python
v1 = Vector2D(3.0, 4.0)
v2 = Vector2D(1.0, 2.0)

print(v1 + v2)  # Output: Vector2D(4.0, 6.0)
print(v1 - v2)  # Output: Vector2D(2.0, 2.0)
print(v1 * 2)   # Output: Vector2D(6.0, 8.0)
print(abs(v1))  # Output: 5.0
print(v1.dot(v2))  # Output: 11.0
print(v1 == Vector2D(3.0, 4.0))  # Output: True
```

---

## Exercise 3: BankAccount with Properties and Encapsulation

**Description:**
Design and implement a `BankAccount` class that demonstrates proper use of properties, encapsulation, and validation. Your class should protect account data from invalid modifications while providing a clean interface for banking operations.

**Learning Objectives:**
- Use properties to control access to class attributes
- Implement encapsulation with private attributes
- Add validation logic to enforce business rules
- Raise appropriate exceptions for invalid operations

**Requirements:**
- Design a `BankAccount` class that supports basic banking operations (deposits, withdrawals, balance inquiries)
- Protect sensitive account data from direct modification outside the class
- Prevent invalid operations such as:
  - Depositing or withdrawing negative or zero amounts
  - Withdrawing more money than available in the account
- Track useful information about the account's activity
- Provide a way to view account information in a user-friendly format

**Design Considerations:**
- What attributes should be private vs. public?
- Which attributes should be read-only, and which should be modifiable?
- What methods are needed for safe account operations?
- How should invalid operations be handled (exceptions, return values)?
- What validation rules make sense for a bank account?

**Testing Requirements:**
- Write at least 3 comprehensive unit tests that verify:
  - Encapsulation: Protected data cannot be modified directly
  - Validation: Invalid operations are properly rejected
  - Business logic: Account operations work correctly under various scenarios

**Example Usage:**
Your implementation should support usage similar to this (exact method names and behavior are up to you):

```python
account = BankAccount("ACC123456")  # Create account with initial balance of 0

# Deposit money
account.deposit(1000.0)
print(account.balance)  # Should show 1000.0

# Withdraw money
account.withdraw(300.0)
print(account.balance)  # Should show 700.0

# Attempt invalid withdrawal (should raise an exception)
account.withdraw(800.0)  # Should fail - insufficient funds

# Attempt to modify balance directly (should fail)
account.balance = 5000.0  # Should raise an error - balance is protected

# View account information
print(account.get_statement())  # Display account details
```

**Note:** The exact implementation is up to you. Focus on proper encapsulation, validation, and creating a clean, intuitive interface.

---

## Exercise 4: Employee Management System with Single Inheritance

**Description:**
Design and implement an employee management system that demonstrates single inheritance. Your system should model different types of employees in a company, where specialized employee types inherit from more general ones. The inheritance hierarchy should reflect real-world organizational structures.

**Learning Objectives:**
- Understand and implement single inheritance hierarchies
- Practice method overriding and extension in subclasses
- Use `super()` to call parent class methods
- Design class hierarchies that reflect real-world relationships
- Implement polymorphism through inheritance

**Requirements:**
- Create a class hierarchy with 2-3 levels of inheritance (no more than 3 levels)
- The base class should represent a general employee with common attributes and behavior
- Derived classes should represent more specialized types of employees
- Each level of inheritance should add or modify behavior appropriately
- Demonstrate at least one case of:
  - Method overriding (child class replaces parent method completely)
  - Method extension (child class calls parent method and adds additional behavior)
- All employees should be able to calculate their compensation, but the calculation may differ by type
- The system should be able to handle a collection of different employee types polymorphically

**Business Rules and Data Requirements:**

The system must track three types of employees with the following data and compensation rules:

1. **Base Employee (Entry-level/Contractor):**
   - Required data: employee ID, full name, hourly rate ($/hour)
   - Compensation formula: `hourly_rate × 160` (assumes 160 hours/month)
   - Work schedule: Standard 40 hours/week

2. **Full-Time Employee (Salaried):**
   - Inherits from Base Employee
   - Additional data: annual salary, department name
   - Compensation formula: `annual_salary / 12` (monthly salary)
   - Benefits: Receives standard company benefits package
   - Override hourly rate concept with fixed salary

3. **Manager (Senior Leadership):**
   - Inherits from Full-Time Employee
   - Additional data: team size (number of direct reports), bonus percentage (as decimal, e.g., 0.15 for 15%)
   - Compensation formula: `(annual_salary / 12) × (1 + bonus_percentage)` (monthly salary + bonus)
   - Benefits: Same as Full-Time Employee plus bonus compensation
   - Additional responsibility: Must track and report team size

**Specific Requirements:**
- Employee IDs must be stored and retrievable
- All monetary values should be in dollars (float)
- Compensation calculations must return monthly pay amounts
- Each employee type must be able to display their information including their specific attributes
- The system should clearly show the difference between hourly, salaried, and bonus-based compensation

**Design Considerations:**
- How should you structure the inheritance: Base → Full-Time → Manager?
- What attributes are common to all employees (should be in base class)?
- Which compensation calculation should be in the base class, and how should subclasses override it?
- How can Full-Time Employee override the hourly rate concept with salary?
- How can Manager extend the Full-Time Employee's compensation with bonuses?
- How should `super()` be used to avoid duplicating the salary calculation in Manager?
- What information should each employee display, and how should subclasses extend this?

**Example Usage:**
Your implementation should support usage similar to this (exact method names are up to you):

```python
# Create different types of employees
contractor = Employee("E001", "Alice Johnson", 25.0)  # $25/hour
full_timer = FullTimeEmployee("E002", "Bob Smith", 90000, "Engineering")  # $90k/year
manager = Manager("E003", "Carol White", 150000, "Engineering", 8, 0.15)  # $150k/year, 8 reports, 15% bonus

# All employees can display their information
print(contractor.get_info())
# Example output: "Employee E001: Alice Johnson, Hourly Rate: $25.00/hr"

print(full_timer.get_info())
# Example output: "Full-Time Employee E002: Bob Smith, Department: Engineering, Salary: $90,000/year"

print(manager.get_info())
# Example output: "Manager E003: Carol White, Department: Engineering, Salary: $150,000/year, Team Size: 8, Bonus: 15%"

# Calculate monthly compensation (each type uses different formula)
contractor_pay = contractor.calculate_compensation()
print(contractor_pay)    # Output: 4000.0 (25 * 160)

full_timer_pay = full_timer.calculate_compensation()
print(full_timer_pay)    # Output: 7500.0 (90000 / 12)

manager_pay = manager.calculate_compensation()
print(manager_pay)       # Output: 14062.5 (150000/12 * 1.15)

# Demonstrate polymorphism - treat all employees uniformly
employees = [contractor, full_timer, manager]
total_monthly_payroll = sum(emp.calculate_compensation() for emp in employees)
formatted_total = f"${total_monthly_payroll:,.2f}"
print(f"Total monthly payroll: {formatted_total}")
# Output: Total monthly payroll: $25,562.50

# Each employee type can be used through the same interface
for emp in employees:
    emp_info = emp.get_info()
    emp_pay = emp.calculate_compensation()
    formatted_pay = f"${emp_pay:,.2f}"
    print(f"{emp_info} - Monthly Pay: {formatted_pay}")
```

**Testing Requirements:**
- Write at least 5 unit tests that verify:
  - Base Employee compensation calculation (hourly rate × 160 = monthly pay)
  - Full-Time Employee compensation calculation (annual salary ÷ 12 = monthly pay)
  - Manager compensation calculation with bonus ((annual salary ÷ 12) × (1 + bonus percentage) = monthly pay)
  - Polymorphism: All three employee types can be stored in a collection and their compensation calculated uniformly
  - Information display includes all relevant data for each employee type (ID, name, and type-specific fields)

**Constraints:**
- Maximum 3 levels of inheritance (Employee → FullTimeEmployee → Manager)
- Use type hints for all method parameters and return values
- Each class should have a clear, single responsibility
- Use `super()` where appropriate to avoid code duplication

**Note:** While the business requirements and formulas are specified, you must design the class structure, method names, and implementation details yourself.
