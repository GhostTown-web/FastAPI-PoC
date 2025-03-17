import uvicorn

from fastapi import FastAPI

from filters.countries import FilterCountries
from filters.phases import FilterPhases
from filters.status import FilterStatus
from filters.therapeutic_area import FilterTherapeuticArea
from filters.sponsor import FilterSponsor

app = FastAPI()


@app.get("/home")
async def root():
    return {"message": "Welcome to the Home Page"}


@app.get("/api/v1/countries/{country_name}")
async def country_filter(country_name: str):
    country_obj = FilterCountries()
    result = country_obj.create_json()

    # if country_name != '':
    #     return {country_name: result.get(country_name, "NULL")}
    #
    # return {"country_dictionary": obj.create_json()}

    return {country_name: result.get(country_name, "NULL"),
            "country_dictionary": result}


@app.get("/api/v1/phases/{phase}")
async def filter_phases(phase: str):
    phases_obj = FilterPhases()
    result = phases_obj.create_json()

    return {phase: result.get(phase, "NULL"),
            "phase_dictionary": result}


@app.get("/api/v1/status/{status}")
async def filter_status(status: str):
    status_obj = FilterStatus()
    result = status_obj.create_json()

    return {status: result.get(status, "NULL"),
            "status_dictionary": result}


@app.get("/api/v1/therapeutic_area/{therapeutic_area_name}")
async def filter_therapeutic_area(therapeutic_area_name: str):
    therapeutic_area_obj = FilterTherapeuticArea()
    result = therapeutic_area_obj.create_json()

    return { therapeutic_area_name: result.get(therapeutic_area_name, "NULL"),
            "therapeutic_area_dictionary": result }


@app.get("/api/v1/sponsor/{sponsor_name}")
async def filter_sponsor(sponsor_name: str):
    sponsor_obj = FilterSponsor()
    result = sponsor_obj.create_json()

    return {sponsor_name: result.get(sponsor_name, "NULL"),
            "sponsor_dictionary": result}


if __name__ == '__main__':
    uvicorn.run("main:app", host='localhost', port=8000, reload=True)
