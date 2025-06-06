# `ServiceOrderItemDocuments_GetDocumentListByFrom`
> Retrieve work order documents

**URL Template:**
`GET /api/service/workitems/documents/list`

**Parameters (Named Ranges):**

> *Required parameters are bolded.*

| Name               | Description                                                       | Type    | Format    |
|:-------------------|:------------------------------------------------------------------|:--------|:----------|
| **From**           | Retrieve documents where CreatedOnUtc greater than From parameter | string  | date-time |
| **To**             | Retrieve documents where CreatedOnUtc less than To parameter      | string  | date-time |
| ReportType         | Retrieve documents given types (Optional)                         | string  | string    |
| ServiceOrderItemId | Retrieve documents by given service order item id (Optional)      | integer | int32     |

**Description:**
Sample request:
            
GET /api/service/workitems/documents/list
            
GET /api/service/workitems/documents/list?status=reportType
            
GET /api/service/workitems/documents/list?from=2020-12-01T10:11:12&amp;to=2021-01-01T10:11:12&amp;reportType=OrderInvoice&amp;ServiceOrderItemId=1
            
reportType:<br />
Unset = 0,<br />
AssetSummary = 1,<br />
AssetLabel = 11,<br />
AssetDetail = 2,<br />
AssetCertificate = 21,<br />
OrderSummary / ServiceOrderSummary = 3,<br />
OrderInvoice / ServiceOrderInvoice = 31,<br />
OrderEstimate / ServiceOrderEstimate = 32,<br />
Dashboard = 4,<br />
OrderDetail / ServiceOrderDetail = 5,<br />
OrderCertificate / ServiceOrderCertificate = 5<br />

### Response Schema

#### OK [200]

| Field              | Type    |
|:-------------------|:--------|
| ServiceOrderId     | integer |
| ServiceOrderItemId | integer |
| Guid               | string  |
| DocumentName       | string  |
| FileName           | string  |
| DocumentType       | string  |
| RevisionNumber     | integer |
| ReportType         | string  |
| DownloadUrl        | string  |

**Group (Tag):**
ServiceOrderItemDocuments

**ODC File:**
[Excel-Qualer-SDK/ServiceOrderItemDocuments/ServiceOrderItemDocuments_GetDocumentListByFrom.odc](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-odc/blob/main/Excel-Qualer-SDK/ServiceOrderItemDocuments/ServiceOrderItemDocuments_GetDocumentListByFrom.odc)

---

To Use in Excel:
---

1. Go to the ![`Data`](https://github.com/user-attachments/assets/da437a70-57b3-4c5b-bb01-4910ece19ed1)
 tab.
3. Click ![Existing Connections](https://github.com/user-attachments/assets/a2f1ed67-b2e0-4c23-ac90-68c870e60289)
4. Click ![`Browse for More...`](https://github.com/user-attachments/assets/8e698494-6865-41e7-b6fa-043aea81809a)
5. Paste the following into the URL bar
```
\\jgiquality.sharepoint.com@SSL\sites\JGI\Shared Documents\General\Excel-Qualer-SDK\ServiceOrderItemDocuments\
```

![image](https://github.com/user-attachments/assets/1e1a8d87-0377-446d-aaf5-d78562991db3)

6. Select `ServiceOrderItemDocuments_GetDocumentListByFrom.odc` and click `Open`.

> ⚠️ If parameters are needed, you'll see an error now. It's ok, but you'll need to set them.

### Setting parameters
If there are any parameters listed near the top of this file, create a named range with each name listed under **Excel Named Range(s):**
> They're just named ranges, with particular names.
