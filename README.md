# Ikhlas_ML_Project
# Real Estate Property Pricing Prediction Project

## Project Objectives
This project simulates a real-world data task involving the collection, cleaning, integration, and modeling of real estate property data. The primary goals are:
- Collect property listings data from two real estate APIs.
- Clean and integrate the data to create a consistent dataset.
- Develop and evaluate predictive models to estimate property prices.

## APIs Used for Data Collection
- **ATTOM Property Data API**: [https://www.attomdata.com/solutions/property-data-api/](https://www.attomdata.com/solutions/property-data-api/)

## Data Collection and Cleaning
- **Data Collection**: Scripts were developed to authenticate and query the APIs, handle rate limiting and errors, and save raw data in CSV format.
- **Data Cleaning & Integration**:
  - Missing values were handled through imputation or removal based on context.
  - Inconsistent formatting (e.g., address formats, numeric fields) was standardized.
  - Column names and data types were unified for seamless integration.
- **Cleaning API**:  
  A RESTful API (built with FastAPI) was implemented to accept raw property data as CSV or file upload, perform cleaning and integration, and return the cleaned dataset as JSON or downloadable CSV.

### Running the Cleaning API
1. Install dependencies:  
   ```bash
   pip install -r requirements.txt
2. start the server --> uvicorn cleaning_api:app --reload

3.Interact with the API:
-Endpoint: POST /clean-data
-Accepts raw property data in JSON format or file upload.
-Returns cleaned and integrated data as JSON or CSV.
-See /docs endpoint for interactive Swagger UI documentation.
