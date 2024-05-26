# Introduction

This is a small Machine Learning project using Python3 and Flask to deploy a automotive
repair cost prediction model as a service. The model itself is not publicly available,
but the code and the API are.

See the provided [Notebook](Notebook.ipynb) for more information about building
and deploying the model.

Feel free to build your own model and deploy it using the provided code.

# The Model

The model is derived from over 50,000 automotive repair invoices and is designed
to predict the service cost based on the ticket description.

It's based on the following properties:

- The ticket description
- The vehicle year
- The vehicle make
- The vehicle model

And it outputs the following properties:

- The predicted repair cost

Of the four different models tested, XGBRegressor from XGBoost was the best one
was selected based on the MSE metric along with the time it took to train. You can
see the results in the [Notebook](Notebook.ipynb).

# Deploying the API

To deploy the local development server, run the following commands:

```bash
pip install flask flask_restful flask_cors pickle pandas
```

```bash
PORT=5000 python src/app.py
```

You can then send an API Request to the following endpoint:

```cURL
curl --location 'http://localhost:5000/predict' \
--header 'Content-Type: application/json' \
--data '{
    "Description": "4 TIRES, FEA",
    "ModelYear": 2014,
    "Make": "TOYOTA",
    "Model": "PRIUS"
}'
```

```JavaScript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({
  "Description": "4 TIRES, FEA",
  "ModelYear": 2014,
  "Make": "TOYOTA",
  "Model": "PRIUS"
});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("http://localhost:5000/predict", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

Which returns

```json
{
    "cost": 655.4513549804688,
    "prediction": "Estimated repair cost: $655.45"
}
```
