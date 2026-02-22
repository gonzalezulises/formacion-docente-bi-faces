# Bibliografía - Módulo 03: Modelado Predictivo e Interpretabilidad

Esta sección recopila referencias para regresión, clasificación, árboles de decisión, clustering, series de tiempo, interpretabilidad de modelos (SHAP) y aplicaciones en contextos educativos.

## Libros de Referencia Fundamental

### Aprendizaje Automático Introductorio
- **An Introduction to Statistical Learning** (2da ed., 2023)
  - Autores: James, G., Witten, D., Hastie, T., Tibshirani, R.
  - Referencia académica con enfoque práctico
  - [ISLR Online - Acceso libre](https://www.statlearning.com/)
  - Cubre: regresión, clasificación, validación, selección de modelos
  - Incluye labs en R y Python

### Aprendizaje Automático Práctico
- **Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow** (3ra ed., 2022)
  - Autor: Aurélien Géron
  - Enfoque pragmático y orientado a implementación
  - Cubre: supervisado, no supervisado, redes neuronales
  - Código disponible en GitHub

### Interpretabilidad de Modelos
- **Interpretable Machine Learning: A Guide for Making Black Box Models Explainable** (2023)
  - Autor: Christoph Molnar
  - [Acceso libre en línea](https://christophm.github.io/interpretable-ml-book/)
  - SHAP, LIME, feature importance
  - Ética en modelos de IA
  - Aplicaciones educativas

## Técnicas de Regresión y Clasificación

### Documentación Scikit-learn
- **Scikit-learn Official Documentation**
  - [https://scikit-learn.org/stable/](https://scikit-learn.org/stable/)
  - Guía de usuario: regresión lineal, logística, SVM, ensemble methods
  - API Reference con ejemplos
  - Galería de ejemplos clasificados por tema

### Regresión
- **Scikit-learn: Linear Regression**
  - [https://scikit-learn.org/stable/modules/linear_model.html](https://scikit-learn.org/stable/modules/linear_model.html)
  - Regresión lineal, Ridge, Lasso, ElasticNet

- **Scikit-learn: Regularización**
  - Validación cruzada, selección de hiperparámetros

### Clasificación
- **Scikit-learn: Classification**
  - [https://scikit-learn.org/stable/modules/classification.html](https://scikit-learn.org/stable/modules/classification.html)
  - Logística, SVM, Naive Bayes, KNN

- **Métricas de Evaluación**
  - Precisión, recall, F1, matriz de confusión, curva ROC, AUC

## Árboles de Decisión y Modelos Ensemble

### Documentación
- **Scikit-learn: Decision Trees**
  - [https://scikit-learn.org/stable/modules/tree.html](https://scikit-learn.org/stable/modules/tree.html)

- **Scikit-learn: Ensemble Methods**
  - [https://scikit-learn.org/stable/modules/ensemble.html](https://scikit-learn.org/stable/modules/ensemble.html)
  - Random Forest, Gradient Boosting, XGBoost
  - Ventajas: feature importance, robustez

- **XGBoost Documentation**
  - [https://xgboost.readthedocs.io/](https://xgboost.readthedocs.io/)
  - Boosting gradient para problemas complejos
  - Competitive en competencias Kaggle

## Clustering y Aprendizaje No Supervisado

### Documentación Scikit-learn
- **Scikit-learn: Clustering**
  - [https://scikit-learn.org/stable/modules/clustering.html](https://scikit-learn.org/stable/modules/clustering.html)
  - K-means, DBSCAN, Jerárquico, Gaussian Mixture Models
  - Selección de número de clusters: elbow method, silhouette

- **PCA y Reducción de Dimensionalidad**
  - [https://scikit-learn.org/stable/modules/decomposition.html](https://scikit-learn.org/stable/modules/decomposition.html)
  - Principal Component Analysis, t-SNE, UMAP

## Series de Tiempo y Pronósticos

### Libro de Referencia
- **Forecasting: Principles and Practice** (3ra ed., 2021)
  - Autores: Rob J. Hyndman & George Athanasopoulos
  - [Acceso libre en línea](https://otexts.com/fpp3/)
  - Métodos: exponencial suavizado, ARIMA, modelos dinámicos
  - Énfasis en aplicaciones prácticas

### Librerías Python
- **Statsmodels Documentation**
  - [https://www.statsmodels.org/](https://www.statsmodels.org/)
  - ARIMA, SARIMA, exponential smoothing
  - Pruebas estadísticas, análisis de tendencias

- **Prophet (Facebook)**
  - [https://facebook.github.io/prophet/](https://facebook.github.io/prophet/)
  - Pronósticos robustos con manejo de estacionalidad
  - Interpretable, maneja datos faltantes bien

- **Scikit-learn: Time Series**
  - Validación cruzada específica para series de tiempo

### Aplicaciones Educativas
- Predicción de rendimiento estudiantil basada en datos históricos
- Análisis de tendencias en matrícula institucional
- Pronósticos presupuestarios universitarios

## Interpretabilidad y Explicabilidad (SHAP)

### Referencia Académica Fundacional
- **"A Unified Approach to Interpreting Model Predictions"** (2017)
  - Autores: Lundberg, S. M. & Lee, S-I
  - *Advances in Neural Information Processing Systems*
  - Fundamento teórico de SHAP (SHapley Additive exPlanations)
  - [Publicación de referencia](https://arxiv.org/abs/1705.07874)

### Documentación SHAP
- **SHAP Official Documentation**
  - [https://shap.readthedocs.io/](https://shap.readthedocs.io/)
  - Installation, tutoriales, ejemplos
  - Métodos: Tree SHAP, Deep SHAP, Kernel SHAP, Linear SHAP

- **SHAP GitHub Repository**
  - [https://github.com/shap/shap](https://github.com/shap/shap)
  - Notebook examples, casos de uso

### LIME (Alternative a SHAP)
- **LIME: Local Interpretable Model-agnostic Explanations**
  - [https://github.com/marcotcr/lime](https://github.com/marcotcr/lime)
  - Interpretabilidad local y agnóstica a modelos

### Feature Importance
- **Permutation Feature Importance** (Breiman, 2001)
- **Scikit-learn Feature Importance**
  - [https://scikit-learn.org/stable/modules/inspection.html](https://scikit-learn.org/stable/modules/inspection.html)

## Validación y Evaluación de Modelos

### Documentación Scikit-learn
- **Scikit-learn: Model Evaluation**
  - [https://scikit-learn.org/stable/modules/model_evaluation.html](https://scikit-learn.org/stable/modules/model_evaluation.html)
  - Métricas de regresión: MSE, RMSE, MAE, R²
  - Métricas de clasificación: accuracy, precision, recall, F1, AUC-ROC

### Validación Cruzada
- **Cross-validation**
  - k-fold, stratified k-fold, time series split
  - Prevención de overfitting

### Hyperparameter Tuning
- **Grid Search, Random Search, Bayesian Optimization**
  - Scikit-learn GridSearchCV, RandomizedSearchCV
  - Optuna para optimización más sofisticada

## Recursos en Línea Prácticos

### Plataformas Educativas
- **StatQuest with Josh Starmer (YouTube)**
  - [https://www.youtube.com/c/joshstarmer](https://www.youtube.com/c/joshstarmer)
  - Explicaciones visuales de algoritmos complejos
  - Regresión, clasificación, clustering, neural networks

- **Kaggle Learn**
  - [https://www.kaggle.com/learn](https://www.kaggle.com/learn)
  - Micro-cursos: Intro to Machine Learning, Intermediate ML, Feature Engineering
  - Datasets para práctica

- **Fast.ai**
  - [https://www.fast.ai/](https://www.fast.ai/)
  - Cursos de deep learning y machine learning
  - Top-down approach (aplicación antes de teoría)

### Comunidad Hispanohablante
- **Ciencia de Datos.net** (Javi Agenjo)
  - [https://www.cienciadedatos.net/](https://www.cienciadedatos.net/)
  - Tutoriales, guías, casos de estudio en español
  - Regresión, clasificación, series de tiempo, NLP

- **Aprendizaje de Máquina en Español**
  - Comunidad de ciencia de datos en América Latina

## Machine Learning en Contextos Educativos

### Aplicaciones Prácticas
- **Predictive Analytics for Student Success**
  - Modelos para identificar estudiantes en riesgo
  - Regresión/clasificación de rendimiento académico

- **Institutional Data Analytics**
  - Pronósticos de matrícula
  - Análisis de retención estudiantil
  - Optimización de asignación de recursos

### Investigación Académica
- Búsqueda: "machine learning in higher education" en Google Scholar
- Journals: *Computers & Education*, *International Journal of Educational Data Mining*

## Redes Neuronales y Deep Learning

### TensorFlow y Keras
- **TensorFlow Official Documentation**
  - [https://www.tensorflow.org/](https://www.tensorflow.org/)
  - Guías, tutoriales, API reference

- **Keras Sequential Models**
  - [https://keras.io/api/models/sequential/](https://keras.io/api/models/sequential/)
  - Redes neuronales densas, convolucionales, recurrentes

### Recursos Complementarios
- **Deep Learning Specialization (Coursera - Andrew Ng)**
- **Fast.ai: Practical Deep Learning**

## Herramientas Complementarias

### NumPy y SciPy
- **NumPy Official Documentation**
  - [https://numpy.org/doc/](https://numpy.org/doc/)

- **SciPy Official Documentation**
  - [https://scipy.org/](https://scipy.org/)
  - Optimización, estadística, álgebra lineal

### Visualización de Modelos
- **Matplotlib & Seaborn**
  - Gráficos de diagnóstico
  - Curvas de aprendizaje, matrices de confusión

- **Yellowbrick**
  - [https://www.scikit-yb.org/](https://www.scikit-yb.org/)
  - Visualización especializada para machine learning

## Cursos Recomendados

- **Coursera: Machine Learning Specialization** (Andrew Ng)
- **Coursera: Applied Data Science with Python** (University of Michigan)
- **edX: Machine Learning Fundamentals** (UC San Diego)
- **Udacity: Machine Learning Nanodegree**
- **Kaggle Competitions** - Aprendizaje práctico y competitivo

## Buenas Prácticas

### Reproducibilidad
- Documentación clara del pipeline
- Versionamiento de datos y modelos
- Semillas aleatorias fijas para replicabilidad

### Ética en ML
- Sesgos en datos de entrenamiento
- Equidad en modelos predictivos
- Transparencia y explicabilidad

### Estructura de Proyectos
- Separación: datos, modelos, reportes
- Scripts reproducibles
- Documentación de supuestos y limitaciones

---

**Última actualización:** Febrero 2026
**Orientación:** Universidad Catolica Andres Bello (UCAB), FACES
**Contexto:** Formación de docentes en Ciencia de Datos e Inteligencia de Negocios
