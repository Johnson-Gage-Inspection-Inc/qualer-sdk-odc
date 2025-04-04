# `ServiceOrders_GetWorkOrdersByEmployeeId`

**URL Template:**
`GET /api/employee/{employeeId}/workorders`

**Parameters:**
- *`employeeId`: `integer`
- `isInternal`: `boolean`


> *Required parameters are marked with an asterisk (*).

**Excel Named Range(s):**
- `EmployeeId`
- `IsInternal`


**Description:**
No description provided.

### Response Schema

#### OK
+------------------------+---------+
| Field                  | Type    |
+========================+=========+
| ServiceOrderId         | integer |
+------------------------+---------+
| Guid                   | string  |
+------------------------+---------+
| ServiceOrderNumber     | integer |
+------------------------+---------+
| CustomOrderNumber      | string  |
+------------------------+---------+
| DueDate                | string  |
+------------------------+---------+
| Assets                 | integer |
+------------------------+---------+
| CompletedAssets        | integer |
+------------------------+---------+
| OrderStatus            | string  |
+------------------------+---------+
| IsQualityControlFail   | boolean |
+------------------------+---------+
| ServicePrivateComments | string  |
+------------------------+---------+
| ClientCompanyId        | integer |
+------------------------+---------+
| ClientCompanyName      | string  |
+------------------------+---------+
| ClientSiteName         | string  |
+------------------------+---------+
| ClientLegacyId         | string  |
+------------------------+---------+
| BusinessFromTime       | string  |
+------------------------+---------+
| BusinessToTime         | string  |
+------------------------+---------+
| Timeframe              | string  |
+------------------------+---------+
| SiteAccessNotes        | string  |
+------------------------+---------+
| DesiredDate            | string  |
+------------------------+---------+
| DeadlineDate           | string  |
+------------------------+---------+
| RequestFromDate        | string  |
+------------------------+---------+
| RequestFromTime        | string  |
+------------------------+---------+
| RequestToDate          | string  |
+------------------------+---------+
| RequestToTime          | string  |
+------------------------+---------+

**Group (Tag):**
ServiceOrders

**ODC File:**
[Excel-Qualer-SDK/ServiceOrders/ServiceOrders_GetWorkOrdersByEmployeeId.odc](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-odc/blob/main/Excel-Qualer-SDK/ServiceOrders/ServiceOrders_GetWorkOrdersByEmployeeId.odc)

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

6. Select `ServiceOrders_GetWorkOrdersByEmployeeId.odc` and click `Open`.

> ⚠️ If parameters are needed, you'll see an error now. It's ok, but you'll need to set them.

### Setting parameters
If there are any parameters listed near the top of this file, create a named range with each name listed under **Excel Named Range(s):**
> They're just named ranges, with particular names.
