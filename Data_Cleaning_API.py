from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse, JSONResponse
import pandas as pd
import io

app = FastAPI()

def clean_data_from_csv(uploaded_df: pd.DataFrame) -> pd.DataFrame:
    df = uploaded_df.copy()

    #Drop completely empty columns
    df.dropna(axis=1, how='all', inplace=True)

    #Drop duplicate rows
    df.drop_duplicates(inplace=True)

    #Standardize column names - lowercase with underscores
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    #Drop rows missing key fields
    required_columns = ['price', 'address', 'city', 'state']
    for col in required_columns:
        if col in df.columns:
            df = df[df[col].notnull()]
    
    # Convert price and size columns to numeric
    for col in ['price', 'size_sqft']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    #Handle rows with missing or zero values in important fields
    df = df[df['price'] > 0]
    if 'size_sqft' in df.columns:
        df = df[df['size_sqft'] > 0]


    return df


@app.post("/clean-data/csv")
async def clean_data_csv(file: UploadFile = File(...)):
    try:
        uploaded_df = pd.read_csv(file.file)
        cleaned_df = clean_data_from_csv(uploaded_df)
        stream = io.StringIO()
        cleaned_df.to_csv(stream, index=False)
        stream.seek(0)
        return StreamingResponse(
            stream,
            media_type="text/csv",
            headers={"Content-Disposition": "attachment; filename=cleaned_data.csv"}
        )
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})

if __name__ == "__main__":
    import nest_asyncio
    import uvicorn
    nest_asyncio.apply()
    uvicorn.run(app, host="0.0.0.0", port=8000)