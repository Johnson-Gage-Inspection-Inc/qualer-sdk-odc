# `AssetReservation_Get`
> 
    
**URL Template:**
`GET /api/assetsreservations`

**Parameters (Named Ranges):**

> *Required parameters are bolded.*

| Name                | Type    | Format    |
|:--------------------|:--------|:----------|
| Model.from          | string  | date-time |
| Model.to            | string  | date-time |
| Model.assetId       | integer | int32     |
| Model.areaId        | integer | int32     |
| Model.productId     | integer | int32     |
| Model.serialNumber  | string  | nan       |
| Model.assetTag      | string  | nan       |
| Model.reservationId | integer | int32     |

**Description:**
No description provided.

### Response Schema

#### OK [200]

| Field             | Type    |
|:------------------|:--------|
| OriginalBeginDate | string  |
| OriginalEndDate   | string  |
| BeginDate         | string  |
| EndDate           | string  |
| ReservedOn        | string  |
| ReservedOnUtc     | string  |
| Comments          | string  |
| ProductId         | integer |
| AssetId           | integer |
| ServiceOrderId    | integer |
| ReservedById      | integer |
| ReservedByName    | string  |

**Group (Tag):**
AssetReservation

**ODC File:**
[Excel-Qualer-SDK/AssetReservation/AssetReservation_Get.odc](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-odc/blob/main/Excel-Qualer-SDK/AssetReservation/AssetReservation_Get.odc)

---

To Use in Excel:
---

1. Go to the ![`Data`](https://github.com/user-attachments/assets/da437a70-57b3-4c5b-bb01-4910ece19ed1)
 tab.
3. Click ![Existing Connections](https://github.com/user-attachments/assets/a2f1ed67-b2e0-4c23-ac90-68c870e60289)
4. Click ![`Browse for More...`](https://github.com/user-attachments/assets/8e698494-6865-41e7-b6fa-043aea81809a)
5. Paste the following into the URL bar
```
\\jgiquality.sharepoint.com@SSL\sites\JGI\Shared Documents\General\Excel-Qualer-SDK\AssetReservation\
```

![image](https://github.com/user-attachments/assets/1e1a8d87-0377-446d-aaf5-d78562991db3)

6. Select `AssetReservation_Get.odc` and click `Open`.

> ⚠️ If parameters are needed, you'll see an error now. It's ok, but you'll need to set them.

### Setting parameters
If there are any parameters listed near the top of this file, create a named range with each name listed under **Excel Named Range(s):**
> They're just named ranges, with particular names.
