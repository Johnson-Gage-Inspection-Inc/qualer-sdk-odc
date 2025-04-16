# `ServiceOrders_GetChargesByServiceOrderId`
> 

**URL Template:**
`GET /api/service/workorders/{serviceOrderId}/charges`

**Parameters (Named Ranges):**

> *Required parameters are bolded.*

| Name               | Type    | Format   |
|:-------------------|:--------|:---------|
| **ServiceOrderId** | integer | int32    |

**Description:**
No description provided.

### Response Schema

#### OK [200]

| Field                                | Type    |
|:-------------------------------------|:--------|
| Charges.Name                         | string  |
| Charges.Price                        | number  |
| Tasks.ContractDiscount               | number  |
| Tasks.TimeSpent                      | number  |
| Tasks.IsHourly                       | boolean |
| Tasks.Details                        | string  |
| Tasks.Name                           | string  |
| Tasks.Price                          | number  |
| Parts.DeliveryCharge                 | number  |
| Parts.Quantity                       | number  |
| Parts.TimeSpentInMinutes             | number  |
| Parts.IsHourlyPricing                | boolean |
| Parts.Description                    | string  |
| Parts.Name                           | string  |
| Parts.Price                          | number  |
| Parts.IsTaxable                      | boolean |
| Repairs.DeliveryCharge               | number  |
| Repairs.Quantity                     | number  |
| Repairs.TimeSpentInMinutes           | number  |
| Repairs.IsHourlyPricing              | boolean |
| Repairs.Description                  | string  |
| Repairs.Name                         | string  |
| Repairs.Price                        | number  |
| Repairs.IsTaxable                    | boolean |
| WorkItems.Tasks.ContractDiscount     | number  |
| WorkItems.Tasks.Name                 | string  |
| WorkItems.Tasks.Price                | number  |
| WorkItems.Parts.DeliveryCharge       | number  |
| WorkItems.Parts.Quantity             | number  |
| WorkItems.Parts.TimeSpentInMinutes   | number  |
| WorkItems.Parts.IsHourlyPricing      | boolean |
| WorkItems.Parts.Description          | string  |
| WorkItems.Parts.Name                 | string  |
| WorkItems.Parts.Price                | number  |
| WorkItems.Parts.UnitName             | string  |
| WorkItems.Parts.IsTaxable            | boolean |
| WorkItems.Repairs.DeliveryCharge     | number  |
| WorkItems.Repairs.Quantity           | number  |
| WorkItems.Repairs.TimeSpentInMinutes | number  |
| WorkItems.Repairs.IsHourlyPricing    | boolean |
| WorkItems.Repairs.Description        | string  |
| WorkItems.Repairs.Name               | string  |
| WorkItems.Repairs.Price              | number  |
| WorkItems.Repairs.UnitName           | string  |
| WorkItems.Repairs.IsTaxable          | boolean |
| WorkItems.WorkItemId                 | integer |
| WorkItems.VendorTag                  | string  |

**Group (Tag):**
ServiceOrders

**ODC File:**
[Excel-Qualer-SDK/ServiceOrders/ServiceOrders_GetChargesByServiceOrderId.odc](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-odc/blob/main/Excel-Qualer-SDK/ServiceOrders/ServiceOrders_GetChargesByServiceOrderId.odc)

---

To Use in Excel:
---

1. Go to the ![`Data`](https://github.com/user-attachments/assets/da437a70-57b3-4c5b-bb01-4910ece19ed1)
 tab.
3. Click ![Existing Connections](https://github.com/user-attachments/assets/a2f1ed67-b2e0-4c23-ac90-68c870e60289)
4. Click ![`Browse for More...`](https://github.com/user-attachments/assets/8e698494-6865-41e7-b6fa-043aea81809a)
5. Paste the following into the URL bar
```
\\jgiquality.sharepoint.com@SSL\sites\JGI\Shared Documents\General\Excel-Qualer-SDK\ServiceOrders\
```

![image](https://github.com/user-attachments/assets/1e1a8d87-0377-446d-aaf5-d78562991db3)

6. Select `ServiceOrders_GetChargesByServiceOrderId.odc` and click `Open`.

> ⚠️ If parameters are needed, you'll see an error now. It's ok, but you'll need to set them.

### Setting parameters
If there are any parameters listed near the top of this file, create a named range with each name listed under **Excel Named Range(s):**
> They're just named ranges, with particular names.
