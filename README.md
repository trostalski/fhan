# Fhan

Fhan is a small [FHIR](https://www.hl7.org/fhir/overview.html) query client with a focus on usability.

```python
from fhan.client import Client

client = Client("http://hapi.fhir.org/baseR4/")
patients = client.get("Patient", count=1)
print(patients)
```

## Installation

Import the package

```shell
pip install fhan
```

## Usage

Import and instantiate the client Class:

```python
from fhan.client import Client

client = Client("https://hapi.fhir.org/baseR4/")
```

Get a Resource by id:

```python
client.get("Condition", "1")
```

Search for resources:

```python
client.get("Observation", search_params={"code":"8310-5"}, count=20)
```

## Other Tools

- Use [Fhir-Views](https://fhir-views.vercel.app/) to inspect FHIR Bundles-
