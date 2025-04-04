# `ServiceOrderParts_GetWorkOrderPartsByServiceOrderId`

**URL Template:**
`GET /api/service/workorders/{serviceOrderId}/parts`

**Parameters:**
- *****`serviceOrderId`: `integer`


> *****Required parameters are marked with an asterisk (*****).

**Excel Named Range(s):**
- `ServiceOrderId`


**Description:**


### Response Schema

#### OK
+-------------------------+---------+
| Field                   | Type    |
+=========================+=========+
| ServiceOrderItemPartId  | integer |
+-------------------------+---------+
| Price                   | number  |
+-------------------------+---------+
| Description             | string  |
+-------------------------+---------+
| Name                    | string  |
+-------------------------+---------+
| UnitName                | string  |
+-------------------------+---------+
| Quantity                | number  |
+-------------------------+---------+
| Discount                | number  |
+-------------------------+---------+
| DeliveryCharge          | number  |
+-------------------------+---------+
| IsTaxable               | boolean |
+-------------------------+---------+
| TimeSpentInMinutes      | number  |
+-------------------------+---------+
| IsHourlyPricing         | boolean |
+-------------------------+---------+
| FreeQuantity            | integer |
+-------------------------+---------+
| CurrencyIsoSymbol       | string  |
+-------------------------+---------+
| CreatedById             | integer |
+-------------------------+---------+
| CreatedBy               | string  |
+-------------------------+---------+
| CreatedOnUtc            | string  |
+-------------------------+---------+
| ChargeDate              | string  |
+-------------------------+---------+
| ContractRepairsDiscount | number  |
+-------------------------+---------+
| ContractPartsDiscount   | number  |
+-------------------------+---------+
| ServiceOrderChargeType  | string  |
+-------------------------+---------+
| TotalDiscount           | number  |
+-------------------------+---------+
| TotalPrice              | number  |
+-------------------------+---------+
| DiscountPrice           | number  |
+-------------------------+---------+

**Group (Tag):**
ServiceOrderParts

**ODC File:**
[Excel-Qualer-SDK/ServiceOrderParts/ServiceOrderParts_GetWorkOrderPartsByServiceOrderId.odc](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-odc/blob/main/Excel-Qualer-SDK/ServiceOrderParts/ServiceOrderParts_GetWorkOrderPartsByServiceOrderId.odc)

---

To Use in Excel:
---

1. Go to the ![`Data`](https://github.com/user-attachments/assets/da437a70-57b3-4c5b-bb01-4910ece19ed1)
 tab.
3. Click ![Existing Connections](https://github.com/user-attachments/assets/a2f1ed67-b2e0-4c23-ac90-68c870e60289)
4. Click ![`Browse for More...`](https://github.com/user-attachments/assets/8e698494-6865-41e7-b6fa-043aea81809a)
5. Paste the following into the URL bar
```
\\jgiquality.sharepoint.com@SSL\sites\JGI\Shared Documents\General\Excel-Qualer-SDK\ServiceOrderParts\
```

![image](https://github.com/user-attachments/assets/1e1a8d87-0377-446d-aaf5-d78562991db3)

6. Select `ServiceOrderParts_GetWorkOrderPartsByServiceOrderId.odc` and click `Open`.

> ⚠️ If parameters are needed, you'll see an error now. It's ok, but you'll need to set them.

### Setting parameters
If there are any parameters listed near the top of this file, create a named range with each name listed under **Excel Named Range(s):**
> They're just named ranges, with particular names.
