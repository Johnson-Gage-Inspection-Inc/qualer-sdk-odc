# `ServiceOrderItemMeasurements_GetMeasurementFormByWorkItemId`

**URL Template:**
`GET /api/service/workitems/{workItemId}/form`

**Parameters:**
- *`workItemId`: `integer`


> *Required parameters are marked with an asterisk (*).

**Excel Named Range(s):**
- `WorkItemId`


**Description:**
No description provided.

### Response Schema

#### OK

+---------------------------------------------------------------------------------------------------------------+---------+
| Field                                                                                                         | Type    |
+===============================================================================================================+=========+
| MeasurementBatches.BatchId                                                                                    | integer |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.BatchType                                                                                  | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementSetId                                                           | integer |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementName                                                            | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.IsAccredited                                                               | boolean |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.UseExpectedValue                                                           | boolean |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.DecimalPlaces                                                              | integer |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.SignificantFigures                                                         | integer |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.InfluenceParameter1Type                                                    | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.InfluenceParameter1ToolTypeId                                              | integer |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.InfluenceParameter1ParameterId                                             | integer |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.InfluenceParameter1Source                                                  | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.InfluenceParameter1Value                                                   | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.InfluenceParameter2Type                                                    | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.InfluenceParameter2ToolTypeId                                              | integer |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.InfluenceParameter2ParameterId                                             | integer |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.InfluenceParameter2Source                                                  | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.InfluenceParameter2Value                                                   | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.MeasurementPointId                                       | integer |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.SpecificationName                                        | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.UnitOfMeasure                                            | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.ExpectedValue                                            | number  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.BaseValue                                                | number  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.TestValue                                                | number  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.Nominal                                                  | number  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.RangeMin                                                 | number  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.RangeMax                                                 | number  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.ToleranceType                                            | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.ToleranceMode                                            | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.ToleranceUnit                                            | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.PrecisionType                                            | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.Precision                                                | number  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.ToleranceMinimum                                         | number  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.ToleranceMaximum                                         | number  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.Resolution                                               | number  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.ResolutionCount                                          | number  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.IsAccredited                                             | boolean |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.LinkedMeasurementPointId                                 | integer |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.HysteresisPoint                                          | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.HideFromCertificate                                      | boolean |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.IsMeasurementNotTaken                                    | boolean |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.MeasurementNotTakenResult                                | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.MeasurementNotTakenReason                                | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.InfluenceParameter1ParameterId                           | integer |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.InfluenceParameter1Value                                 | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.InfluenceParameter2ParameterId                           | integer |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.InfluenceParameter2Value                                 | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.Measurements.MeasurementId                               | integer |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.Measurements.Values                                      | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.Measurements.Channel                                     | integer |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.Measurements.UpdatedBy                                   | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.Measurements.UpdatedOn                                   | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.MeasurementConditionFactors.MeasurementConditionFactorId | integer |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.MeasurementConditionFactors.FactorId                     | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.MeasurementConditionFactors.FactorName                   | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.MeasurementConditionFactors.FactorValue                  | number  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.MeasurementConditionFactors.FactorUom                    | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.PrimaryMeasurementTool.MeasurementToolId                 | integer |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.PrimaryMeasurementTool.LastServiceDate                   | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.PrimaryMeasurementTool.NextServiceDate                   | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.PrimaryMeasurementTool.CalibratedBy                      | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.PrimaryMeasurementTool.CertificateNumber                 | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.PrimaryMeasurementTool.ToolName                          | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.PrimaryMeasurementTool.ToolDescription                   | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.PrimaryMeasurementTool.Manufacturer                      | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.PrimaryMeasurementTool.ManufacturerPartNumber            | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.PrimaryMeasurementTool.SerialNumber                      | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.PrimaryMeasurementTool.AssetTag                          | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.PrimaryMeasurementTool.AssetUser                         | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.PrimaryMeasurementTool.EquipmentId                       | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.SecondaryMeasurementTool.MeasurementToolId               | integer |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.SecondaryMeasurementTool.LastServiceDate                 | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.SecondaryMeasurementTool.NextServiceDate                 | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.SecondaryMeasurementTool.CalibratedBy                    | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.SecondaryMeasurementTool.CertificateNumber               | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.SecondaryMeasurementTool.ToolName                        | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.SecondaryMeasurementTool.ToolDescription                 | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.SecondaryMeasurementTool.Manufacturer                    | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.SecondaryMeasurementTool.ManufacturerPartNumber          | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.SecondaryMeasurementTool.SerialNumber                    | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.SecondaryMeasurementTool.AssetTag                        | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.SecondaryMeasurementTool.AssetUser                       | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementPoints.SecondaryMeasurementTool.EquipmentId                     | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementFields.FieldId                                                  | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementFields.Name                                                     | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementFields.Type                                                     | string  |
+---------------------------------------------------------------------------------------------------------------+---------+
| MeasurementBatches.MeasurementSets.MeasurementFields.Value                                                    | string  |
+---------------------------------------------------------------------------------------------------------------+---------+

**Group (Tag):**
ServiceOrderItemMeasurements

**ODC File:**
[Excel-Qualer-SDK/ServiceOrderItemMeasurements/ServiceOrderItemMeasurements_GetMeasurementFormByWorkItemId.odc](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-odc/blob/main/Excel-Qualer-SDK/ServiceOrderItemMeasurements/ServiceOrderItemMeasurements_GetMeasurementFormByWorkItemId.odc)

---

To Use in Excel:
---

1. Go to the ![`Data`](https://github.com/user-attachments/assets/da437a70-57b3-4c5b-bb01-4910ece19ed1)
 tab.
3. Click ![Existing Connections](https://github.com/user-attachments/assets/a2f1ed67-b2e0-4c23-ac90-68c870e60289)
4. Click ![`Browse for More...`](https://github.com/user-attachments/assets/8e698494-6865-41e7-b6fa-043aea81809a)
5. Paste the following into the URL bar
```
\\jgiquality.sharepoint.com@SSL\sites\JGI\Shared Documents\General\Excel-Qualer-SDK\ServiceOrderItemMeasurements\
```

![image](https://github.com/user-attachments/assets/1e1a8d87-0377-446d-aaf5-d78562991db3)

6. Select `ServiceOrderItemMeasurements_GetMeasurementFormByWorkItemId.odc` and click `Open`.

> ⚠️ If parameters are needed, you'll see an error now. It's ok, but you'll need to set them.

### Setting parameters
If there are any parameters listed near the top of this file, create a named range with each name listed under **Excel Named Range(s):**
> They're just named ranges, with particular names.
