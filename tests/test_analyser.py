# Test results:
# test_analyse_twice (tests.test_analyser.TestAnalyser.test_analyse_twice)
# Calling analyse() twice must produce identical results. ... ok
# test_result_has_required_keys (tests.test_analyser.TestAnalyser.test_result_has_required_keys)
# Result must contain all Variant C required keys. ... ok
# test_result_is_not_empty (tests.test_analyser.TestAnalyser.test_result_is_not_empty)
# After analyse(), result must not be an empty dictionary. ... ok
# test_total_students (tests.test_analyser.TestAnalyser.test_total_students)
# result['total_students'] must equal the sample size (5). ... ok
#
# ----------------------------------------------------------------------
# Ran 4 tests in 0.001s
#
# OK

import unittest
from analytics.analyser import SleepAnalyser


class TestAnalyser(unittest.TestCase):

    def setUp(self):
        """Runs before every test — hardcoded 5-row sample, no CSV needed."""
        self.sample = [
            {"GPA": "3.8", "sleep_hours": "7", "country": "USA",
             "final_exam_score": "95", "study_hours_per_day": "4"},
            {"GPA": "2.5", "sleep_hours": "5", "country": "India",
             "final_exam_score": "72", "study_hours_per_day": "2"},
            {"GPA": "3.9", "sleep_hours": "8", "country": "USA",
             "final_exam_score": "98", "study_hours_per_day": "5"},
            {"GPA": "1.8", "sleep_hours": "4", "country": "Canada",
             "final_exam_score": "55", "study_hours_per_day": "1"},
            {"GPA": "3.5", "sleep_hours": "6", "country": "India",
             "final_exam_score": "88", "study_hours_per_day": "3"},
        ]

    def test_result_is_not_empty(self):
        """After analyse(), result must not be an empty dictionary."""
        analyser = SleepAnalyser(self.sample)
        analyser.analyse()
        self.assertNotEqual(analyser.result, {})

    def test_total_students(self):
        """result['total_students'] must equal the sample size (5)."""
        analyser = SleepAnalyser(self.sample)
        analyser.analyse()
        self.assertEqual(analyser.result['total_students'], 5)

    def test_result_has_required_keys(self):
        """Result must contain all Variant C required keys."""
        analyser = SleepAnalyser(self.sample)
        analyser.analyse()
        self.assertIn('low_sleep', analyser.result)
        self.assertIn('high_sleep', analyser.result)
        self.assertIn('gpa_difference', analyser.result)

    def test_analyse_twice(self):
        """Calling analyse() twice must produce identical results."""
        analyser = SleepAnalyser(self.sample)
        analyser.analyse()
        result1 = analyser.result.copy()
        analyser.analyse()
        self.assertEqual(analyser.result, result1)


if __name__ == '__main__':
    unittest.main()