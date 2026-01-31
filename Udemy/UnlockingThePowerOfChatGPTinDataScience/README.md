Udemy Course:
https://www.udemy.com/course/unlocking-the-power-of-chatgpt-in-data-science-a-z-guide/learn/lecture/35886520?start=0#overview

# Data Exploration prompts:
- Use this dataset to generate summary statistics, visualizations and insights. Utilice este conjunto de datos para generar estadísticas de resumen, visualizaciones y conocimientos.

Estadísticas de Resumen
Aquí tienes un resumen estadístico general del dataset de viviendas (500 registros). Utilicé pandas para calcular estas métricas:

Métrica Número de dormitorios Número de baños Metros cuadrados Precio de venta ($)
Conteo  500 500 500 500
Media   3.54    3.03    2304.30 2,339,950.00
Desviación estándar 1.20    1.47    1065.66 2,432,224.00
Mínimo  2   1   800 375,000
25% 3   2   1550    1,050,000
Mediana(50%)    3   3   2125    1,525,000
75% 4   4   2650    2,431,250
Máximo  8   8   6650    17,625,000

Agrupación por Ubicación
Promedios y medianas por ubicación (solo las primeras 10 para brevidad; hay 38 únicas en total):

Ubicación   Precio medio($$)    Precio mediana($$)  Conteo  Metros cuadrados medio  Metros cuadrados mediana
Bel Air 10,670,833  10,450,000  6   4325    4525
Malibu  9,775,000   10,100,000  5   3860    4150
Beverly Hills   7,652,273   6,275,000   11  3627    3400
Brentwood   6,947,917   6,362,500   12  4179    4550
Pacific Palisades   6,266,667   6,637,500   12  4346    4550
Hollywood Hills 5,809,615   6,300,000   13  3758    3550    
Manhattan Beach 3,947,917   4,550,000   12  3183    3475    
La Jolla    3,712,500   3,287,500   10  2905    2900
Santa Monica    3,625,000   3,400,000   15  2847    2550    
Laguna Beach    3,464,583   3,200,000   12  3108    3500

Matriz de Correlación
Correlaciones entre variables numéricas (valores cercanos a 1 indican fuerte relación positiva):

Variable    Dormitorios Baños   Metros cuadrados    Precio de venta 
Dormitorios 1.00    0.40    0.39    0.47
Baños   0.40    1.00    0.61    0.57
Metros cuadrados    0.39    0.61    1.00    0.83    
Precio de venta 0.47    0.57    0.83    1.00

Visualizaciones (Text-based)
Dado que no puedo generar imágenes interactivas aquí, aquí va una representación textual simple de un gráfico de barras para las 5 ubicaciones más caras (basado en precio medio). La longitud de las barras es proporcional al precio máximo en esta selección:

Bel Air: $10,670,833 ##################################################
Malibu: $9,775,000 #############################################
Beverly Hills: $7,652,273 ###################################
Brentwood: $6,947,917 ################################
Pacific Palisades: $6,266,667 #############################

(En un entorno con gráficos, esto sería un histograma de precios o un scatter plot de metros cuadrados vs. precio.)
Conocimientos Principales

Precio promedio general: Las viviendas tienen un precio medio de aproximadamente $2.34 millones, con una gran variabilidad (desde $375,000 hasta $17.6 millones), lo que indica un mercado de lujo en áreas como Bel Air y Malibu.
Ubicaciones más caras: Áreas premium como Bel Air (promedio >$10M) y Malibu dominan, probablemente debido a su exclusividad en California. En contraste, lugares como Dana Point o Costa Mesa son más asequibles (alrededor de $1M en promedio).
Relación clave: Hay una fuerte correlación (0.83) entre metros cuadrados y precio de venta, sugiriendo que el tamaño es un factor principal en el valor. Los baños y dormitorios también influyen, pero menos (0.57 y 0.47 respectivamente).
Distribución: La mayoría de las casas tienen 3 dormitorios y 3 baños (mediana), con un tamaño medio de ~2125 m². Hay outliers en propiedades grandes y caras, posiblemente mansiones en Hollywood Hills o Brentwood.
Oportunidades: Si buscas valor, mira Irvine o San Diego (precios ~$1.2-1.3M con tamaños decentes). Para inversión de lujo, enfócate en correlaciones altas: más espacio = mayor precio.

- How to generate a bar chart showing the distribution of sales price by number of bedrooms. Cómo generar un gráfico de barras que muestre la distribución del precio de venta por número de habitaciones

Response: See the dataExploration.py file

- What factors seems to be the most significant predictors of housing prices in this dataset? ¿Qué factores parecen ser los predictores más significativos de los precios de la vivienda en este conjunto de datos?

# Data Modeling

The Iris dataset is a small, clean, labeled dataset of flower measurements used primarily to demonstrate and teach classification techniques in machine learning and statistics.

What is the Iris dataset?

The Iris dataset is one of the most famous and widely used datasets in statistics, machine learning, and data science. It was introduced in 1936 by Ronald A. Fisher in his paper “The use of multiple measurements in taxonomic problems.”

Its original purpose was biological classification (taxonomy), but today it is mainly used for:
- Teaching supervised learning
- Demonstrating classification algorithms
- Practicing exploratory data analysis (EDA)

Example of Iris dataset rows:

| Sepal Length | Sepal Width | Petal Length | Petal Width | Species    |
| ------------ | ----------- | ------------ | ----------- | ---------- |
| 5.1          | 3.5         | 1.4          | 0.2         | Setosa     |
| 4.9          | 3.0         | 1.4          | 0.2         | Setosa     |
| 6.4          | 3.2         | 4.5          | 1.5         | Versicolor |
| 6.9          | 3.1         | 5.4          | 2.1         | Virginica  |

- Give a sample of Iris dataset in a tabular format

| SepalLength (cm) | SepalWidth (cm) | PetalLength (cm) | PetalWidth (cm) | Species    |
| ---------------- | --------------- | ---------------- | --------------- | ---------- |
| 5.1              | 3.5             | 1.4              | 0.2             | setosa     |
| 4.9              | 3.0             | 1.4              | 0.2             | setosa     |
| 4.7              | 3.2             | 1.3              | 0.2             | setosa     |
| 5.0              | 3.6             | 1.4              | 0.2             | setosa     |
| 6.4              | 3.2             | 4.5              | 1.5             | versicolor |
| 6.9              | 3.1             | 4.9              | 1.5             | versicolor |
| 6.5              | 2.8             | 4.6              | 1.5             | versicolor |
| 5.5              | 2.4             | 3.8              | 1.1             | versicolor |
| 6.5              | 3.0             | 5.5              | 1.8             | virginica  |
| 7.6              | 3.0             | 6.6              | 2.1             | virginica  |

- Provide suggestions of types of models that may be appropriate for this dataset

The Iris dataset is a small, clean, labeled, tabular dataset with numeric features and a 3-class target, so a wide range of supervised classification models are appropriate. Below are well-justified model choices, grouped by purpose and complexity.

1. Baseline & Interpretable Models

These are often the first models you should try.

Logistic Regression (Multinomial)

✔ Simple, fast, strong baseline

✔ Interpretable coefficients

✔ Works well because classes are fairly separable

⚠ Assumes linear decision boundaries

Why suitable: Iris is low-dimensional and near-linearly separable (especially setosa).

Linear Discriminant Analysis (LDA)

✔ Designed for class separation

✔ Performs dimensionality reduction + classification

✔ Very strong on Iris

Why suitable: Fisher originally used LDA concepts on this dataset.

2. Distance-Based Models
k-Nearest Neighbors (kNN)

✔ Very intuitive

✔ Non-parametric

✔ Performs well on small datasets

⚠ Sensitive to feature scaling

⚠ Slower for large datasets (not an issue here)

Why suitable: Iris has only 150 samples and 4 features.

3. Tree-Based Models
Decision Tree

✔ Highly interpretable

✔ Captures non-linear relationships

✔ No feature scaling needed

⚠ Can overfit if not constrained

Why suitable: Petal features split classes very cleanly.

Random Forest

✔ High accuracy

✔ Reduces overfitting

✔ Handles feature interactions well

⚠ Less interpretable than a single tree

Why suitable: Excellent demonstration of ensemble learning.

4. Margin-Based Models
Support Vector Machine (SVM)

✔ Very high accuracy on Iris

✔ Kernel trick allows non-linear boundaries

✔ Robust in low-dimensional spaces

⚠ Requires tuning (C, kernel, gamma)

Why suitable: Iris is a textbook SVM dataset.

5. Probabilistic Models
Naive Bayes (Gaussian)

✔ Fast

✔ Simple probabilistic interpretation

✔ Surprisingly effective

⚠ Assumes feature independence (not strictly true)

Why suitable: Iris features are approximately Gaussian per class.

6. Neural Networks (Educational, Not Necessary)
Multilayer Perceptron (MLP)

✔ Demonstrates neural networks

✔ Can achieve near-perfect accuracy

⚠ Overkill for this dataset

⚠ Less interpretable

Why suitable: Mainly for teaching NN concepts, not efficiency.

7. Unsupervised (Exploratory, Optional)
k-Means Clustering

✔ Useful for comparison with true labels

✔ Good for visualization and EDA

⚠ Not a classifier by itself

Why suitable: Natural clustering structure in petal features.

Recommended Model Progression (Best Practice)

Logistic Regression / LDA (baseline)

kNN or Decision Tree

SVM

Random Forest

MLP (optional, educational)

| Model               | Interpretability | Accuracy    | Complexity |
| ------------------- | ---------------- | ----------- | ---------- |
| Logistic Regression | High             | High        | Low        |
| LDA                 | High             | High        | Low        |
| kNN                 | Medium           | High        | Low        |
| Decision Tree       | Very High        | High        | Medium     |
| Random Forest       | Medium           | Very High   | Medium     |
| SVM                 | Medium           | Very High   | Medium     |
| Naive Bayes         | High             | Medium-High | Low        |
| MLP                 | Low              | Very High   | High       |

Below is a clean, end-to-end Python example of a Logistic Regression model using the Iris dataset with scikit-learn.
This follows standard ML best practices: train/test split, feature scaling, training, and evaluation.
