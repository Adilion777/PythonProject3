# ──────────────────────────────────────────────
# Base Class
# ──────────────────────────────────────────────

class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        print("Not implemented — use a child class")

    def print_results(self):
        for key, value in self.result.items():
            print(f"{key}: {value}")

    def __str__(self):
        return f"DataAnalyser: base class, {len(self.students)} students"


# ──────────────────────────────────────────────
# Variant C Child Class
# ──────────────────────────────────────────────

class SleepAnalyser(DataAnalyser):
    """Variant C — analyses GPA difference between low-sleep and high-sleep students."""

    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        low = [s for s in self.students if float(s['sleep_hours']) < 6]
        high = [s for s in self.students if float(s['sleep_hours']) >= 6]

        avg_gpa_low = (
            round(sum(float(s['GPA']) for s in low) / len(low), 2) if low else 0.0
        )
        avg_gpa_high = (
            round(sum(float(s['GPA']) for s in high) / len(high), 2) if high else 0.0
        )

        self.result = {
            'total_students': len(self.students),
            'low_sleep': len(low),
            'high_sleep': len(high),
            'avg_gpa_low_sleep': avg_gpa_low,
            'avg_gpa_high_sleep': avg_gpa_high,
            'gpa_difference': round(avg_gpa_high - avg_gpa_low, 2),
        }

    def print_results(self):
        print("=" * 30)
        print("SLEEP ANALYSIS REPORT")
        print("=" * 30)
        super().print_results()
        print("=" * 30)

    def __str__(self):
        return f"SleepAnalyser: Sleep Analysis, {len(self.students)} students"


# ──────────────────────────────────────────────
# Extra class for polymorphism demo (Variant A)
# ──────────────────────────────────────────────

class GpaAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        gpas = [float(s['GPA']) for s in self.students]
        self.result = {
            'total_students': len(self.students),
            'average_gpa': round(sum(gpas) / len(gpas), 2),
            'max_gpa': max(gpas),
            'min_gpa': min(gpas),
            'high_performers': sum(1 for g in gpas if g > 3.5),
        }

    def print_results(self):
        print("=" * 30)
        print("GPA ANALYSIS REPORT")
        print("=" * 30)
        super().print_results()
        print("=" * 30)

    def __str__(self):
        return f"GpaAnalyser: GPA Statistics, {len(self.students)} students"