# `ServiceOrderDocuments_GetDocumentList`

**URL Template:**  
`GET /api/service/workorders/documents/list`

**Parameters:**  
None

**Excel Named Range(s):**  
None

**Description:**  
Sample request:
            
GET /api/service/workorders/documents/list
            
GET /api/service/workorders/documents/list?status=reportType
            
GET /api/service/workorders/documents/list?from=2020-12-01T10:11:12&amp;to=2021-01-01T10:11:12&amp;reportType=OrderInvoice&amp;ServiceOrderId=1
            
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

**Group (Tag):**  
ServiceOrderDocuments

**ODC File:**  
[Excel-Qualer-SDK/ServiceOrderDocuments/ServiceOrderDocuments_GetDocumentList.odc](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-odc/blob/main/Excel-Qualer-SDK/ServiceOrderDocuments/ServiceOrderDocuments_GetDocumentList.odc)
