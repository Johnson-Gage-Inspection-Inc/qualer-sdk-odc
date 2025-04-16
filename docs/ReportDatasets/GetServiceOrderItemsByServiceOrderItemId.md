# `ReportDatasets_GetServiceOrderItemsByServiceOrderItemId`
> 

**URL Template:**
`GET /api/data/ServiceOrderItems/{serviceOrderItemId}`

**Parameters (Named Ranges):**

> *Required parameters are bolded.*

| Name                   | Type    | Format   |
|:-----------------------|:--------|:---------|
| **ServiceOrderItemId** | integer | int32    |

**Description:**
No description provided.

### Response Schema

#### OK [200]

| Field                           | Type    |
|:--------------------------------|:--------|
| CertificateNumber               | string  |
| DocumentNumber                  | string  |
| Revision                        | string  |
| EffectiveDate                   | string  |
| DocumentSection                 | string  |
| ServiceLevel                    | string  |
| ServiceLevelCode                | string  |
| ServiceType                     | string  |
| OrderItemNumber                 | integer |
| ServiceCharge                   | number  |
| UpdatedBy                       | string  |
| UpdatedOn                       | string  |
| WorkStatus                      | integer |
| CustomWorkStatus                | string  |
| ServiceComments                 | string  |
| ClientNotes                     | string  |
| VendorServiceNotes              | string  |
| DisplayName                     | string  |
| DisplayPartNumber               | string  |
| PartNumber                      | string  |
| ScheduleName                    | string  |
| SegmentName                     | string  |
| NextSegmentName                 | string  |
| IntervalLength                  | integer |
| IntervalCycle                   | string  |
| ServiceOptions                  | string  |
| ServiceOptionsPrice             | string  |
| ServiceOptionsDocumentNumbers   | string  |
| Location                        | string  |
| Station                         | string  |
| Room                            | string  |
| Site                            | string  |
| VendorId                        | integer |
| ServiceOrderNumber              | integer |
| CustomOrderNumber               | string  |
| LinkedOrderNumber               | string  |
| AssetId                         | integer |
| AssetClass                      | string  |
| AssetCondition                  | string  |
| AssetCriticality                | string  |
| AssetPool                       | string  |
| AssetName                       | string  |
| AssetDescription                | string  |
| AssetDocumentNumber             | string  |
| AssetDocumentSection            | string  |
| DocumentNumberValues            | string  |
| ProductName                     | string  |
| ProductDescription              | string  |
| AssetMaker                      | string  |
| CategoryName                    | string  |
| RootCategoryName                | string  |
| VendorTag                       | string  |
| ResultStatus                    | integer |
| ServiceDate                     | string  |
| NextServiceDate                 | string  |
| OriginalDueDate                 | string  |
| AssetTag                        | string  |
| Department                      | string  |
| AssetUser                       | string  |
| EquipmentId                     | string  |
| LegacyIdentifier                | string  |
| ActivationDate                  | string  |
| PurchaseDate                    | string  |
| PartName                        | string  |
| PartDescription                 | string  |
| IsTaxable                       | boolean |
| IsLimited                       | boolean |
| Quantity                        | number  |
| Discount                        | number  |
| Price                           | number  |
| TimeSpentInMinutes              | number  |
| IsHourlyPricing                 | boolean |
| DeliveryCharge                  | number  |
| SerialNumber                    | string  |
| PartRepairCharges               | number  |
| PartRepairPrice                 | number  |
| OverridePartsTotal              | boolean |
| OverrideRepairsTotal            | boolean |
| AssetCustodianName              | string  |
| AsFoundSpecificationGroupName   | string  |
| AsFoundSpecificationCompanyName | string  |
| AsLeftSpecificationGroupName    | string  |
| AsLeftSpecificationCompanyName  | string  |
| OrderId                         | integer |
| ParentOrderId                   | integer |
| OrderItemId                     | integer |
| OrderItemPartId                 | integer |
| AsFoundSpecificationGroupId     | integer |
| AsLeftSpecificationGroupId      | integer |
| AsFoundStatus                   | integer |
| AsLeftStatus                    | integer |
| AsFoundResult                   | integer |
| AsLeftResult                    | integer |
| CompletedOn                     | string  |
| ReceivedOn                      | string  |
| CompletedByName                 | string  |
| ServiceChargeBase               | number  |
| ServiceTotal                    | number  |
| RepairsTotal                    | number  |
| PartsTotal                      | number  |
| PartsTotalBeforeDiscount        | number  |
| ParentManufacturer              | string  |
| ParentLocation                  | string  |
| ParentManufacturerPartNumber    | string  |
| ParentDisplayPartNumber         | string  |
| ParentAssetId                   | integer |
| ParentCategoryName              | string  |
| ParentRootCategoryName          | string  |
| ParentSerialNumber              | string  |
| ParentAssetTag                  | string  |
| ParentAssetUser                 | string  |
| ParentDisplayName               | string  |
| ParentEquipmentId               | string  |
| AssetShippingAddress1           | string  |
| AssetShippingAddress2           | string  |
| AssetShippingFirstName          | string  |
| AssetShippingLastName           | string  |
| AssetShippingEmail              | string  |
| AssetShippingCompany            | string  |
| AssetShippingCity               | string  |
| AssetShippingZip                | string  |
| AssetShippingPhoneNumber        | string  |
| AssetShippingFaxNumber          | string  |
| AssetShippingCountry            | string  |
| AssetShippingState              | string  |
| ShippingAddress1                | string  |
| ShippingAddress2                | string  |
| ShippingFirstName               | string  |
| ShippingLastName                | string  |
| ShippingEmail                   | string  |
| ShippingCompany                 | string  |
| ShippingCity                    | string  |
| ShippingZip                     | string  |
| ShippingPhoneNumber             | string  |
| ShippingFaxNumber               | string  |
| ShippingCountry                 | string  |
| ShippingState                   | string  |
| AssetServiceNotes               | string  |
| ServiceOptionServiceCode        | string  |

**Group (Tag):**
ReportDatasets

**ODC File:**
[Excel-Qualer-SDK/ReportDatasets/ReportDatasets_GetServiceOrderItemsByServiceOrderItemId.odc](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-odc/blob/main/Excel-Qualer-SDK/ReportDatasets/ReportDatasets_GetServiceOrderItemsByServiceOrderItemId.odc)

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

6. Select `ReportDatasets_GetServiceOrderItemsByServiceOrderItemId.odc` and click `Open`.

> ⚠️ If parameters are needed, you'll see an error now. It's ok, but you'll need to set them.

### Setting parameters
If there are any parameters listed near the top of this file, create a named range with each name listed under **Excel Named Range(s):**
> They're just named ranges, with particular names.
