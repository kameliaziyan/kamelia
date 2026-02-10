def classify_grade(score: int) -> str :

    if score < 0 or score > 100 :
        raise ValueError("Score must be between 0 and 100.")
    if score >= 90 and score <=100 :
        print("A")
        return "A"
    
    if score >= 80 and score <=89 :
        print("B")
        return "B"
    
    if score >= 70 and score <=79 :
        print("C")
        return "C"
    
    if score >= 60 and score <=69 :
        print("D")
        return "D"
    
    if score >= 0 and score <=59 :
        print("F")
        return "F"
    
    return

classify_grade(95)  # Returns "A"
classify_grade(85)  # Returns "B"
classify_grade(55)  # Returns "F"

###### Write at least 3 unit tests covering different grade ranges and validation cases.
