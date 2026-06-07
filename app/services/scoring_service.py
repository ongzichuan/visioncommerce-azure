def calculate_quality_score(tags):

    score = 50

    if len(tags) >= 5:
        score += 20

    if "product" in tags:
        score += 15

    if "indoor" in tags:
        score += 10

    if score > 100:
        score = 100

    return score