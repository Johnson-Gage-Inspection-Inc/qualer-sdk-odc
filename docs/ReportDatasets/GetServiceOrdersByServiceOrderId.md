# `ReportDatasets_GetServiceOrdersByServiceOrderId`
> 
    
**URL Template:**
`GET /api/data/ServiceOrders/{serviceOrderId}`

**Parameters (Named Ranges):**

> *Required parameters are bolded.*

| Name               | Type    | Format   |
|:-------------------|:--------|:---------|
| **ServiceOrderId** | integer | int32    |

**Description:**
No description provided.

### Response Schema

#### OK [200]

| Field                         | Type    |
|:------------------------------|:--------|
| Guid                          | string  |
| AccountNumber                 | string  |
| ServiceOrderNumber            | integer |
| ServiceOrderNumberText        | string  |
| NumberOfInstruments           | integer |
| PartsDiscountTotal            | number  |
| PoNumber                      | string  |
| SecondaryPo                   | string  |
| Location                      | string  |
| ShippedDate                   | string  |
| PaymentTerms                  | integer |
| SiteAccessNotes               | string  |
| GracePeriod                   | integer |
| TradeInCredit                 | number  |
| PrepaidCredit                 | number  |
| InterestRate                  | number  |
| ServiceTaxation               | integer |
| ServiceOrderId                | integer |
| FederalNumber                 | string  |
| VendorSiteId                  | integer |
| VendorSite                    | string  |
| SiteName                      | string  |
| SiteCode                      | string  |
| VendorName                    | string  |
| DomainName                    | string  |
| ClientCompanyDomain           | string  |
| ProviderLogo                  | string  |
| ClientSignature               | string  |
| VendorSignature               | string  |
| QrCode                        | string  |
| BarCode                       | string  |
| BarCodeString                 | string  |
| PoBalance                     | number  |
| ServiceTerms                  | string  |
| ServiceTotal                  | number  |
| RepairsTotal                  | number  |
| PartsTotal                    | number  |
| PartsTotalBeforeDiscount      | number  |
| EffectiveTaxRate              | number  |
| TaxAmount                     | number  |
| ShippingFee                   | number  |
| LateFee                       | number  |
| GrandTotal                    | number  |
| AmountPaid                    | number  |
| BalanceTotal                  | number  |
| TravelCharge                  | number  |
| PrivateNotes                  | string  |
| ServiceNotes                  | string  |
| DisplayServiceComments        | boolean |
| DisplayPartRepairs            | boolean |
| PrintSeparateMeasurement      | boolean |
| BillingAddress1               | string  |
| BillingAddress2               | string  |
| BillingFirstName              | string  |
| BillingLastName               | string  |
| BillingCompany                | string  |
| BillingCountry                | string  |
| BillingCity                   | string  |
| BillingState                  | string  |
| BillingZip                    | string  |
| BillingPhoneNumber            | string  |
| BillingFaxNumber              | string  |
| BillingEmail                  | string  |
| ShippingAddress1              | string  |
| ShippingAddress2              | string  |
| ShippingFirstName             | string  |
| ShippingLastName              | string  |
| ShippingEmail                 | string  |
| ShippingCompany               | string  |
| ShippingCity                  | string  |
| ShippingZip                   | string  |
| ShippingPhoneNumber           | string  |
| ShippingFaxNumber             | string  |
| ShippingCountry               | string  |
| ShippingState                 | string  |
| ShippingMethod                | string  |
| ReturnShippingMethod          | string  |
| TrackingNumber                | string  |
| ProviderBillingAddress1       | string  |
| ProviderBillingAddress2       | string  |
| ProviderBillingFirstName      | string  |
| ProviderBillingLastName       | string  |
| ProviderBillingEmail          | string  |
| ProviderBillingCompany        | string  |
| ProviderBillingCity           | string  |
| ProviderBillingZip            | string  |
| ProviderBillingPhoneNumber    | string  |
| ProviderBillingCountry        | string  |
| ProviderBillingState          | string  |
| ProviderBillingFaxNumber      | string  |
| ProviderShippingAddress1      | string  |
| ProviderShippingAddress2      | string  |
| ProviderShippingFirstName     | string  |
| ProviderShippingLastName      | string  |
| ProviderShippingEmail         | string  |
| ProviderShippingCompany       | string  |
| ProviderShippingCity          | string  |
| ProviderShippingZip           | string  |
| ProviderShippingPhoneNumber   | string  |
| ProviderShippingCountry       | string  |
| ProviderShippingState         | string  |
| ProviderShippingFaxNumber     | string  |
| CultureName                   | string  |
| VendorCompanyId               | integer |
| ClientVendorId                | integer |
| SignOffDate                   | string  |
| QualityControlDate            | string  |
| ClientSignOffOn               | string  |
| ClientSignOffByName           | string  |
| ClientSignedOn                | string  |
| ClientStickerNotes            | string  |
| AssetStickerNotes             | string  |
| OrderStickerNotes             | string  |
| QualityControlName            | string  |
| FulfilledByName               | string  |
| SignOffName                   | string  |
| DisplayAsFound                | boolean |
| DisplayAsLeft                 | boolean |
| CreatedOn                     | string  |
| InvoicedOn                    | string  |
| SubmittedOn                   | string  |
| ShippedOn                     | string  |
| CompletedOn                   | string  |
| AcceptedOn                    | string  |
| ApprovedOn                    | string  |
| DeliveredOn                   | string  |
| PaidOn                        | string  |
| CancelledOn                   | string  |
| FulfilledOn                   | string  |
| SignOffOn                     | string  |
| VendorSignedOn                | string  |
| ClientNotes                   | string  |
| OrderShippingOption           | integer |
| ShipmentStatus                | integer |
| PaymentStatus                 | integer |
| PaymentOption                 | string  |
| OrderStatus                   | integer |
| CreatedByName                 | string  |
| CompletedByName               | string  |
| ShippedByName                 | string  |
| AcceptedByName                | string  |
| ApproveByName                 | string  |
| InvoicedByName                | string  |
| DeliveredByName               | string  |
| PaidByName                    | string  |
| CancelledByName               | string  |
| SignOffByName                 | string  |
| OwnerName                     | string  |
| OwnerDepartment               | string  |
| AssigneeName                  | string  |
| PaymentDueOn                  | string  |
| ProcessDateOption             | string  |
| DesiredDate                   | string  |
| DeadlineDate                  | string  |
| VendorSignOffOn               | string  |
| VendorSignOffByName           | string  |
| ServiceDiscount               | number  |
| ReturnAccount                 | string  |
| BusinessHoursFrom             | string  |
| BusinessHoursTo               | string  |
| ClientCompanyAlternativeNames | string  |
| ClientId                      | integer |
| ClientClass                   | string  |
| ClientStatus                  | string  |
| ClientInvoicing               | string  |
| ClientStanding                | string  |
| ClientCategory                | string  |
| MasterTemplateName            | string  |
| ClientSiteCode                | string  |
| OrderWorkflowName             | string  |
| RequestWorkflowName           | string  |

**Group (Tag):**
ReportDatasets

**ODC File:**
[Excel-Qualer-SDK/ReportDatasets/ReportDatasets_GetServiceOrdersByServiceOrderId.odc](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-odc/blob/main/Excel-Qualer-SDK/ReportDatasets/ReportDatasets_GetServiceOrdersByServiceOrderId.odc)

---

To Use in Excel:
---

1. Go to the ![`Data`](https://github.com/user-attachments/assets/da437a70-57b3-4c5b-bb01-4910ece19ed1)
 tab.
3. Click ![Existing Connections](https://github.com/user-attachments/assets/a2f1ed67-b2e0-4c23-ac90-68c870e60289)
4. Click ![`Browse for More...`](https://github.com/user-attachments/assets/8e698494-6865-41e7-b6fa-043aea81809a)
5. Paste the following into the URL bar
```
\\jgiquality.sharepoint.com@SSL\sites\JGI\Shared Documents\General\Excel-Qualer-SDK\ReportDatasets\
```

![image](https://github.com/user-attachments/assets/1e1a8d87-0377-446d-aaf5-d78562991db3)

6. Select `ReportDatasets_GetServiceOrdersByServiceOrderId.odc` and click `Open`.

> ⚠️ If parameters are needed, you'll see an error now. It's ok, but you'll need to set them.

### Setting parameters
If there are any parameters listed near the top of this file, create a named range with each name listed under **Excel Named Range(s):**
> They're just named ranges, with particular names.
