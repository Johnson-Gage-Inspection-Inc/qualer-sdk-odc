# `ClientSite_GetClientSitesByClientCompanyId`

**URL Template:**
`GET /api/service/clients/{clientCompanyId}/sites`

**Parameters:**
- *****`clientCompanyId`: `integer`


> *****Required parameters are marked with an asterisk (*****).

**Excel Named Range(s):**
- `ClientCompanyId`


**Description:**
No description provided.

### Response Schema

#### OK
+-------------------------------------------+---------+
| Field                                     | Type    |
+===========================================+=========+
| SiteId                                    | integer |
+-------------------------------------------+---------+
| SiteName                                  | string  |
+-------------------------------------------+---------+
| SiteCode                                  | string  |
+-------------------------------------------+---------+
| ShippingAddress.FirstName                 | string  |
+-------------------------------------------+---------+
| ShippingAddress.LastName                  | string  |
+-------------------------------------------+---------+
| ShippingAddress.Email                     | string  |
+-------------------------------------------+---------+
| ShippingAddress.Company                   | string  |
+-------------------------------------------+---------+
| ShippingAddress.City                      | string  |
+-------------------------------------------+---------+
| ShippingAddress.Address1                  | string  |
+-------------------------------------------+---------+
| ShippingAddress.Address2                  | string  |
+-------------------------------------------+---------+
| ShippingAddress.ZipPostalCode             | string  |
+-------------------------------------------+---------+
| ShippingAddress.PhoneNumber               | string  |
+-------------------------------------------+---------+
| ShippingAddress.FaxNumber                 | string  |
+-------------------------------------------+---------+
| ShippingAddress.Attention1                | string  |
+-------------------------------------------+---------+
| ShippingAddress.Attention2                | string  |
+-------------------------------------------+---------+
| ShippingAddress.Country                   | string  |
+-------------------------------------------+---------+
| ShippingAddress.StateProvince             | string  |
+-------------------------------------------+---------+
| ShippingAddress.StateProvinceAbbreviation | string  |
+-------------------------------------------+---------+
| ShippingInherited                         | boolean |
+-------------------------------------------+---------+
| BillingAddress.FirstName                  | string  |
+-------------------------------------------+---------+
| BillingAddress.LastName                   | string  |
+-------------------------------------------+---------+
| BillingAddress.Email                      | string  |
+-------------------------------------------+---------+
| BillingAddress.Company                    | string  |
+-------------------------------------------+---------+
| BillingAddress.City                       | string  |
+-------------------------------------------+---------+
| BillingAddress.Address1                   | string  |
+-------------------------------------------+---------+
| BillingAddress.Address2                   | string  |
+-------------------------------------------+---------+
| BillingAddress.ZipPostalCode              | string  |
+-------------------------------------------+---------+
| BillingAddress.PhoneNumber                | string  |
+-------------------------------------------+---------+
| BillingAddress.FaxNumber                  | string  |
+-------------------------------------------+---------+
| BillingAddress.Attention1                 | string  |
+-------------------------------------------+---------+
| BillingAddress.Attention2                 | string  |
+-------------------------------------------+---------+
| BillingAddress.Country                    | string  |
+-------------------------------------------+---------+
| BillingAddress.StateProvince              | string  |
+-------------------------------------------+---------+
| BillingAddress.StateProvinceAbbreviation  | string  |
+-------------------------------------------+---------+
| DefaultAccountRepresentativeEmployeeId    | integer |
+-------------------------------------------+---------+
| BillingInherited                          | boolean |
+-------------------------------------------+---------+
| FederalNumber                             | string  |
+-------------------------------------------+---------+
| StateNumber                               | string  |
+-------------------------------------------+---------+
| CultureName                               | string  |
+-------------------------------------------+---------+
| IsScienceFacility                         | boolean |
+-------------------------------------------+---------+
| IsServiceCenter                           | boolean |
+-------------------------------------------+---------+
| IsInventoryStorage                        | boolean |
+-------------------------------------------+---------+
| IsProduction                              | boolean |
+-------------------------------------------+---------+
| TimeZoneId                                | string  |
+-------------------------------------------+---------+
| TimeZoneOffsetMinutes                     | integer |
+-------------------------------------------+---------+
| UpdatedOnUtc                              | string  |
+-------------------------------------------+---------+
| Attributes.Name                           | string  |
+-------------------------------------------+---------+
| Attributes.Value                          | string  |
+-------------------------------------------+---------+

**Group (Tag):**
ClientSite

**ODC File:**
[Excel-Qualer-SDK/ClientSite/ClientSite_GetClientSitesByClientCompanyId.odc](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-odc/blob/main/Excel-Qualer-SDK/ClientSite/ClientSite_GetClientSitesByClientCompanyId.odc)

---

To Use in Excel:
---

1. Go to the ![`Data`](https://github.com/user-attachments/assets/da437a70-57b3-4c5b-bb01-4910ece19ed1)
 tab.
3. Click ![Existing Connections](https://github.com/user-attachments/assets/a2f1ed67-b2e0-4c23-ac90-68c870e60289)
4. Click ![`Browse for More...`](https://github.com/user-attachments/assets/8e698494-6865-41e7-b6fa-043aea81809a)
5. Paste the following into the URL bar
```
\\jgiquality.sharepoint.com@SSL\sites\JGI\Shared Documents\General\Excel-Qualer-SDK\ClientSite\
```

![image](https://github.com/user-attachments/assets/1e1a8d87-0377-446d-aaf5-d78562991db3)

6. Select `ClientSite_GetClientSitesByClientCompanyId.odc` and click `Open`.

> ⚠️ If parameters are needed, you'll see an error now. It's ok, but you'll need to set them.

### Setting parameters
If there are any parameters listed near the top of this file, create a named range with each name listed under **Excel Named Range(s):**
> They're just named ranges, with particular names.
