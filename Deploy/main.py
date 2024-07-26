# Library API
from flask import Flask, request, jsonify
import os

# Library Dataset 
import pandas as pd

# Library Data Preprocessing
import numpy as  np

# Library Model
import tensorflow as tf
from tensorflow import keras
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import euclidean_distances
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.optimizers import Adam

app = Flask(__name__)

# Load the models
model = tf.keras.models.load_model('./model/model.h5')
model_2 = tf.keras.models.load_model('./model/model_2.h5')

# Load the dataset
dataset = pd.read_csv('./dataset/recipesprepross.csv')

# Recommendation system based on nutritional values
# Select relevant columns for nutritional values
nutritional_columns = ['Calories', 'FatContent', 'SaturatedFatContent', 'CholesterolContent',
                       'SodiumContent', 'CarbohydrateContent', 'FiberContent', 'SugarContent', 'ProteinContent']

recipe_data = dataset[nutritional_columns]

# Preprocess the dataset
recipe_data = recipe_data.fillna(0)  # Replace missing values with 0 or appropriate values
scaler = MinMaxScaler()
recipe_data_scaled = scaler.fit_transform(recipe_data)  # Scale the features to [0, 1]

# Split the dataset into training and validation sets
train_data, val_data = train_test_split(recipe_data_scaled, test_size=0.3, random_state=42)

input_dim = recipe_data_scaled.shape[1]  # Number of features

# Recommendation system based on Calorie
# Preprocess the data
calories = dataset['Calories'].values.reshape(-1, 1)
mean_calories = np.mean(calories)
std_calories = np.std(calories)
normalized_calories = (calories - mean_calories) / std_calories

# Create the TensorFlow model
input_dim_2 = normalized_calories.shape[1]  # Number of features

@app.route('/recnut', methods=['POST'])
def recnut():
    calories = request.json['Calories']
    fat = request.json['FatContent']
    saturated_fat = request.json['SaturatedFatContent']
    cholesterol = request.json['CholesterolContent']
    sodium = request.json['SodiumContent']
    carbohydrate = request.json['CarbohydrateContent']
    fiber = request.json['FiberContent']
    sugar = request.json['SugarContent']
    protein = request.json['ProteinContent']
    float_features = [calories, fat, saturated_fat, cholesterol, sodium, carbohydrate, fiber, sugar, protein]
    final_features = [float_features]
    prediction = model.predict(final_features)

    # Scale the input recipe using the same scaler
    input_recipe_scaled = scaler.transform(prediction)

    # Calculate similarity scores
    similarity_scores = cosine_similarity(input_recipe_scaled, recipe_data_scaled)

    # Get recommended recipe indices
    top_indices = np.argsort(similarity_scores, axis=1)[0][::-1][:10]  # Get top 10 indices

    # Filter out irrelevant columns
    relevant_columns = ['Name', 'Images', 'CookTime', 'PrepTime', 'TotalTime', 'RecipeIngredientParts',
                        'Calories', 'FatContent', 'SaturatedFatContent', 'CholesterolContent',
                        'SodiumContent', 'CarbohydrateContent', 'FiberContent',
                        'SugarContent', 'ProteinContent', 'RecipeServings', 'RecipeInstructions']
    recommendations = dataset.iloc[top_indices][relevant_columns]

    recjs = recommendations.to_dict('records')

    return {"message": "Predict success deck!", "status": 200, "data": recjs}

@app.route('/recol', methods=['POST'])
def recol():
    calories = request.json['Calories']
    prediction = model_2.predict([calories])

    # Calculate the Euclidean distances between input calories and all recipes
    distances = euclidean_distances(dataset[['Calories']], prediction)

    # Add distances as a new column in the dataset
    dataset['Distance'] = distances

    # Sort recipes based on the distances in ascending order
    sorted_recipes = dataset.sort_values('Distance')

    # Select top k recipes
    top_recipes = sorted_recipes.head(15)

    # Test the recommendation system
    # recommended_recipes = top_recipes(prediction, top_k=5)

    trjs = top_recipes.to_dict('records')

    return {"message": "Predict success deck!", "status": 200, "data": trjs}

@app.route('/getrecipe', methods=['GET'])
def getrecipe():
    getrecipe = dataset.sample(10)
    grjs = getrecipe.to_dict('records')

    return {"message": "Get success deck!", "status": 200, "data": grjs}

@app.route('/search', methods=['POST'])
def search():
    search = request.json['Name']
    search = dataset[dataset['Name'].str.contains(search)]
    srjs = search.to_dict('records')

    return {"message": "Search success deck!", "status": 200, "data": srjs}

@app.route('/')
def index():
    return jsonify({"message": "WELCOME TO RECIPE API"})

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True, port=os.getenv("PORT", default=5000))