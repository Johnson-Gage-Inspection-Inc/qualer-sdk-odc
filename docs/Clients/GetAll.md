# `Clients_GetAll`
> 

**URL Template:**
`GET /api/service/clients`

**Parameters (Named Ranges):**

> *Required parameters are bolded.*

| Name                    | Type    | Format    |
|:------------------------|:--------|:----------|
| Model.legacyId          | string  | string    |
| Model.accountNumberText | string  | string    |
| Model.companyName       | string  | string    |
| Model.take              | integer | int32     |
| Model.modifiedAfter     | string  | date-time |

**Description:**
No description provided.

### Response Schema

#### OK [200]

| Field                                     | Type    |
|:------------------------------------------|:--------|
| CompanyId                                 | integer |
| AccountNumberText                         | string  |
| AccountNumber                             | integer |
| CurrencyId                                | integer |
| ClientStatus                              | string  |
| CompanyName                               | string  |
| CompanyDescription                        | string  |
| DomainName                                | string  |
| CustomClientName                          | string  |
| LegacyId                                  | string  |
| UpdatedOnUtc                              | string  |
| AccountRepresentativeEmployeeId           | integer |
| AccountRepresentativeSiteId               | integer |
| AccountManagerEmployeeId                  | integer |
| BillingAddress.FirstName                  | string  |
| BillingAddress.LastName                   | string  |
| BillingAddress.Email                      | string  |
| BillingAddress.Company                    | string  |
| BillingAddress.City                       | string  |
| BillingAddress.Address1                   | string  |
| BillingAddress.Address2                   | string  |
| BillingAddress.ZipPostalCode              | string  |
| BillingAddress.PhoneNumber                | string  |
| BillingAddress.FaxNumber                  | string  |
| BillingAddress.Attention1                 | string  |
| BillingAddress.Attention2                 | string  |
| BillingAddress.Country                    | string  |
| BillingAddress.StateProvince              | string  |
| BillingAddress.StateProvinceAbbreviation  | string  |
| ShippingAddress.FirstName                 | string  |
| ShippingAddress.LastName                  | string  |
| ShippingAddress.Email                     | string  |
| ShippingAddress.Company                   | string  |
| ShippingAddress.City                      | string  |
| ShippingAddress.Address1                  | string  |
| ShippingAddress.Address2                  | string  |
| ShippingAddress.ZipPostalCode             | string  |
| ShippingAddress.PhoneNumber               | string  |
| ShippingAddress.FaxNumber                 | string  |
| ShippingAddress.Attention1                | string  |
| ShippingAddress.Attention2                | string  |
| ShippingAddress.Country                   | string  |
| ShippingAddress.StateProvince             | string  |
| ShippingAddress.StateProvinceAbbreviation | string  |
| Attributes.Name                           | string  |
| Attributes.Value                          | string  |

**Group (Tag):**
Clients

**ODC File:**
[Excel-Qualer-SDK/Clients/Clients_GetAll.odc](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-odc/blob/main/Excel-Qualer-SDK/Clients/Clients_GetAll.odc)

---

To Use in Excel:
---

1. Go to the ![`Data`](https://github.com/user-attachments/assets/da437a70-57b3-4c5b-bb01-4910ece19ed1)
 tab.
3. Click ![Existing Connections](https://github.com/user-attachments/assets/a2f1ed67-b2e0-4c23-ac90-68c870e60289)
4. Click ![`Browse for More...`](https://github.com/user-attachments/assets/8e698494-6865-41e7-b6fa-043aea81809a)
5. Paste the following into the URL bar
```
\\jgiquality.sharepoint.com@SSL\sites\JGI\Shared Documents\General\Excel-Qualer-SDK\Clients\
```

![image](https://github.com/user-attachments/assets/1e1a8d87-0377-446d-aaf5-d78562991db3)

6. Select `Clients_GetAll.odc` and click `Open`.

> ⚠️ If parameters are needed, you'll see an error now. It's ok, but you'll need to set them.

### Setting parameters
If there are any parameters listed near the top of this file, create a named range with each name listed under **Excel Named Range(s):**
> They're just named ranges, with particular names.
