# `ReportDatasets_GetReferenceStandardsByServiceOrderItemId`

**URL Template:**
`GET /api/data/ReferenceStandards/{serviceOrderItemId}`

**Parameters:**
- *`serviceOrderItemId`: `integer`


> *Required parameters are marked with an asterisk (*).

**Excel Named Range(s):**
- `ServiceOrderItemId`


**Description:**
No description provided.

### Response Schema

#### OK

+------------------------+---------+
| Field                  | Type    |
+========================+=========+
| IsAuxiliary            | boolean |
+------------------------+---------+
| LastServiceDate        | string  |
+------------------------+---------+
| NextServiceDate        | string  |
+------------------------+---------+
| CertificateNumber      | string  |
+------------------------+---------+
| CalibratedBy           | string  |
+------------------------+---------+
| ToolName               | string  |
+------------------------+---------+
| ToolSite               | string  |
+------------------------+---------+
| ToolRoom               | string  |
+------------------------+---------+
| ToolStation            | string  |
+------------------------+---------+
| ToolLocation           | string  |
+------------------------+---------+
| AssetTag               | string  |
+------------------------+---------+
| LotNumber              | string  |
+------------------------+---------+
| AssetUser              | string  |
+------------------------+---------+
| ToolTypeName           | string  |
+------------------------+---------+
| ToolDescription        | string  |
+------------------------+---------+
| ToolId                 | integer |
+------------------------+---------+
| Manufacturer           | string  |
+------------------------+---------+
| SerialNumber           | string  |
+------------------------+---------+
| Area                   | string  |
+------------------------+---------+
| ServiceOrderItemId     | integer |
+------------------------+---------+
| ManufacturerPartNumber | string  |
+------------------------+---------+
| EquipmentId            | string  |
+------------------------+---------+

**Group (Tag):**
ReportDatasets

**ODC File:**
[Excel-Qualer-SDK/ReportDatasets/ReportDatasets_GetReferenceStandardsByServiceOrderItemId.odc](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-odc/blob/main/Excel-Qualer-SDK/ReportDatasets/ReportDatasets_GetReferenceStandardsByServiceOrderItemId.odc)

---

To Use in Excel:
---

1. Go to the ![`Data`](https://github.com/user-attachments/assets/da437a70-57b3-4c5b-bb01-4910ece19ed1)
 tab.
3. Click ![Existing Connections](https://github.com/user-attachments/assets/a2f1ed67-b2e0-4c23-ac90-68c870e60289)
4. Click ![`Browse for More...`](https://github.com/user-attachments/assets/8e698494-6865-41e7-b6fa-043aea81809a)
5. Paste the following into the URL bar
```
\\jgiquality.sharepoint.com@SSL\sites\JGI\Shared Documents\General\Excel-Qualer-SDK\ReportDatasets\
```

![image](https://github.com/user-attachments/assets/1e1a8d87-0377-446d-aaf5-d78562991db3)

6. Select `ReportDatasets_GetReferenceStandardsByServiceOrderItemId.odc` and click `Open`.

> ⚠️ If parameters are needed, you'll see an error now. It's ok, but you'll need to set them.

### Setting parameters
If there are any parameters listed near the top of this file, create a named range with each name listed under **Excel Named Range(s):**
> They're just named ranges, with particular names.
