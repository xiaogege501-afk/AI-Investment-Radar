def calculate_score(price_change):

    score = 50


    # 趋势评分

    if price_change > 3:

        score += 20

    elif price_change > 0:

        score += 10

    else:

        score -= 10



    # 风险调整

    if price_change > 10:

        score -= 15



    # 限制范围

    if score > 100:

        score = 100


    if score < 0:

        score = 0


    return score



def analyze_market(price_change):


    score = calculate_score(price_change)


    if score >=80:

        status="Strong"


    elif score >=60:

        status="Neutral"


    else:

        status="Weak"



    reasons=[]


    if price_change>0:

        reasons.append(
            "Positive momentum"
        )

    else:

        reasons.append(
            "Weak short term trend"
        )


    if price_change>5:

        reasons.append(
            "High market attention"
        )


    return {

        "score":score,

        "status":status,

        "reasons":reasons

    }
