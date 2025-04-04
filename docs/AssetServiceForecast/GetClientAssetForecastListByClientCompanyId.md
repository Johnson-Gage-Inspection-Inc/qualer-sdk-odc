# `AssetServiceForecast_GetClientAssetForecastListByClientCompanyId`

**URL Template:**
`GET /api/assetserviceforecast/client/{clientCompanyId}`

**Parameters:**
- *`clientCompanyId`: `integer`


> *Required parameters are marked with an asterisk (*).

**Excel Named Range(s):**
- `ClientCompanyId`


**Description:**
No description provided.

### Response Schema

#### OK [200]

| Field                      | Type    |
|:---------------------------|:--------|
| CompanyId                  | integer |
| AssetId                    | integer |
| SiteId                     | integer |
| AssetServiceRecordId       | integer |
| SerialNumber               | string  |
| AssetUser                  | string  |
| AssetTag                   | string  |
| EquipmentId                | string  |
| AssetName                  | string  |
| CategoryName               | string  |
| ManufacturerName           | string  |
| SiteName                   | string  |
| MaintenancePlanId          | integer |
| MaintenancePlanName        | string  |
| MaintenanceTaskId          | integer |
| MaintenanceTaskName        | string  |
| NextServiceDate            | string  |
| AdvanceRecallDate          | string  |
| GracePeriodDate            | string  |
| CertificateNextServiceDate | string  |
| ServiceInterval            | string  |
| IntervalCycle              | string  |
| IntervalLength             | integer |
| OnDay                      | string  |
| OnMonth                    | string  |
| OnWeekDays                 | string  |
| WeekdayOfMonth             | string  |
| AdvanceRecallPeriod        | string  |
| DaysBeforeDue              | integer |
| PastDueGracePeriod         | string  |
| DaysAfterDue               | integer |

**Group (Tag):**
AssetServiceForecast

**ODC File:**
[Excel-Qualer-SDK/AssetServiceForecast/AssetServiceForecast_GetClientAssetForecastListByClientCompanyId.odc](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-odc/blob/main/Excel-Qualer-SDK/AssetServiceForecast/AssetServiceForecast_GetClientAssetForecastListByClientCompanyId.odc)

---

To Use in Excel:
---

1. Go to the ![`Data`](https://github.com/user-attachments/assets/da437a70-57b3-4c5b-bb01-4910ece19ed1)
 tab.
3. Click ![Existing Connections](https://github.com/user-attachments/assets/a2f1ed67-b2e0-4c23-ac90-68c870e60289)
4. Click ![`Browse for More...`](https://github.com/user-attachments/assets/8e698494-6865-41e7-b6fa-043aea81809a)
5. Paste the following into the URL bar
```
\\jgiquality.sharepoint.com@SSL\sites\JGI\Shared Documents\General\Excel-Qualer-SDK\AssetServiceForecast\
```

![image](https://github.com/user-attachments/assets/1e1a8d87-0377-446d-aaf5-d78562991db3)

6. Select `AssetServiceForecast_GetClientAssetForecastListByClientCompanyId.odc` and click `Open`.

> ⚠️ If parameters are needed, you'll see an error now. It's ok, but you'll need to set them.

### Setting parameters
If there are any parameters listed near the top of this file, create a named range with each name listed under **Excel Named Range(s):**
> They're just named ranges, with particular names.
