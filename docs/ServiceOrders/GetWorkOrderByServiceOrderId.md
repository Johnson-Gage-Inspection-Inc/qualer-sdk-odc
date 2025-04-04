# `ServiceOrders_GetWorkOrderByServiceOrderId`
> 
    
**URL Template:**
`GET /api/service/workorders/{serviceOrderId}`

**Parameters (Named Ranges):**

> *Required parameters are bolded.*

| Excel Name         | Type    | In   |
|:-------------------|:--------|:-----|
| **ServiceOrderId** | integer | path |

**Description:**
No description provided.

### Response Schema

#### OK [200]

| Field                                     | Type    |
|:------------------------------------------|:--------|
| ServiceOrderId                            | integer |
| ParentOrderId                             | integer |
| ClientLegacyId                            | string  |
| OwnerName                                 | string  |
| SubmitedByName                            | string  |
| SignOffByName                             | string  |
| VendorSignOffByName                       | string  |
| ApprovedByName                            | string  |
| AcceptedByName                            | string  |
| ReadyForQualityControlByName              | string  |
| QualityControlByName                      | string  |
| CreatedByName                             | string  |
| CompletedByName                           | string  |
| ShippedByName                             | string  |
| DeliveredByName                           | string  |
| InvoicedByName                            | string  |
| PaidByName                                | string  |
| CancelledByName                           | string  |
| ClosedByName                              | string  |
| ClientCompanyId                           | integer |
| ClientCompanyName                         | string  |
| ClientDomainName                          | string  |
| ClientAlternativeNames                    | string  |
| ServiceComments                           | string  |
| ServicePrivateComments                    | string  |
| CreatedOn                                 | string  |
| ApprovedOn                                | string  |
| SignOffOn                                 | string  |
| VendorSignOffOn                           | string  |
| CompletedOn                               | string  |
| SubmitedOn                                | string  |
| ShippedOn                                 | string  |
| AcceptedOn                                | string  |
| ReadyForQualityControlOn                  | string  |
| QualityControlOn                          | string  |
| DeliveredOn                               | string  |
| InvoicedOn                                | string  |
| LastInvoicedOn                            | string  |
| PaymentDueOn                              | string  |
| PaidOn                                    | string  |
| LateFeeOn                                 | string  |
| CancelledOn                               | string  |
| ClosedOn                                  | string  |
| LastUpdatedOn                             | string  |
| LastUpdatedBy                             | string  |
| SubmitedById                              | integer |
| SignOffById                               | integer |
| VendorSignOffById                         | integer |
| ApprovedById                              | integer |
| LateFeeById                               | integer |
| AcceptedById                              | integer |
| ReadyForQualityControlById                | integer |
| QualityControlById                        | integer |
| CreatedById                               | integer |
| CompletedById                             | integer |
| ShippedById                               | integer |
| DeliveredById                             | integer |
| InvoicedById                              | integer |
| PaidById                                  | integer |
| CancelledById                             | integer |
| ClosedById                                | integer |
| PoNumber                                  | string  |
| SecondaryPo                               | string  |
| ServiceTotal                              | number  |
| RepairsTotal                              | number  |
| PartsTotal                                | number  |
| PartsTotalBeforeDiscount                  | number  |
| PartsDiscountTotal                        | number  |
| EffectiveTaxRate                          | number  |
| TaxAmount                                 | number  |
| ShippingFee                               | number  |
| TravelCharge                              | number  |
| LateFee                                   | number  |
| IsTaxExempt                               | boolean |
| ServiceDiscount                           | number  |
| TradeInCredit                             | number  |
| PrepaidCredit                             | number  |
| GrandTotal                                | number  |
| PaidAmount                                | number  |
| RemainingBalance                          | number  |
| ServiceDiscountDetails                    | string  |
| TradeInCreditDetails                      | string  |
| PrepaidCreditDetails                      | string  |
| PaymentNotes                              | string  |
| ServiceOrderNumber                        | integer |
| LegacyOrderNumber                         | string  |
| CustomOrderNumber                         | string  |
| PaymentStatus                             | string  |
| PaymentOption                             | string  |
| ShipmentStatus                            | string  |
| OrderStatus                               | string  |
| OwnerId                                   | integer |
| OwnerDepartment                           | string  |
| ClientSite                                | string  |
| ClientSiteCode                            | string  |
| VendorSite                                | string  |
| Internal                                  | boolean |
| Guid                                      | string  |
| BusinessFromTime                          | string  |
| BusinessToTime                            | string  |
| SiteAccessNotes                           | string  |
| DesiredDate                               | string  |
| DeadlineDate                              | string  |
| RequestFromDate                           | string  |
| RequestFromTime                           | string  |
| RequestToDate                             | string  |
| RequestToTime                             | string  |
| OrderNotes                                | string  |
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

**Group (Tag):**
ServiceOrders

**ODC File:**
[Excel-Qualer-SDK/ServiceOrders/ServiceOrders_GetWorkOrderByServiceOrderId.odc](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-odc/blob/main/Excel-Qualer-SDK/ServiceOrders/ServiceOrders_GetWorkOrderByServiceOrderId.odc)

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

6. Select `ServiceOrders_GetWorkOrderByServiceOrderId.odc` and click `Open`.

> ⚠️ If parameters are needed, you'll see an error now. It's ok, but you'll need to set them.

### Setting parameters
If there are any parameters listed near the top of this file, create a named range with each name listed under **Excel Named Range(s):**
> They're just named ranges, with particular names.
