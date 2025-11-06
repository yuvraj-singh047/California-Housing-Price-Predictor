import pickle
import pandas as pd

with open("california_housing_model_V1.pkl","rb") as file:
    model=pickle.load(file)

MedInc=float(input("Enter Your Median Income:"))
HouseAge=float(input("Enter Age of House:"))
AveRooms=float(input("Enter Avg No. of Rooms:"))
AveBedrms=float(input("Enter Avg Bedrooms:"))
Population=float(input("Enter total Population:"))
AveOccup=float(input("Enter Avg Occupancy:"))
Latitude=float(input("Enter the Latitude:"))
Longitude=float(input("Enter the Longitude:"))

features = pd.DataFrame([[MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude]], 
                        columns=["MedInc", "HouseAge", "AveRooms", "AveBedrms", "Population", "AveOccup", "Latitude", "Longitude"])
prediction=model.predict(features)
print(f"Predicted Price:{prediction}")