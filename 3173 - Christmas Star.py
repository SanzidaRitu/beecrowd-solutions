from datetime import date, timedelta

JUPITER_YEARS = 11.9
SATURN_YEARS = 29.6
DAYS_PER_YEAR = 365.25

N = int(input())

days_jupiter = int(JUPITER_YEARS * DAYS_PER_YEAR * N)
days_saturn = int(SATURN_YEARS * DAYS_PER_YEAR * N)

start = date(2020, 12, 21)

end_jupiter = start + timedelta(days=days_jupiter)
end_saturn = start + timedelta(days=days_saturn)

print(f"Dias terrestres para Jupiter = {days_jupiter}")
print(f"Data terrestre para Jupiter: {end_jupiter:%Y-%m-%d}")
print(f"Dias terrestres para Saturno = {days_saturn}")
print(f"Data terrestre para Saturno: {end_saturn:%Y-%m-%d}")