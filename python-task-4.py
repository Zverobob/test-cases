class TimeDegreeCalculator:
    def __init__(self):
        print(
            "Enter your time. Dont't worry about the time format, we'll figure it out!"
        )
        self.hour, self.minute = map(
            int,
            input('Input time in a format "hh mm" or "hh:mm": ')
            .replace(":", " ")
            .split(),
        )

    def FindDegree(self):
        # Сначала проверяем формат времени, и фиксим его если 24 часа, а не 12. Но не перезаписываем, чтобы после вернуть пользвателю введённое время!
        time_fix_h = self.hour if self.hour <= 11 else self.hour - 12
        # От минутной до часовой
        degrees_m = abs((time_fix_h * 30) + (self.minute * 0.5) - (self.minute * 6))
        # От часовой до минутной
        degrees_h = 360 - degrees_m
        return (degrees_h, degrees_m)


if __name__ == "__main__":
    deg_calc = TimeDegreeCalculator()
    res = deg_calc.FindDegree()
    print(
        f'There is a {res[0]} degrees from hour to minute arrows and {res[1]} vice versa at {deg_calc.hour}:{"%02d" % deg_calc.minute}'
    )
