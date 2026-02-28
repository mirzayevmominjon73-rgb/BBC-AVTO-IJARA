def calculate_installment(price, down_payment, years, interest):
    remaining = price - down_payment
    total = remaining + (remaining * interest / 100 * years)
    monthly = total / (years * 12)

    return {
        "remaining": round(remaining, 2),
        "total_payment": round(total, 2),
        "monthly_payment": round(monthly, 2),
    }

