# `Company_LookupsByLookupType`

**URL Template:**
`GET /api/company/lookups`

**Parameters:**
- *****`lookupType`: `string`


> *****Required parameters are marked with an asterisk (*****).

**Excel Named Range(s):**
- `LookupType`


**Description:**
lookupName:
AssetClass = 1
AssetCriticality = 2
AssetCondition = 3
InventoryCategory = 4
InventoryUnit = 5
OrderItemInProgressWorkStatus = 6
OrderItemDelayWorkStatus = 7
OrderItemWithdrawnWorkStatus = 8
OrderItemCompletedWorkStatus = 9
OrderDelayedStatus = 10
ClientInvoicing = 11
ClientStanding = 12
ClientCategory = 13
CancelOrderReasons = 14
OrderItemLockedWorkStatus = 15

### Response Schema

#### OK
+---------+-----------------+
| Field   | Type            |
+=========+=================+
|         | array of string |
+---------+-----------------+

**Group (Tag):**
Company

**ODC File:**
[Excel-Qualer-SDK/Company/Company_LookupsByLookupType.odc](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-odc/blob/main/Excel-Qualer-SDK/Company/Company_LookupsByLookupType.odc)

---

To Use in Excel:
---

1. Go to the ![`Data`](https://github.com/user-attachments/assets/da437a70-57b3-4c5b-bb01-4910ece19ed1)
 tab.
3. Click ![Existing Connections](https://github.com/user-attachments/assets/a2f1ed67-b2e0-4c23-ac90-68c870e60289)
4. Click ![`Browse for More...`](https://github.com/user-attachments/assets/8e698494-6865-41e7-b6fa-043aea81809a)
5. Paste the following into the URL bar
```
\\jgiquality.sharepoint.com@SSL\sites\JGI\Shared Documents\General\Excel-Qualer-SDK\Company\
```

![image](https://github.com/user-attachments/assets/1e1a8d87-0377-446d-aaf5-d78562991db3)

6. Select `Company_LookupsByLookupType.odc` and click `Open`.

> ⚠️ If parameters are needed, you'll see an error now. It's ok, but you'll need to set them.

### Setting parameters
If there are any parameters listed near the top of this file, create a named range with each name listed under **Excel Named Range(s):**
> They're just named ranges, with particular names.
