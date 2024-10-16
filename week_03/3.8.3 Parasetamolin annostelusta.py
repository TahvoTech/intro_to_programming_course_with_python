# COMP.CS.100 3.8.3 Parasetamolin annostelusta
# Tekijä: Jarmo Tahvanainen
# Opiskelijanumero: 151737413

"""

Program calculates the amount of Parasetamol to give to the patient.

Examples:

Patient's weight (kg): 50
How much time has passed from the previous dose (full hours): 6
The total dose for the last 24 hours (mg): 750
The amount of Parasetamol to give to the patient: 750

Patient's weight (kg): 80
How much time has passed from the previous dose (full hours): 7
The total dose for the last 24 hours (mg): 3600
The amount of Parasetamol to give to the patient: 400

Patient's weight (kg): 67
How much time has passed from the previous dose (full hours): 4
The total dose for the last 24 hours (mg): 1000
The amount of Parasetamol to give to the patient: 0

"""

def calculate_dose(patient_weight, last_dose_time, doses_last_24h):
    """calculates correct dose.

    :param patient_weight: int, patient's weight.
    :param last_dose_time: int, last dose time.
    :param doses_last_24h: int, how much doses has been taken within the last 24h.
    :return: returns either 0 or the dose (max dose - doses taken last 24h).
    """
    max_dose = 4000
    max_dose_6 = patient_weight * 15
    max_dose_24 = max_dose_6 * 4
    if last_dose_time < 6:
        result = 0
    elif doses_last_24h > max_dose:
        result = 0
    elif doses_last_24h == 0:
        result = max_dose_6
    else:
        result = max_dose_6
    if result + doses_last_24h > 4000:
        result = max_dose - doses_last_24h
    return result

def main():
    patient_weight = int(input("Patient's weight (kg): "))
    last_dose_time = int(input("How much time has passed from the previous dose (full hours): "))
    doses_last_24h = int(input("The total dose for the last 24 hours (mg): "))

    print(f"The amount of Parasetamol to give to the patient: {calculate_dose(patient_weight, last_dose_time, doses_last_24h)}")

    # calculate_dose assumes parameters to be of type int
    # and they should be passed in the order: weight, time, total_doze_24
    # (or more like the automated tests assume this)

if __name__ == "__main__":
  main()