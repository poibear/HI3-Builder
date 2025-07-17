<div style="text-align: center;">
    <img src="./static/images/logo%20white%20background.png" alt="HI3 Builder Logo" width=50% height=50%>
    <br>
    <br>
    <h1>Honkai Impact 3rd Builder</h1>
</div>

The Honkai Impact 3rd Builder (HI3 Builder) provides optimized build setups for characters in Honkai Impact 3rd with the power of PyTorch. Curated from trusted builds made by [Marisa Honkai](https://www.hoyolab.com/accountCenter/postList?id=1021101), HI3 Builder offers synergistic builds for newly released characters based on tested data of existing high-performing equipment setups.

> [!WARNING]
> This project is a work-in-progress and development is not stable. Files will be updated at any point and can break unexpectedly. Contributors are free to fork the repository and add changes to merge into this repository.

# Installation
1. Clone this repository
   ```bash
   git clone https://github.com/poibear/HI3-Builder
   ```
2. Open the repository and install the required libraries
   ```bash
   pip install -r requirements.txt
   ```
    > [!TIP]
    > It is recommended to create a virtual environment for the project (especially for PyTorch) when installing libraries
3. Run `app.py` and navigate to [127.0.0.1:8080](127.0.0.1:8080)

# How It Works
On the front-end, HI3 Builder uses Flask to serve static pages and integrate model predictions to the user. The backend consists of a pretrained BERT model, responsible for reading skill descriptions, battlesuit information (e.g., Psychic, Lightning), and ideal stigmata and weapon configuration. This BERT model is connected with a Dense layer that filters learning proceses to the ideal weapon and stigmata of a user-desired battlesuit. The following is a short summary of how the program is broken down:

- Dataset of existing battlesuits, their skill descriptions and battlesuit information, and ideal weapon and stigmata
- (Supervised) BERT model parsing entire dataset to learn and train itself on ideal weapon/stigmata configuration for battlesuits
  - Dense PyTorch output layer of 3 neurons to categorize weapon and stigmata predictions
- Flask to port Python code (including model predictions) to webpage for user-friendly interaction

# Attribution
- [Marisa Honkai](https://www.hoyolab.com/accountCenter/postList?id=1021101) for the optimal builds compiled in the dataset