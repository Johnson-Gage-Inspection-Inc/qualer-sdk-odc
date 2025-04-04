# `Product_GetProductByProductId`

**URL Template:**
`GET /api/products/{productId}`

**Parameters:**
- *`productId`: `integer`


> *Required parameters are marked with an asterisk (*).

**Excel Named Range(s):**
- `ProductId`


**Description:**
No description provided.

### Response Schema

#### OK

+------------------------+---------+
| Field                  | Type    |
+========================+=========+
| ProductId              | integer |
+------------------------+---------+
| ParentProductId        | integer |
+------------------------+---------+
| CategoryId             | integer |
+------------------------+---------+
| ManufacturerId         | integer |
+------------------------+---------+
| ManufacturerName       | string  |
+------------------------+---------+
| ProductName            | string  |
+------------------------+---------+
| ParentProductName      | string  |
+------------------------+---------+
| ManufacturerPartNumber | string  |
+------------------------+---------+
| ProductDescription     | string  |
+------------------------+---------+
| IsFamily               | boolean |
+------------------------+---------+
| IsDiscontinued         | boolean |
+------------------------+---------+
| IsStockItem            | boolean |
+------------------------+---------+
| UnitSalePrice          | number  |
+------------------------+---------+
| SupplierInformation    | string  |
+------------------------+---------+
| QuantityOnHand         | integer |
+------------------------+---------+
| ProductCode            | string  |
+------------------------+---------+
| CategoryName           | string  |
+------------------------+---------+
| ParentCategoryName     | string  |
+------------------------+---------+

**Group (Tag):**
Product

**ODC File:**
[Excel-Qualer-SDK/Product/Product_GetProductByProductId.odc](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-odc/blob/main/Excel-Qualer-SDK/Product/Product_GetProductByProductId.odc)

---

To Use in Excel:
---

1. Go to the ![`Data`](https://github.com/user-attachments/assets/da437a70-57b3-4c5b-bb01-4910ece19ed1)
 tab.
3. Click ![Existing Connections](https://github.com/user-attachments/assets/a2f1ed67-b2e0-4c23-ac90-68c870e60289)
4. Click ![`Browse for More...`](https://github.com/user-attachments/assets/8e698494-6865-41e7-b6fa-043aea81809a)
5. Paste the following into the URL bar
```
\\jgiquality.sharepoint.com@SSL\sites\JGI\Shared Documents\General\Excel-Qualer-SDK\Product\
```

![image](https://github.com/user-attachments/assets/1e1a8d87-0377-446d-aaf5-d78562991db3)

6. Select `Product_GetProductByProductId.odc` and click `Open`.

> ⚠️ If parameters are needed, you'll see an error now. It's ok, but you'll need to set them.

### Setting parameters
If there are any parameters listed near the top of this file, create a named range with each name listed under **Excel Named Range(s):**
> They're just named ranges, with particular names.
