import pandas as pd

data = pd.read_csv("Datasheet.csv")
color = data["Primary Fur Color"].tolist()


black = len(data[data["Primary Fur Color"] == "Black"])
gray = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])


color_dic = {
    "Fur color": ["gray", "cinnamon", "black"],
    "Color": [gray, cinnamon, black]
}

dat = pd.DataFrame(color_dic)
print(dat)
dat.to_csv("new_data.csv")
