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
- Parameters in API paths like `{id}` become **Excel Named Ranges** (e.g., `ClientID`)
- Power Query within the `.odc` handles authentication and data parsing

## 📑 API Endpoint Docs

All endpoint-specific documentation is in the [`docs/`](./docs/README.md) folder. Each file includes:
- Path and operation summary
- Parameters required
- Excel-specific details
- Link to the `.odc` file

## 📈 Using the SDK

1. Open Excel
2. Use **Data → Existing Connections → Browse for More...**
3. Paste this into the address bar to find and select an `.odc` file:
   ```
   \\jgiquality.sharepoint.com@SSL\sites\JGI\Shared Documents\General\Excel-Qualer-SDK\
   ```
![image](https://github.com/user-attachments/assets/e536b959-8e1d-4fa3-a34e-058a9baf2f8f)

4. Ensure the required **named ranges** are present in your workbook.
  - In the `Formula` Tab, find "Define Name" or "Name Manager" in the _Defined Names_ section
    ![image](https://github.com/user-attachments/assets/b0ae65a3-eac9-4e63-a6f3-3eff3e0f3813)
5. Refresh the query to pull live data from the API.
  ![image](https://github.com/user-attachments/assets/ee83bb7a-b0de-4a65-8b80-7188930fac71)

> ℹ️ Excel must be set to **Anonymous** for web credentials. The API token is handled inside the Power Query headers.

## 🔐 Security

Make sure `.env` contains your token:
```
QUALER_API_TOKEN=Api-Token your-token-here
```
And that `.gitignore` excludes it from commits.

---

## 📦 Want to Extend This?

- Add support for `POST`, `PUT`, or `query` parameters
- Generate `.xlsx` templates with named ranges pre-filled
- Publish to SharePoint or GitHub Pages for distribution

---
