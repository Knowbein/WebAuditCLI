RISK_MATRIX = {
    "Content-Security-Policy": {
        "likelihood": 3,
        "impact": 3
    },

    "Strict-Transport-Security": {
        "likelihood": 2,
        "impact": 2
    },

    "X-Frame-Options": {
        "likelihood": 2,
        "impact": 2
    }
}


def calculate_risk(finding):

    for key in RISK_MATRIX:

        if key in finding:

            likelihood = RISK_MATRIX[key]["likelihood"]
            impact = RISK_MATRIX[key]["impact"]

            score = likelihood * impact

            return {
                "likelihood": likelihood,
                "impact": impact,
                "score": score
            }

    return {
        "likelihood": 1,
        "impact": 1,
        "score": 1
    }