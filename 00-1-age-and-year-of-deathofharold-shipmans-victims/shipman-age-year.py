import pandas as pd
import matplotlib.pyplot as plt

shipman = pd.read_csv('00-1-shipman-confirmed-victims-x.csv')

plt.style.use( 'ggplot')
fig, ax = plt.subplots()
women_year = shipman[shipman.gender == 0].fractionalDeathYear
women_age = shipman[shipman.gender == 0].Age
men_year = shipman[shipman.gender == 1].fractionalDeathYear
men_age = shipman[shipman.gender == 1].Age
ax.scatter(women_year, women_age, label='Women')
ax.scatter(men_year, men_age, label='Men')
ax.set_title("Shipman's 215 victims")
ax.set_xlabel('Year')
ax.set_ylabel('Age of victim')
ax.legend()
plt.show()


year = shipman.yearOfDeath
age = shipman.Age
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
ax1.hist(year, bins=25)
ax2.hist(age, bins=10)
ax1.set_title('Victims by year')
ax1.set_xlabel('Year')
ax2.set_title('Victims by age')
ax2.set_xlabel('Age')
plt.show()
