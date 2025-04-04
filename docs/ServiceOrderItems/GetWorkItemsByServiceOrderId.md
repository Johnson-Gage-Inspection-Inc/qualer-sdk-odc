# `ServiceOrderItems_GetWorkItemsByServiceOrderId`

**URL Template:**
`GET /api/service/workorders/{serviceOrderId}/workitems`

**Parameters:**
- *`serviceOrderId`: `integer`


> *Required parameters are marked with an asterisk (*).

**Excel Named Range(s):**
- `ServiceOrderId`


**Description:**
No description provided.

### Response Schema

#### OK [200]

| Field                          | Type    |
|:-------------------------------|:--------|
| WorkItemId                     | integer |
| ClientNotes                    | string  |
| ServiceComments                | string  |
| PrivateComments                | string  |
| OrderItemNumber                | integer |
| ServiceOrderId                 | integer |
| ChannelCount                   | integer |
| ServiceTotal                   | number  |
| RepairsTotal                   | number  |
| PartsTotal                     | number  |
| PartsTotalBeforeDiscount       | number  |
| OverrideServiceTotal           | boolean |
| OverrideRepairsTotal           | boolean |
| OverridePartsTotal             | boolean |
| ServiceType                    | string  |
| DocumentNumber                 | string  |
| DocumentSection                | string  |
| WorkStatus                     | string  |
| CustomWorkStatus               | string  |
| IsLimited                      | boolean |
| CheckedOn                      | string  |
| CheckedByName                  | string  |
| CheckedById                    | integer |
| CompletedOn                    | string  |
| CompletedByName                | string  |
| CompletedById                  | integer |
| UpdatedById                    | integer |
| UpdatedBy                      | string  |
| AsFoundCheck                   | string  |
| AsLeftCheck                    | string  |
| ItemResultStatus               | string  |
| ItemAsFoundResult              | string  |
| ItemAsLeftResult               | string  |
| AsFoundSpecification           | integer |
| AsLeftSpecification            | integer |
| CreatedOnUtc                   | string  |
| UpdatedOnUtc                   | string  |
| EquipmentId                    | string  |
| ServiceLevel                   | string  |
| ServiceLevelCode               | string  |
| ServiceLevelDocumentNumber     | string  |
| ServiceLevelDocumentSection    | string  |
| NextServiceLevel               | string  |
| NextServiceLevelCode           | string  |
| ResultStatus                   | string  |
| AsFoundResult                  | string  |
| AsLeftResult                   | string  |
| SerialNumber                   | string  |
| SerialNumberChange             | string  |
| AssetTag                       | string  |
| AssetUser                      | string  |
| AssetTagChange                 | string  |
| AssetUserChange                | string  |
| AssetId                        | integer |
| AssetName                      | string  |
| AssetDescription               | string  |
| AssetSiteName                  | string  |
| AssetSiteId                    | integer |
| AssetCompanyName               | string  |
| AssetCompanyId                 | integer |
| ClientCompanyId                | integer |
| VendorCompanyId                | integer |
| ServiceNotes                   | string  |
| ProviderTechnician             | string  |
| ProviderPhone                  | string  |
| ProviderCompany                | string  |
| ServiceCharge                  | number  |
| RepairsCharge                  | number  |
| PartsCharge                    | number  |
| PartsChargeBeforeDiscount      | number  |
| CustomOrderNumber              | string  |
| CertificateNumber              | string  |
| ServiceDate                    | string  |
| DueDate                        | string  |
| NextServiceDate                | string  |
| MaintenanceTask                | string  |
| MaintenancePlan                | string  |
| ServiceOptions.Name            | string  |
| ServiceOptions.Price           | number  |
| ServiceOptions.ServiceCharge   | number  |
| ServiceOptions.TimeSpent       | number  |
| ServiceOptions.IsHourly        | boolean |
| ServiceOptions.DocumentNumber  | string  |
| ServiceOptions.DocumentSection | string  |
| ServiceOptions.ServiceCode     | string  |
| VendorTag                      | string  |
| LegacyId                       | string  |
| AssetOwnership                 | string  |

**Group (Tag):**
ServiceOrderItems

**ODC File:**
[Excel-Qualer-SDK/ServiceOrderItems/ServiceOrderItems_GetWorkItemsByServiceOrderId.odc](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-odc/blob/main/Excel-Qualer-SDK/ServiceOrderItems/ServiceOrderItems_GetWorkItemsByServiceOrderId.odc)

---

To Use in Excel:
---

1. Go to the ![`Data`](https://github.com/user-attachments/assets/da437a70-57b3-4c5b-bb01-4910ece19ed1)
 tab.
3. Click ![Existing Connections](https://github.com/user-attachments/assets/a2f1ed67-b2e0-4c23-ac90-68c870e60289)
4. Click ![`Browse for More...`](https://github.com/user-attachments/assets/8e698494-6865-41e7-b6fa-043aea81809a)
5. Paste the following into the URL bar
```
\\jgiquality.sharepoint.com@SSL\sites\JGI\Shared Documents\General\Excel-Qualer-SDK\ServiceOrderItems\
```

![image](https://github.com/user-attachments/assets/1e1a8d87-0377-446d-aaf5-d78562991db3)

6. Select `ServiceOrderItems_GetWorkItemsByServiceOrderId.odc` and click `Open`.

> ⚠️ If parameters are needed, you'll see an error now. It's ok, but you'll need to set them.

### Setting parameters
If there are any parameters listed near the top of this file, create a named range with each name listed under **Excel Named Range(s):**
> They're just named ranges, with particular names.
