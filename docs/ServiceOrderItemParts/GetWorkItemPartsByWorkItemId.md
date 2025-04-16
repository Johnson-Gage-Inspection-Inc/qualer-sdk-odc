# `ServiceOrderItemParts_GetWorkItemPartsByWorkItemId`
> 

**URL Template:**
`GET /api/service/workitems/{workItemId}/parts`

**Parameters (Named Ranges):**

> *Required parameters are bolded.*

| Name           | Type    | Format   |
|:---------------|:--------|:---------|
| **WorkItemId** | integer | int32    |

**Description:**
No description provided.

### Response Schema

#### OK [200]

| Field                  | Type    |
|:-----------------------|:--------|
| ServiceOrderItemPartId | integer |
| ServiceOrderItemId     | integer |
| Name                   | string  |
| Description            | string  |
| Discount               | number  |
| IsTaxable              | boolean |
| IsHourlyPricing        | boolean |
| Price                  | number  |
| UnitName               | string  |
| Quantity               | number  |
| DeliveryCharge         | number  |
| TimeSpentInMinutes     | number  |
| FreeQuantity           | integer |
| ServiceOrderChargeType | string  |

**Group (Tag):**
ServiceOrderItemParts

**ODC File:**
[Excel-Qualer-SDK/ServiceOrderItemParts/ServiceOrderItemParts_GetWorkItemPartsByWorkItemId.odc](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-odc/blob/main/Excel-Qualer-SDK/ServiceOrderItemParts/ServiceOrderItemParts_GetWorkItemPartsByWorkItemId.odc)

---

To Use in Excel:
---

1. Go to the ![`Data`](https://github.com/user-attachments/assets/da437a70-57b3-4c5b-bb01-4910ece19ed1)
 tab.
3. Click ![Existing Connections](https://github.com/user-attachments/assets/a2f1ed67-b2e0-4c23-ac90-68c870e60289)
4. Click ![`Browse for More...`](https://github.com/user-attachments/assets/8e698494-6865-41e7-b6fa-043aea81809a)
5. Paste the following into the URL bar
```
\\jgiquality.sharepoint.com@SSL\sites\JGI\Shared Documents\General\Excel-Qualer-SDK\ServiceOrderItemParts\
```

![image](https://github.com/user-attachments/assets/1e1a8d87-0377-446d-aaf5-d78562991db3)

6. Select `ServiceOrderItemParts_GetWorkItemPartsByWorkItemId.odc` and click `Open`.

> ⚠️ If parameters are needed, you'll see an error now. It's ok, but you'll need to set them.

### Setting parameters
If there are any parameters listed near the top of this file, create a named range with each name listed under **Excel Named Range(s):**
> They're just named ranges, with particular names.
