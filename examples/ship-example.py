# Due to data privacy concerns, this code is not in a jupyter notebook.

from pprint import pprint

from fhirmodels.R4 import Observation

from fhan.client import Client

# SET THESE ENVIRONMENT VARIABLES in the .env file
LOGIN_URL = "https://ship.ume.de/app/Auth/v1/basicAuth"
REFRESH_URL = "https://ship.ume.de/app/Auth/v1/refresh"
BASE_URL = "https://ship.ume.de/app/FHIR/r4"


if __name__ == "__main__":
    # Create a client object, ensure that the auth environment variables are set inside the .env
    client = Client(base_url="https://ship.ume.de/app/FHIR/r4/")

    # Get a patient by ID
    patient = client.get(
        resource_type="Patient",
        id="75eae276f9d78ede8add4f6c6734f66f534495326d42fc42dc4104fe06ad6fc7",
    )
    pprint(patient)

    # # Get a a bundle of 5 patients
    patients = client.get("Patient", count=5)
    pprint(patients)

    # # Get a bundle of 5 conditions with the code ICD I64 (Stroke, not specified as hemorrhage or infarction)
    conditions = client.get("Condition", search_params={"code": "I64"}, count=5)
    pprint(conditions)

    # Also get the patients for the conditions above
    bundle = client.get(
        "Condition",
        search_params={"code": "I64"},
        count=5,
        revinclude="Condition:subject",
    )
    # same as "conditions = client.get("Condition", search_params={"code": "I64"}, count=5)"
    pprint(bundle)

    # Get a bundle of 5 observations with the code zHb (hemoglobin) as a Search Bundle Object
    observations = client.get(
        "Observation", search_params={"code": "zHb"}, count=5, as_object=True
    )
    pprint(observations)

    # get resource dictionaries as list
    observation_dicts = observations.resources
    observations_objs = [Observation.from_dict(obs) for obs in observation_dicts]

    # we can now access the fhir elements as objects
    pprint(observations_objs[0].code.coding[0].display)
