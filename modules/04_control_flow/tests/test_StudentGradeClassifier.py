from solution.StudentGradeClassifier import classify_grade
import pytest



def test_invalid_score_raises_error():
    with pytest.raises(ValueError, match="Score must be between 0 and 100."):
        classify_grade(120)

def test_grade_zero():
    result = classify_grade(0)
    assert result == "F"

def test_grade_a():
    result = classify_grade(95)
    assert result == "A"

