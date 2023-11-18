# Fhan

Fhan is a small [FHIR](https://www.hl7.org/fhir/overview.html) query client with a focus on performance and usability.

```python
from fhan.client import Client

client = Client(base_url="http://hapi.fhir.org/baseR4/", authenticate=False)
patients = client.get("Patient", count=1)
print(patients)
```

## Installation

To get started with Fhan, install it using pip:

```shell
pip install fhan
```

## Basic Usage

**Check out the [example notebooks](./examples).**

After installation, you can begin using Fhan to query FHIR resources:

```python
from fhan.client import Client

# The server is public and does not require authentication
client = Client("https://hapi.fhir.org/baseR4/", authenticate=False)
```

Get a Resource by id:

```python
client.get("Condition", "39238")
```

Search for resources:

```python
client.get("Observation", search_params={"code":"8310-5"}, count=20)
```

## Features
- Intelligent Autocomplete
- Integrated Metadata and Package Context Management
- `SearchBuilder` for Incremental Search Query Construction
- Seamless Authentication
- Efficient Caching Mechanism
- Object-Oriented FHIR Resources
- FHIR Views Integration ([link](https://build.fhir.org/ig/FHIR/sql-on-fhir-v2/))
- `ViewBuilder` for Robust View Construction

## Authentication

For servers that require authentication:

Copy `.env.example` to `.env`.
Fill in your authentication details in the .env file.
Currently, Fhan supports a limited set of authentication methods. Contributions to expand authentication support are welcome!

## Other Tools

- Fhan is using [rye](https://github.com/mitsuhiko/rye) for managing packages.
- Use [Fhir-Views](https://fhir-views.vercel.app/) to inspect FHIR Bundles.
