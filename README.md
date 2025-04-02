# Qualer Excel SDK

[![Last Commit](https://img.shields.io/github/last-commit/Johnson-Gage-Inspection-Inc/qualer-sdk-odc)](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-odc/commits/main)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Uses ODC & PowerQuery](https://img.shields.io/badge/Excel-.odc%20%2B%20PowerQuery-brightgreen)](#)
[![Qualer API](https://img.shields.io/badge/Qualer%20API-v1-orange)](https://jgiquality.qualer.com/swagger/ui/index)

> 📊 Auto-generated `.odc` files to query the Qualer API from Microsoft Excel.

This repository contains an auto-generated SDK that connects Microsoft Excel to the [Qualer API](https://jgiquality.qualer.com) using `.odc` (Office Data Connection) files and Power Query.

## 📂 Directory Structure

```
qualer-sdk-odc/
├── Excel-Qualer-SDK/    # Generated .odc files grouped by API tag
├── docs/                # One Markdown doc per GET endpoint
├── generate.py          # Generator script for ODC + docs
├── spec.json            # Swagger/OpenAPI v2 spec from Qualer
├── .env                 # Environment variables (e.g., QUALER_API_TOKEN)
└── README.md            # You're here
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

## 📈 Using the SDK

1. Open Excel
2. Use **Data → Existing Connections → Browse for More...**
3. Paste this into the file dialog’s address bar to browse and select an  `.odc` file:
   ```
   \\jgiquality.sharepoint.com@SSL\sites\JGI\Shared Documents\General\Excel-Qualer-SDK\
   ```
![image](https://github.com/user-attachments/assets/e536b959-8e1d-4fa3-a34e-058a9baf2f8f)

4. Ensure the required **named ranges** are defined in your workbook.
  - Go to **Formulas → Name Manager** to verify or create ranges (e.g., `ClientID`, `CompanyId`)
    ![image](https://github.com/user-attachments/assets/b0ae65a3-eac9-4e63-a6f3-3eff3e0f3813)
5. Refresh the query to pull live data from the API.
  ![image](https://github.com/user-attachments/assets/ee83bb7a-b0de-4a65-8b80-7188930fac71)

> ℹ️ Excel’s data connection must be set to use **Anonymous** authentication.  
> The API token is automatically included in the request headers by the Power Query script inside the `.odc`.

## 🔄 Shaping the data

“The raw data might not be immediately usable — but Power Query makes it easy to transform.

![HowTo](https://github.com/user-attachments/assets/64bdc174-0a84-4439-8610-969b7161cb7e)

1. You'll probably see a list of "Records" or something else other than the data you want
2. To fix this, go to Queries and Connections
3. Edit the query that needs fixed
4. Click the expand button ![image](https://github.com/user-attachments/assets/265f49b9-9679-425d-a1c8-02d387a67871) next to the column header (if available).
5. ❗ If it's missing, delete the last step, ![❌ ConvertToTable](https://github.com/user-attachments/assets/14282043-48e2-4ded-96bc-56c30c189180) and try again.
6. From here, you should be able to shape and filter the data according to your particular use-case. For transformation tips, check out [Power Query in Excel (Microsoft Docs)](https://learn.microsoft.com/en-us/power-query/) or explore [M code reference](https://learn.microsoft.com/powerquery-m/) for advanced customization.
7. Finally, click `Close & Load` ![image](https://github.com/user-attachments/assets/0c06bad1-b6ac-424b-ac10-0a49125898e6)


### ➡️ Quick Example

To get a list of our customers:

1. Download and open the connection file: [`Clients_GetAll.odc`](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-odc/blob/main/Excel-Qualer-SDK/Clients/Clients_GetAll.odc)
2. Define no parameters — this endpoint doesn’t require any input.
3. Expand the columns as described [above](#-shaping-the-data).
4. Click **Refresh** to fetch all client records from Qualer.

## 🧪 Tested With

- Microsoft® Excel® for Microsoft 365 MSO (Version 2502 Build 16.0.18526.20168) 64-bit 
- SharePoint Online (Modern experience)
- Qualer API v1 (as of March 2025)

## 🔐 Developer's note

When generating the SDK, make sure `.env` contains your token:
```
QUALER_API_TOKEN=Api-Token your-token-here
```
And that `.gitignore` excludes it from commits.
