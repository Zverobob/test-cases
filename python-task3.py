class BaseConverter:
    def __init__(self, celsius):
        self.celsius = celsius
        self.convert()

    def convert(self):
        self.fahrenheit = (self.celsius * 9 / 5) + 32
        self.kelvin = self.celsius + 273.15

    def rewrite(self, data):
        self.celsius = data
        self.convert()


if __name__ == "__main__":
    inp = float(input("Enter your temperature in Celsius: "))
    deg = BaseConverter(inp)
    while True:
        option = float(
            input(
                f"Current Celsius:{deg.celsius}C\nChoose your option:\n1.Convert to Fahrenheit\n2.Convert to Kelvin\n3.Re-enter temperature\n4.Exit"
            )
        )
        if option == 1:
            print(f"\nFahrenheit: {deg.fahrenheit}F")
        elif option == 2:
            print(f"\nKelvin: {deg.kelvin}K")
        elif option == 3:
            deg.rewrite(float(input("Enter your temperature in Celsius: ")))
        elif option == 4:
            break
    print("---Job's done---")
