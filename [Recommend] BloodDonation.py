""" BloodDonation """
def main():
    """ . """
    age = int(input())
    weight = int(input())
    consent = "False"
    times = int(input())
    if age == 17 or 60 <= age <= 70:
        consent = input()
    if not times and age > 55:
        print('No')
    elif (age == 17 or 60 <= age <= 70) and times and weight >= 45 and consent == "True":
        print("Yes")
    elif 18 <= age <= 59 and weight >= 45:
        print("Yes")
    else:
        print("No")
main()
