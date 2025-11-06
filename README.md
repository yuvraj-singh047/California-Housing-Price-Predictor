# 🏠 California Housing Price Predictor

This project predicts house prices using the **California Housing Dataset** from Scikit-Learn.  
A **Machine Learning Regression Model** was trained and saved as a `.pkl` file, and the user can input house-related features to get a predicted price.

---

## 📦 Features Used
| Feature Name | Description |
|-------------|-------------|
| MedInc      | Median Income of block group |
| HouseAge    | Median House Age |
| AveRooms    | Average Number of Rooms per house |
| AveBedrms   | Average Number of Bedrooms per house |
| Population  | Total population of block group |
| AveOccup    | Average household occupancy |
| Latitude    | Geographical Latitude |
| Longitude   | Geographical Longitude |

---

## 🧠 Model Used
- `HistGradientBoostingRegressor` (from Scikit-Learn)
- Trained on the California Housing dataset
- Saved using `pickle`

---

## ▶️ Running the Program

### 1. Install dependencies
pip install -r requirements.txt

shell
Copy code

### 2. Run the Prediction App
python app/Predict_House_Price.py

yaml
Copy code

---

## 🧮 Example Input
Enter Your Median Income: 4.5
Enter Age of House: 20
Enter Avg No. of Rooms: 5
Enter Avg Bedrooms: 1
Enter total population: 800
Enter Avg Occupancy: 3
Enter Latitude: 34.5
Enter Longitude: -118.2

yaml
Copy code

---

## ✅ Output Example
🏠 Predicted House Price: 3.54

yaml
Copy code

---

## 📌 Future Improvements
- Convert to Streamlit Web App UI ✅
- Deploy to Cloud (Render / Hugging Face / Vercel)

---

## 🧑‍💻 Author
**Yuvraj Singh**  
B.Tech CSE (2nd Year), AIML + DSA Learner  