import pandas


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color = data["Primary Fur Color"]
table = color.value_counts()
ans = table.to_dict()
print(ans)
grey = ans["Gray"]
red = ans["Cinnamon"]
black = ans["Black"]
answe = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey, red, black]
}
anser = pandas.DataFrame(answe)
anser.to_csv("squirrel_count.csv")