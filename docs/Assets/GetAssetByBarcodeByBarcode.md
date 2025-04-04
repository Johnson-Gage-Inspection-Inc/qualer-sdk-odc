# `Assets_GetAssetByBarcodeByBarcode`

**URL Template:**
`GET /api/assets/bybarcode/{barcode}`

**Parameters:**
- *****`barcode`: `string`


> *****Required parameters are marked with an asterisk (*****).

**Excel Named Range(s):**
- `Barcode`


**Description:**
No description provided.

### Response Schema

#### OK
+------------------------+---------+
| Field                  | Type    |
+========================+=========+
| CompanyId              | integer |
+------------------------+---------+
| AssetId                | integer |
+------------------------+---------+
| SerialNumber           | string  |
+------------------------+---------+
| AssetUser              | string  |
+------------------------+---------+
| AssetTag               | string  |
+------------------------+---------+
| EquipmentId            | string  |
+------------------------+---------+
| AssetStatus            | string  |
+------------------------+---------+
| AssetName              | string  |
+------------------------+---------+
| AssetDescription       | string  |
+------------------------+---------+
| AssetMaker             | string  |
+------------------------+---------+
| Location               | string  |
+------------------------+---------+
| RoomNumber             | string  |
+------------------------+---------+
| Barcode                | string  |
+------------------------+---------+
| LegacyIdentifier       | string  |
+------------------------+---------+
| RootCategoryName       | string  |
+------------------------+---------+
| CategoryName           | string  |
+------------------------+---------+
| Class                  | string  |
+------------------------+---------+
| CustodianEmail         | string  |
+------------------------+---------+
| CustodianFirstName     | string  |
+------------------------+---------+
| CustodianLastName      | string  |
+------------------------+---------+
| CustodianName          | string  |
+------------------------+---------+
| Department             | string  |
+------------------------+---------+
| Station                | string  |
+------------------------+---------+
| Notes                  | string  |
+------------------------+---------+
| DocumentNumber         | string  |
+------------------------+---------+
| DocumentSection        | string  |
+------------------------+---------+
| CumulativeServiceCost  | number  |
+------------------------+---------+
| ProductId              | integer |
+------------------------+---------+
| ManufacturerPartNumber | string  |
+------------------------+---------+
| ProductName            | string  |
+------------------------+---------+
| ProductDescription     | string  |
+------------------------+---------+
| ProductManufacturer    | string  |
+------------------------+---------+
| SiteName               | string  |
+------------------------+---------+
| SiteId                 | integer |
+------------------------+---------+
| Condition              | string  |
+------------------------+---------+
| Criticality            | string  |
+------------------------+---------+
| Pool                   | string  |
+------------------------+---------+
| PurchaseDate           | string  |
+------------------------+---------+
| PurchaseCost           | number  |
+------------------------+---------+
| LifeSpanMonths         | integer |
+------------------------+---------+
| ActivationDate         | string  |
+------------------------+---------+
| DepreciationBasis      | number  |
+------------------------+---------+
| DepreciationMethod     | integer |
+------------------------+---------+
| RetirementDate         | string  |
+------------------------+---------+
| SalvageValue           | number  |
+------------------------+---------+
| RetirmentReason        | string  |
+------------------------+---------+
| CompositeParentId      | integer |
+------------------------+---------+
| CompositeChildCount    | integer |
+------------------------+---------+

**Group (Tag):**
Assets

**ODC File:**
[Excel-Qualer-SDK/Assets/Assets_GetAssetByBarcodeByBarcode.odc](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-odc/blob/main/Excel-Qualer-SDK/Assets/Assets_GetAssetByBarcodeByBarcode.odc)

---

To Use in Excel:
---

1. Go to the ![`Data`](https://github.com/user-attachments/assets/da437a70-57b3-4c5b-bb01-4910ece19ed1)
 tab.
3. Click ![Existing Connections](https://github.com/user-attachments/assets/a2f1ed67-b2e0-4c23-ac90-68c870e60289)
4. Click ![`Browse for More...`](https://github.com/user-attachments/assets/8e698494-6865-41e7-b6fa-043aea81809a)
5. Paste the following into the URL bar
```
\\jgiquality.sharepoint.com@SSL\sites\JGI\Shared Documents\General\Excel-Qualer-SDK\Assets\
```

![image](https://github.com/user-attachments/assets/1e1a8d87-0377-446d-aaf5-d78562991db3)

6. Select `Assets_GetAssetByBarcodeByBarcode.odc` and click `Open`.

> ⚠️ If parameters are needed, you'll see an error now. It's ok, but you'll need to set them.

### Setting parameters
If there are any parameters listed near the top of this file, create a named range with each name listed under **Excel Named Range(s):**
> They're just named ranges, with particular names.
