def analytics_query(question, df):

    question = question.lower()

    if "highest revenue" in question:

        company = df.loc[
            df["revenue"].idxmax()
        ]

        return (
            f"{company['org_name']} "
            f"has highest revenue "
            f"of {company['revenue']} crore"
        )

    if "average revenue" in question:

        avg = df["revenue"].mean()

        return (
            f"Average revenue "
            f"is {avg:.2f} crore"
        )

    return None