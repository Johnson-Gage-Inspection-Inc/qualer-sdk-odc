# `AssetMeasurements_GetMeasurementsByAssetByAssetId`

**URL Template:**
`GET /api/assets/{assetId}/measurements`

**Parameters:**
- *`assetId`: `integer`
- `from`: `string`
- `to`: `string`


> *Required parameters are marked with an asterisk (*).

**Excel Named Range(s):**
- `AssetId`
- `From`
- `To`


**Description:**
No description provided.

### Response Schema

#### OK
+------------------------------------------------------------------------------------------------------+---------+
| Field                                                                                                | Type    |
+======================================================================================================+=========+
| ServiceOrderId                                                                                       | integer |
+------------------------------------------------------------------------------------------------------+---------+
| ServiceOrderNumber                                                                                   | integer |
+------------------------------------------------------------------------------------------------------+---------+
| CustomOrderNumber                                                                                    | string  |
+------------------------------------------------------------------------------------------------------+---------+
| OrderItemNumber                                                                                      | integer |
+------------------------------------------------------------------------------------------------------+---------+
| CertificateNumber                                                                                    | string  |
+------------------------------------------------------------------------------------------------------+---------+
| ResultStatus                                                                                         | string  |
+------------------------------------------------------------------------------------------------------+---------+
| AsFoundResult                                                                                        | string  |
+------------------------------------------------------------------------------------------------------+---------+
| AsLeftResult                                                                                         | string  |
+------------------------------------------------------------------------------------------------------+---------+
| ServiceDate                                                                                          | string  |
+------------------------------------------------------------------------------------------------------+---------+
| SerialNumber                                                                                         | string  |
+------------------------------------------------------------------------------------------------------+---------+
| AssetTag                                                                                             | string  |
+------------------------------------------------------------------------------------------------------+---------+
| AssetUser                                                                                            | string  |
+------------------------------------------------------------------------------------------------------+---------+
| AssetTagChange                                                                                       | string  |
+------------------------------------------------------------------------------------------------------+---------+
| AssetUserChange                                                                                      | string  |
+------------------------------------------------------------------------------------------------------+---------+
| ServiceNotes                                                                                         | string  |
+------------------------------------------------------------------------------------------------------+---------+
| SerialNumberChange                                                                                   | string  |
+------------------------------------------------------------------------------------------------------+---------+
| DueDate                                                                                              | string  |
+------------------------------------------------------------------------------------------------------+---------+
| NextServiceDate                                                                                      | string  |
+------------------------------------------------------------------------------------------------------+---------+
| ServiceLevel                                                                                         | string  |
+------------------------------------------------------------------------------------------------------+---------+
| ServiceLevelCode                                                                                     | string  |
+------------------------------------------------------------------------------------------------------+---------+
| NextServiceLevel                                                                                     | string  |
+------------------------------------------------------------------------------------------------------+---------+
| NextServiceLevelCode                                                                                 | string  |
+------------------------------------------------------------------------------------------------------+---------+
| AssetName                                                                                            | string  |
+------------------------------------------------------------------------------------------------------+---------+
| AssetDescription                                                                                     | string  |
+------------------------------------------------------------------------------------------------------+---------+
| PartsCharge                                                                                          | number  |
+------------------------------------------------------------------------------------------------------+---------+
| PartsChargeBeforeDiscount                                                                            | number  |
+------------------------------------------------------------------------------------------------------+---------+
| ServiceCharge                                                                                        | number  |
+------------------------------------------------------------------------------------------------------+---------+
| RepairsCharge                                                                                        | number  |
+------------------------------------------------------------------------------------------------------+---------+
| SegmentName                                                                                          | string  |
+------------------------------------------------------------------------------------------------------+---------+
| ScheduleName                                                                                         | string  |
+------------------------------------------------------------------------------------------------------+---------+
| ServiceScheduleSegmentId                                                                             | integer |
+------------------------------------------------------------------------------------------------------+---------+
| ForwardNextService                                                                                   | boolean |
+------------------------------------------------------------------------------------------------------+---------+
| ForwardSegmentId                                                                                     | integer |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.BatchType                                                                         | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.BatchResult                                                                       | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.Specification.Title                                                               | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.Specification.Subtitle                                                            | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.Specification.Group                                                               | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementName                                                   | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.IsAccredited                                                      | boolean |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementQuantityId                                             | integer |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.DefaultUnitOfMeasureId                                            | integer |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.DecimalPlaces                                                     | integer |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.SignificantFigures                                                | integer |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.DisplayOptions.Err                                                | boolean |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.DisplayOptions.Mean                                               | boolean |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.DisplayOptions.Max                                                | boolean |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.DisplayOptions.Min                                                | boolean |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.DisplayOptions.Sd                                                 | boolean |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.DisplayOptions.Cv                                                 | boolean |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.DisplayOptions.Tar                                                | boolean |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.DisplayOptions.Tur                                                | boolean |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.DisplayOptions.Mu                                                 | boolean |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.DisplayOptions.Cmc                                                | boolean |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.DisplayOptions.Tol                                                | boolean |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.DisplayOptions.Delta                                              | boolean |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.DisplayOptions.Range                                              | boolean |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.CustomFields.Description                                          | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.CustomFields.Result                                               | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.CustomFields.Items.Name                                           | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.CustomFields.Items.Type                                           | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.CustomFields.Items.Value                                          | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.CustomFields.Items.FieldId                                        | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.CustomFields.Items.ValidValues                                    | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.SpecificationName                               | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.MeasurementQuantity                             | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.UnitOfMeasureId                                 | integer |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.UnitOfMeasure                                   | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.RangeMin                                        | number  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.RangeMax                                        | number  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.ToleranceType                                   | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.SpecificationMode                               | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.ToleranceMode                                   | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.ToleranceUnit                                   | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.PrecisionType                                   | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.Readings                                        | integer |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.ChannelsType                                    | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.ChannelCount                                    | integer |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.Precision                                       | number  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.ToleranceMinimum                                | number  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.ToleranceMaximum                                | number  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.Resolution                                      | number  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.ResolutionCount                                 | number  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.Nominal                                         | number  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.ExpectedValue                                   | number  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.BaseValue                                       | number  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.TestValue                                       | number  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.IsAccredited                                    | boolean |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.Measurements.Values                             | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.Measurements.Mean                               | number  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.Measurements.SD                                 | number  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.Measurements.Range                              | number  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.Measurements.Delta                              | number  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.Measurements.CV                                 | number  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.Measurements.CMC                                | number  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.Measurements.MU                                 | number  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.Measurements.TUR                                | number  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.Measurements.TAR                                | number  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.Measurements.MaxValue                           | number  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.Measurements.MinValue                           | number  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.Measurements.Error                              | number  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.Measurements.Result                             | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.Measurements.UpdatedOn                          | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.Measurements.UpdatedBy                          | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.ConditionFactors.FactorId                       | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.ConditionFactors.FactorName                     | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.ConditionFactors.FactorValue                    | number  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.ConditionFactors.FactorUom                      | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.ConditionFactors.LastModifiedOnUtc              | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.PrimaryMeasurementTool.LastServiceDate          | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.PrimaryMeasurementTool.NextServiceDate          | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.PrimaryMeasurementTool.CalibratedBy             | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.PrimaryMeasurementTool.CertificateNumber        | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.PrimaryMeasurementTool.ToolName                 | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.PrimaryMeasurementTool.ToolDescription          | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.PrimaryMeasurementTool.Manufacturer             | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.PrimaryMeasurementTool.ManufacturerPartNumber   | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.PrimaryMeasurementTool.SerialNumber             | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.PrimaryMeasurementTool.AssetTag                 | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.PrimaryMeasurementTool.AssetUser                | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.PrimaryMeasurementTool.EquipmentId              | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.SecondaryMeasurementTool.LastServiceDate        | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.SecondaryMeasurementTool.NextServiceDate        | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.SecondaryMeasurementTool.CalibratedBy           | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.SecondaryMeasurementTool.CertificateNumber      | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.SecondaryMeasurementTool.ToolName               | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.SecondaryMeasurementTool.ToolDescription        | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.SecondaryMeasurementTool.Manufacturer           | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.SecondaryMeasurementTool.ManufacturerPartNumber | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.SecondaryMeasurementTool.SerialNumber           | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.SecondaryMeasurementTool.AssetTag               | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.SecondaryMeasurementTool.AssetUser              | string  |
+------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.SecondaryMeasurementTool.EquipmentId            | string  |
+------------------------------------------------------------------------------------------------------+---------+

**Group (Tag):**
AssetMeasurements

**ODC File:**
[Excel-Qualer-SDK/AssetMeasurements/AssetMeasurements_GetMeasurementsByAssetByAssetId.odc](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-odc/blob/main/Excel-Qualer-SDK/AssetMeasurements/AssetMeasurements_GetMeasurementsByAssetByAssetId.odc)

---

To Use in Excel:
---

1. Go to the ![`Data`](https://github.com/user-attachments/assets/da437a70-57b3-4c5b-bb01-4910ece19ed1)
 tab.
3. Click ![Existing Connections](https://github.com/user-attachments/assets/a2f1ed67-b2e0-4c23-ac90-68c870e60289)
4. Click ![`Browse for More...`](https://github.com/user-attachments/assets/8e698494-6865-41e7-b6fa-043aea81809a)
5. Paste the following into the URL bar
```
\\jgiquality.sharepoint.com@SSL\sites\JGI\Shared Documents\General\Excel-Qualer-SDK\AssetMeasurements\
```

![image](https://github.com/user-attachments/assets/1e1a8d87-0377-446d-aaf5-d78562991db3)

6. Select `AssetMeasurements_GetMeasurementsByAssetByAssetId.odc` and click `Open`.

> ⚠️ If parameters are needed, you'll see an error now. It's ok, but you'll need to set them.

### Setting parameters
If there are any parameters listed near the top of this file, create a named range with each name listed under **Excel Named Range(s):**
> They're just named ranges, with particular names.
