# `EmployeePreference_GetByElementPage`

**URL Template:**
`GET /api/user/preferences/{elementPage}`

**Parameters:**
- *`elementPage`: `string`


> *Required parameters are marked with an asterisk (*).

**Excel Named Range(s):**
- `ElementPage`


**Description:**
elementPage:
AssetManager = 1,
WorkOrders = 2,
ServiceOrderItems = 3,
ServiceSchedules = 4,
ServiceRequests = 5,
Vendors = 6,
VendorAgreements = 7,
ClientAgreements = 8,
WorkCalendar = 9,
Clients = 10,
GlobalAssetManager = 11,
InvoicesManager = 12,
ProductManager = 13,
ProductSpecifications = 14,
DocumentManager = 15

### Response Schema

#### OK

+-------------+-----------------+
| Field       | Type            |
+=============+=================+
| ElementType | string          |
+-------------+-----------------+
| ElementPage | string          |
+-------------+-----------------+
| ElementId   | string          |
+-------------+-----------------+
| Preference  | array of string |
+-------------+-----------------+
| IsPinned    | boolean         |
+-------------+-----------------+

**Group (Tag):**
EmployeePreference

**ODC File:**
[Excel-Qualer-SDK/EmployeePreference/EmployeePreference_GetByElementPage.odc](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-odc/blob/main/Excel-Qualer-SDK/EmployeePreference/EmployeePreference_GetByElementPage.odc)

---

To Use in Excel:
---

1. Go to the ![`Data`](https://github.com/user-attachments/assets/da437a70-57b3-4c5b-bb01-4910ece19ed1)
 tab.
3. Click ![Existing Connections](https://github.com/user-attachments/assets/a2f1ed67-b2e0-4c23-ac90-68c870e60289)
4. Click ![`Browse for More...`](https://github.com/user-attachments/assets/8e698494-6865-41e7-b6fa-043aea81809a)
5. Paste the following into the URL bar
```
\\jgiquality.sharepoint.com@SSL\sites\JGI\Shared Documents\General\Excel-Qualer-SDK\EmployeePreference\
```

![image](https://github.com/user-attachments/assets/1e1a8d87-0377-446d-aaf5-d78562991db3)

6. Select `EmployeePreference_GetByElementPage.odc` and click `Open`.

> ⚠️ If parameters are needed, you'll see an error now. It's ok, but you'll need to set them.

### Setting parameters
If there are any parameters listed near the top of this file, create a named range with each name listed under **Excel Named Range(s):**
> They're just named ranges, with particular names.
