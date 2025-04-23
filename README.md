# Qualer Excel SDK

[![Last Commit](https://img.shields.io/github/last-commit/Johnson-Gage-Inspection-Inc/qualer-sdk-odc)](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-odc/commits/main)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Uses ODC & PowerQuery](https://img.shields.io/badge/Excel-.odc%20%2B%20PowerQuery-brightgreen)](#)
[![Qualer API](https://img.shields.io/badge/Qualer%20API-v1-orange)](https://jgiquality.qualer.com/swagger/ui/index)

Welcome to the Qualer Excel SDK! This repository provides an auto-generated SDK to connect Microsoft Excel to the Qualer API using .odc (Office Data Connection) files and Power Query.

## Overview

The SDK automates the creation of:
- A .odc file per **GET** endpoint (located in [Excel-Qualer-SDK](Excel-Qualer-SDK/)) for use in Excel.
- Endpoint-specific Markdown documentation files (located in [docs](./docs/README.md)).
- A centralized Markdown index for easy navigation of the API documentation.

## Directory Structure

```
qualer-sdk-odc/
├── Excel-Qualer-SDK/    # Generated .odc files grouped by API tag
├── docs/                # Markdown documentation files for each GET endpoint and index
├── src/                 # Source code for generating .odc and Markdown files
│   ├── generate.py      # Main generator script
│   ├── odc_writer.py    # ODC file rendering logic
│   └── doc_writer.py    # Documentation file writing logic
├── spec.json            # Swagger/OpenAPI v2 specification from Qualer
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

## 🔧 How It Works

- `generate.py` reads the Swagger spec and creates:
  - A `.odc` file per **GET** endpoint for use in Excel
  - A `.md` documentation file per endpoint (in [`docs/`](./docs/README.md))
- Parameters in API paths like `{id}` are converted to **Excel Named Ranges** (e.g., `ClientID`), allowing users to control query inputs from the workbook itself.
- Power Query embedded in each `.odc` handles both authentication and JSON parsing behind the scenes.

## 📑 API Endpoint Docs

All endpoint-specific documentation is in the [`docs/`](./docs/README.md) folder. Each file includes:
- Path and operation summary
- Parameters required
- Excel-specific details
- Link to the `.odc` file

## Using the SDK

1. Open Excel
2. Use **Data → Existing Connections → Browse for More...**
3. Paste this into the file dialog’s address bar to browse and select an  `.odc` file:
   ```
   \\jgiquality.sharepoint.com@SSL\sites\JGI\Shared Documents\General\Excel-Qualer-SDK\
   ```
![image](https://github.com/user-attachments/assets/e536b959-8e1d-4fa3-a34e-058a9baf2f8f)

4. Ensure the required **named ranges** are present in your workbook.
  - Go to **Formulas → Name Manager** to verify or create ranges (e.g., `AssetId`, `ClientCompanyId`,)
    ![image](https://github.com/user-attachments/assets/b0ae65a3-eac9-4e63-a6f3-3eff3e0f3813)
5. Refresh the query to pull live data from the API.
  ![image](https://github.com/user-attachments/assets/ee83bb7a-b0de-4a65-8b80-7188930fac71)

> ℹ️ Excel’s data connection must be set to use **Anonymous** authentication.
> The API token is automatically included in the request headers by the Power Query script inside the `.odc`.

## Shaping the Data

The raw data from the API might require transformation before analysis. Use Excel's Power Query Editor to:
- Expand columns.
- Filter and transform the data accordingly.

For transformation tips, refer to [Power Query in Excel (Microsoft Docs)](https://learn.microsoft.com/en-us/power-query/) or the [M code reference](https://learn.microsoft.com/powerquery-m/).


### ➡️ Quick Example

To get a list of our customers:

1. Download and open the connection file: [`Clients_GetAll.odc`](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-odc/blob/main/Excel-Qualer-SDK/Clients/Clients_GetAll.odc)
2. Define no parameters — this endpoint doesn’t require any input.
3. Expand the columns as described [above](#-shaping-the-data).
4. Click **Refresh** to fetch all client records from Qualer.
## Tested With

- Microsoft® Excel® for Microsoft 365 (64-bit)
- SharePoint Online (Modern experience)
- Qualer API v1 (as of April 2025)
