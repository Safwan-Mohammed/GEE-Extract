from fastapi import APIRouter, UploadFile, File, Form
from app.services.geojson_service import process_geojson
from app.services.s1_service import extract_s1_parameters
from app.services.s2_service import extract_s2_parameters

router = APIRouter()

@router.post("/extract-s1-parameters")
async def extract_s1_parameters_endpoint(
    geojson: UploadFile = File(..., description="GeoJSON file defining the region of interest"),
    start_date: str = Form(..., description="Start date in YYYY-MM-DD format"),
    end_date: str = Form(..., description="End date in YYYY-MM-DD format")
):
    geometry = process_geojson(geojson)
    results = extract_s1_parameters(geometry, start_date, end_date)
    return results

@router.post("/extract-s2-parameters")
async def extract_s2_parameters_endpoint(
    geojson: UploadFile = File(..., description="GeoJSON file defining the region of interest"),
    start_date: str = Form(..., description="Start date in YYYY-MM-DD format"),
    end_date: str = Form(..., description="End date in YYYY-MM-DD format")
):
    geometry = process_geojson(geojson)
    results = extract_s2_parameters(geometry, start_date, end_date)
    return results
