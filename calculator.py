from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from re import findall, match, IGNORECASE
from argparse import ArgumentParser


professions = ['net', 'analytics', 'architecture', 'c', 'data', 'devops', 'erp', 'game', 'go', 'html', 'admin', 'java', 'javascript', 'mobile', 'php', 'pm', 'python', 'ruby', 'scala', 'security', 'support', 'testing', 'ux']
experience = ['junior', 'mid', 'senior']
employment = ['b2b', 'permanent', 'mandate_contract']

parser = ArgumentParser()
parser.add_argument('--prof', choices=professions, help='Profession')
parser.add_argument('--exp', choices=experience, help='Experience level')
parser.add_argument('--emp', choices=employment, help='Type of employment')
args = parser.parse_args()

prof = '' if not args.prof else args.prof  # You can set is as permanent value. Use one of values in professions
exp = '' if not args.exp else args.exp  # You can set is as permanent value. Use one of values in experience
emp = '' if not args.emp else args.emp  # You can set is as permanent value. Use one of values in employment


def get_profession():
    global prof
    while prof not in professions:
        user = input("Type key word of your profession: ")
        if user == '!all':
            print(', '.join(professions))

        else:
            guess = [x.title() for x in professions if match(f'.*({user}).*', x, flags=IGNORECASE)]

            if len(guess) == 0:
                print("Nothing found! Please try again or type '!all' to display all available professions")

            elif len(guess) == 1:
                if input(f"Do you mean {guess[0]}? y/n: ") == 'y':
                    prof = guess[0]
                    break

            elif len(guess) > 1:
                print('\n'.join(list(map(lambda x: f'{guess.index(x)+1}: {x}', guess))))
                i = int(input("\nIf You mean one of them, type it ID here, or any other number to try again: "))

                if i in range(1, len(guess)+1):
                    prof = guess[i-1]
                    print(f"\nYour role is: {prof}")
                    break

                else:
                    print("Wrong ID!")


def get_experience():
    global exp
    while exp not in experience:
        print('\n'.join(list(map(lambda x: f'{experience.index(x) + 1}: {x}', experience))).title())
        i = int(input(f"Type one ID or 0 to select all: "))
        if i in range(1, len(experience)+1):
            exp = experience[int(i) - 1]
            print(f"\nSelected experience is: {exp.title()}\n")
            break
        elif i == 0:
            print(f"\nSelected experience is: {', '.join(experience).title()}\n")
            break


def get_employment():
    global emp
    while emp not in employment:
        print('\n'.join(list(map(lambda x: f'{employment.index(x) + 1}: {x}', employment))).title())
        i = int(input(f"Type one ID or 0 to select all: "))
        if i in range(1, len(employment)+1):
            emp = employment[int(i) - 1]
            print(f"\nSelected employment is: {emp.title()}\n")
            break
        elif i == 0:
            print(f"\nSelected employment is: {', '.join(employment).title()}\n")
            break


get_profession()
get_experience()
get_employment()

# Prepare url
url = f"https://justjoin.it/"
url += f'all/{prof}' if prof else ''
url += f'all/all/{exp}' if exp and not prof else (f'/{exp}' if exp else '')
url += f'?employmentType={emp}&tab=with-salary' if emp else '?tab=with-salary'

# Prepare bowser
options = Options()
options.add_argument("--headless")
options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Disable annoying alert 'DevTools listening...'
driver = webdriver.Chrome(service=Service(), options=options)  # Replace Service() to Service('/path/to/chromedriver')
driver.get(url)

# Find salary in page source
offers = findall(r"[0-9]{1,2}.?[0-9]?k - [0-9]{1,2}.?[0-9]?k [A-Z]{3}", driver.page_source)
if len(offers) == 0:
    print(f"Sorry, no offers at the moment. For {exp} {prof} on {emp} employment type")
    exit()

currency = findall(r"[A-Z]{3}", offers[0])[0]
driver.close()

# Get smallest, biggest and average salary
offer_min = []
offer_max = []
offer_avg = []
for o in offers:
    offer = o.replace('k ', '').replace(f'{currency}', '').split('-')
    offer_min.append(float(offer[0])*1000)
    offer_max.append(float(offer[1])*1000)
    offer_avg.append((float(offer[0]) + float(offer[1])) / 2 * 1000)

print(f"Result for {exp} {prof} on {emp} employment type:\n")
print(f"Average salary brackets: {round(sum(offer_min)/len(offer_min))} - {round(sum(offer_max)/len(offer_max))} {currency}")
print(f"Average salary: {round(sum(offer_avg)/len(offer_avg))} {currency}")
print(f"Smallest salary: {round(min(offer_min))} {currency}")
print(f"Biggest salary: {round(max(offer_max))} {currency}")
