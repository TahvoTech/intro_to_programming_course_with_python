# COMP.CS.100 7.13 Lajittele hinnan mukaan
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

korando = {
    "name": "Korando",
    "monthly_fee": 579,
    "insurance_year":1500,
    "km_year": 25000,
    "km_month": 2000,
    "km_week": 500,
    "consumption_per_100km": "18kwh/100km",
    "kwh_or_gas_price": 0.15,
    "maintenance": 300,
    "consuption_eur_in_year": 25000*0.15*30/100,
    "consuption_eur_in_month": round(1125/12),
    "consuption_eur_in_week": round(1125/52),
    "consuption_eur_per_100km": 30 * 0.15,
    "consuption_eur_per_150km": 30 * 0.15 *3/2,
    "total_costs_12m": round((1500 + 1125 + 579 * 12 + 300)/12*12),
    "total_costs_14m": round((1500 + 1125 + 579 * 12 + 300)/12*14),
    "total_costs_16m": round((1500 + 1125 + 579 * 12 + 300)/12*16),
    "total_costs_18m": round((1500 + 1125 + 579 * 12 + 300)/12*18),
    "total_costs_24m": round((1500 + 1125 + 579 * 12 + 300) / 12 * 24),
    "investment": 300,
    "cashflow_after_24m": 20000,
    "sell_car": 0,
    "cost_after_end/sell": 20000,
    "factory_guarantee": "4 year"
}

ibiza = {
    "name": "Ibiza",
    "monthly_fee": 0,
    "insurance_year":700,
    "km_year": 25000,
    "km_month": 2000,
    "km_week": 500,
    "consumption_per_100km": "5l/100km",
    "kwh_or_gas_price": 2,
    "maintenance": 300,
    "consuption_eur_in_year": 25000*2*5/100,
    "consuption_eur_in_month": round(25000*2*5/100/12),
    "consuption_eur_in_week": round(25000*2*5/100/52),
    "consuption_eur_per_100km": 5 * 2,
    "consuption_eur_per_150km": 7.5 * 2,
    "total_costs_12m": round(3500 / 12 * 12),
    "total_costs_14m": round(3500 / 12 * 14),
    "total_costs_16m": round(3500 / 12 * 16),
    "total_costs_18m": round(3500 / 12 * 18),
    "total_costs_24m": round(3500 / 12 * 24),
    "investment": 11000,
    "cashflow_after_24m": 11000+7000,
    "sell_car": 6000,
    "cost_after_end/sell": 12000,
    "factory_guarantee": "0 year"
}

bmw_118 = {
    "name": "BMW 118",
    "monthly_fee": 0,
    "insurance_year":700,
    "km_year": 25000,
    "km_month": 2000,
    "km_week": 500,
    "consumption_per_100km": "5l/100km",
    "kwh_or_gas_price": 2,
    "maintenance": 300,
    "consuption_eur_in_year": 25000*2*5/100,
    "consuption_eur_in_month": round(25000*2*5/100/12),
    "consuption_eur_in_week": round(25000*2*5/100/52),
    "consuption_eur_per_100km": 5 * 2,
    "consuption_eur_per_150km": 7.5 * 2,
    "total_costs_12m": round(3500 / 12 * 12),
    "total_costs_14m": round(3500 / 12 * 14),
    "total_costs_16m": round(3500 / 12 * 16),
    "total_costs_18m": round(3500 / 12 * 18),
    "total_costs_24m": round(3500 / 12 * 24),
    "investment": 15000,
    "cashflow_after_24m": 15000+7000,
    "sell_car": 10000,
    "cost_after_end/sell(24m)": 11000,
    "factory_guarantee": "2 year"
}

bmw_118 = {
    "name": "Focus",
    "monthly_fee": 0,
    "insurance_year":700,
    "km_year": 25000,
    "km_month": 2000,
    "km_week": 500,
    "consumption_per_100km": "5l/100km",
    "kwh_or_gas_price": 2,
    "maintenance": 300,
    "consuption_eur_in_year": 25000*2*5/100,
    "consuption_eur_in_month": round(25000*2*5/100/12),
    "consuption_eur_in_week": round(25000*2*5/100/52),
    "consuption_eur_per_100km": 5 * 2,
    "consuption_eur_per_150km": 7.5 * 2,
    "total_costs_12m": round(3500 / 12 * 12),
    "total_costs_14m": round(3500 / 12 * 14),
    "total_costs_16m": round(3500 / 12 * 16),
    "total_costs_18m": round(3500 / 12 * 18),
    "total_costs_24m": round(3500 / 12 * 24),
    "investment": 15000,
    "cashflow_after_24m": 15000+7000,
    "sell_car": 10000,
    "cost_after_end/sell(24m)": 11000,
    "factory_guarantee": "2 year"
}

def main():

    tiedosto_olio = open("tuloste.txt", mode="w", encoding="utf8")

    print("", file=tiedosto_olio)
    for i,j,k in zip(korando, ibiza, bmw_118):
        print(f"{i:<25}: {(korando[i]):>12} {(ibiza[j]):>12}"
              f" {(bmw_118[k]):>12}", file=tiedosto_olio)
    print("", file=tiedosto_olio)


    tiedosto_olio.close()

    tiedosto_olio = open("tuloste.txt", mode="r", encoding="utf8")


    for i in tiedosto_olio:
        i = i.rstrip()
        print(i)

    tiedosto_olio.close()

if __name__ == "__main__":
    main()