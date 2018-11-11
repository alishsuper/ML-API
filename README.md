# ML-API
Модель определения качества вина на основе его физико-химических характеристик

Для запуска и установки необходимо:
1. Скачать проект - git clone git@github.com:alishsuper/ML-API.git
2. Перейти в папку ML-API - cd ML-API
3. Сбилдить проект - docker build -t ml-api
4. Запустить проект - docker run -p 80:8080 ml-api
5. Перейти в localhost//api/winequality/query
6. Тип запроса - объекты-признаки
{
    "fixed acidity": 7.4,
    "volatile acidity": 0.70,
    "citric acid": 0.00,
    "residual sugar": 1.9,
    "chlorides": 0.076,
    "free sulfur dioxide": 11.0,
    "total sulfur dioxide": 34.0,
    "density": 0.9978,
    "pH": 3.51,
    "sulphates": 0.56,
    "alcohol": 9.4
}
7. Тип ответа - качество вина
{
    "quality": 5
}
