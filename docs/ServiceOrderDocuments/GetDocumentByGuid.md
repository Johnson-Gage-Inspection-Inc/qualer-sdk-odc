# `ServiceOrderDocuments_GetDocumentByGuid`
> Retrieve work order document by Unique Id

**URL Template:**
`GET /api/wd/{guid}`

**Parameters (Named Ranges):**

> *Required parameters are bolded.*

| Name     | Description        | Type   | Format   |
|:---------|:-------------------|:-------|:---------|
| **Guid** | Document unique id | string | uuid     |

**Description:**
Sample request:
            
GET api/service/workorders/documents/FE6B21DC-8061-46FF-AAB8-12C2030FE4B9
            
GET api/wd/FE6B21DC-8061-46FF-AAB8-12C2030FE4B9

### Response Schema

#### OK [200]



**Group (Tag):**
ServiceOrderDocuments

**ODC File:**
[Excel-Qualer-SDK/ServiceOrderDocuments/ServiceOrderDocuments_GetDocumentByGuid.odc](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-odc/blob/main/Excel-Qualer-SDK/ServiceOrderDocuments/ServiceOrderDocuments_GetDocumentByGuid.odc)

---

To Use in Excel:
---

1. Go to the ![`Data`](https://github.com/user-attachments/assets/da437a70-57b3-4c5b-bb01-4910ece19ed1)
 tab.
3. Click ![Existing Connections](https://github.com/user-attachments/assets/a2f1ed67-b2e0-4c23-ac90-68c870e60289)
4. Click ![`Browse for More...`](https://github.com/user-attachments/assets/8e698494-6865-41e7-b6fa-043aea81809a)
5. Paste the following into the URL bar
```
\\jgiquality.sharepoint.com@SSL\sites\JGI\Shared Documents\General\Excel-Qualer-SDK\ServiceOrderDocuments\
```

![image](https://github.com/user-attachments/assets/1e1a8d87-0377-446d-aaf5-d78562991db3)

6. Select `ServiceOrderDocuments_GetDocumentByGuid.odc` and click `Open`.

> ⚠️ If parameters are needed, you'll see an error now. It's ok, but you'll need to set them.

### Setting parameters
If there are any parameters listed near the top of this file, create a named range with each name listed under **Excel Named Range(s):**
> They're just named ranges, with particular names.
