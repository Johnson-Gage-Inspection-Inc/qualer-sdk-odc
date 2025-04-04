# `ClientAssets_GetAssetManagerListByClientCompanyId`
> GetAssetManagerList
    
**URL Template:**
`GET /api/service/clients/{clientCompanyId}/assets/byfilter`

**Parameters (Named Ranges):**

> *Required parameters are bolded.*

| Excel Name          | Type    | In    |
|:--------------------|:--------|:------|
| **ClientCompanyId** | integer | path  |
| Query.filterType    | string  | query |
| Query.searchString  | string  | query |
| Query.page          | integer | query |
| Query.pageSize      | integer | query |

**Description:**
assetFilterType: ClientUnset, ClientAssetsCollected, ClientPastDue, ClientDueForService, ClientOutOfService, ClientWithoutSchedule
            
ClientDueForService - depends on Employee Filter Preference
POST api/user/filters

### Response Schema

#### OK [200]

| Field                    | Type    |
|:-------------------------|:--------|
| AssetId                  | integer |
| AssetName                | string  |
| AssetDescription         | string  |
| AssetMaker               | string  |
| RecordType               | string  |
| ParentAssetId            | integer |
| ChildrenCount            | integer |
| SiteId                   | integer |
| SerialNumber             | string  |
| AssetTag                 | string  |
| AssetUser                | string  |
| EquipmentId              | string  |
| LegacyIdentifier         | string  |
| Criticality              | string  |
| Condition                | string  |
| AssetClass               | string  |
| ActivationDate           | string  |
| RetirmentDate            | string  |
| ClientVendorId           | integer |
| CompanyName              | string  |
| SiteName                 | string  |
| AssetHasImage            | boolean |
| HasImage                 | boolean |
| ParentHasImage           | boolean |
| PoolId                   | integer |
| Pool                     | string  |
| ProductId                | integer |
| ParentProductId          | integer |
| ProductName              | string  |
| ParentProductName        | string  |
| CategoryId               | integer |
| RootCategoryId           | integer |
| CategoryName             | string  |
| RootCategoryName         | string  |
| ManufacturerId           | integer |
| Manufacturer             | string  |
| DisplayPartNumber        | string  |
| DisplayName              | string  |
| ManufacturerPartNumber   | string  |
| AssetRoom                | string  |
| Location                 | string  |
| Station                  | string  |
| ToolRole                 | string  |
| ToolId                   | integer |
| DepartmentId             | integer |
| DepartmentName           | string  |
| CustodianName            | string  |
| Warranty                 | string  |
| WarrantyEnd              | string  |
| IsWarrantyExpired        | boolean |
| DepreciationMethod       | integer |
| DepreciationBasis        | number  |
| SalvageValue             | number  |
| TotalServiceCost         | number  |
| LifeSpanMonths           | integer |
| DueForReplacementDate    | string  |
| DepreciationProc         | number  |
| PurchaseDate             | string  |
| PurchaseCost             | number  |
| TimeInService            | integer |
| RetirementReason         | string  |
| ResidualCost             | number  |
| EmployeeId               | integer |
| AssetCollectionId        | integer |
| AssetServiceRecordId     | integer |
| ResultStatus             | string  |
| AsFoundResult            | string  |
| AsLeftResult             | string  |
| LastServiceDate          | string  |
| LastService              | string  |
| NextServiceDate          | string  |
| NextService              | string  |
| ServiceScheduleSegmentId | integer |
| ServiceScheduleId        | integer |
| ServiceSchedule          | string  |
| InService                | boolean |
| InLastService            | boolean |
| ServiceOrderId           | integer |
| ServiceOrderStatus       | string  |
| CustomOrderNumber        | string  |
| ServiceOrderItemId       | integer |
| Vendor                   | string  |
| Technician               | string  |
| CertificateNumber        | string  |
| DueTriggerDate           | string  |
| PastDueTriggerDate       | string  |
| DueStatus                | string  |
| WorkStatus               | string  |
| ServiceTag               | string  |
| ServiceSiteName          | string  |
| ServiceSiteId            | integer |
| StandardTitle            | string  |
| Schedules                | string  |

**Group (Tag):**
ClientAssets

**ODC File:**
[Excel-Qualer-SDK/ClientAssets/ClientAssets_GetAssetManagerListByClientCompanyId.odc](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-odc/blob/main/Excel-Qualer-SDK/ClientAssets/ClientAssets_GetAssetManagerListByClientCompanyId.odc)

---

To Use in Excel:
---

1. Go to the ![`Data`](https://github.com/user-attachments/assets/da437a70-57b3-4c5b-bb01-4910ece19ed1)
 tab.
3. Click ![Existing Connections](https://github.com/user-attachments/assets/a2f1ed67-b2e0-4c23-ac90-68c870e60289)
4. Click ![`Browse for More...`](https://github.com/user-attachments/assets/8e698494-6865-41e7-b6fa-043aea81809a)
5. Paste the following into the URL bar
```
\\jgiquality.sharepoint.com@SSL\sites\JGI\Shared Documents\General\Excel-Qualer-SDK\ClientAssets\
```

![image](https://github.com/user-attachments/assets/1e1a8d87-0377-446d-aaf5-d78562991db3)

6. Select `ClientAssets_GetAssetManagerListByClientCompanyId.odc` and click `Open`.

> ⚠️ If parameters are needed, you'll see an error now. It's ok, but you'll need to set them.

### Setting parameters
If there are any parameters listed near the top of this file, create a named range with each name listed under **Excel Named Range(s):**
> They're just named ranges, with particular names.
