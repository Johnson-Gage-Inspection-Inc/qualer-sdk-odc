# `ReportDatasets_GetAsFoundMeasurementsByServiceOrderItemId`
> 

**URL Template:**
`GET /api/data/MeasurementsAsFound/{serviceOrderItemId}`

**Parameters (Named Ranges):**

> *Required parameters are bolded.*

| Name                   | Type    | Format   |
|:-----------------------|:--------|:---------|
| **ServiceOrderItemId** | integer | int32    |

**Description:**
No description provided.

### Response Schema

#### OK [200]

| Field                                   | Type    |
|:----------------------------------------|:--------|
| IsAccredited                            | boolean |
| ServiceTotal                            | number  |
| RepairsTotal                            | number  |
| PartsTotal                              | number  |
| ParameterId                             | integer |
| ToolRangeName                           | string  |
| ToolRangeUncertainty                    | string  |
| PrimaryToolLastServiceDate              | string  |
| PrimaryToolNextServiceDate              | string  |
| PrimaryToolCalibratedBy                 | string  |
| PrimaryToolToolName                     | string  |
| PrimaryToolToolDescription              | string  |
| PrimaryToolToolTypeName                 | string  |
| PrimaryToolManufacturer                 | string  |
| PrimaryToolManufacturerPartNumber       | string  |
| PrimaryToolSerialNumber                 | string  |
| SecondaryToolLastServiceDate            | string  |
| SecondaryToolNextServiceDate            | string  |
| SecondaryToolCalibratedBy               | string  |
| SecondaryToolToolName                   | string  |
| SecondaryToolToolDescription            | string  |
| SecondaryToolToolTypeName               | string  |
| SecondaryToolManufacturer               | string  |
| SecondaryToolManufacturerPartNumber     | string  |
| SecondaryToolSerialNumber               | string  |
| MeasurementSetName                      | string  |
| DecimalPlaces                           | integer |
| SignificantFigures                      | integer |
| SdHeader                                | number  |
| CvHeader                                | number  |
| MeasurementLocalTime                    | string  |
| Mean                                    | number  |
| MeanRaw                                 | number  |
| MeanDecimalPlaces                       | integer |
| MeanExtended                            | string  |
| Sd                                      | number  |
| SdRaw                                   | number  |
| SDDecimalPlaces                         | integer |
| Delta                                   | number  |
| Range                                   | number  |
| SdExtended                              | string  |
| RangeExtended                           | string  |
| DeltaExtended                           | string  |
| MinimumMeasuredValue                    | number  |
| MaximumMeasuredValue                    | number  |
| MinMaxValueExtended                     | string  |
| Cv                                      | number  |
| CvRaw                                   | number  |
| CVDecimalPlaces                         | integer |
| CvExtended                              | string  |
| Result                                  | integer |
| RangeResult                             | boolean |
| DeltaResult                             | boolean |
| MinResult                               | boolean |
| MaxResult                               | boolean |
| TarResult                               | boolean |
| TurResult                               | boolean |
| ErrorResult                             | boolean |
| SdResult                                | boolean |
| CvResult                                | boolean |
| CustomFieldResult                       | integer |
| Mu                                      | number  |
| MuRaw                                   | number  |
| MUEffectiveDOF                          | number  |
| MUCoverageFactor                        | number  |
| MuExtended                              | string  |
| Cmc                                     | number  |
| CmcComments                             | string  |
| Tur                                     | number  |
| TurRaw                                  | number  |
| TURDecimalPlaces                        | integer |
| Tar                                     | number  |
| TarRaw                                  | number  |
| TARDecimalPlaces                        | integer |
| GuardBand                               | string  |
| GuardBandLogic                          | string  |
| UncertaintyBudget                       | string  |
| CalculatedUncertainty                   | number  |
| LockUncertaintyBudget                   | boolean |
| LabMu                                   | number  |
| Channel                                 | integer |
| MeasurementType                         | string  |
| UpdatedBy                               | string  |
| UpdatedOn                               | string  |
| Error                                   | number  |
| ErrorExtended                           | string  |
| RequireAdjustment                       | boolean |
| AdjustmentThreshold                     | number  |
| PercentOfTolerance                      | number  |
| PercentOfToleranceExtended              | string  |
| TOLDecimalPlaces                        | integer |
| SpecificationTitle                      | string  |
| SpecificationSubtitle                   | string  |
| SpecificationGroup                      | string  |
| BatchType                               | integer |
| BatchResult                             | integer |
| IsByChannel                             | boolean |
| ChannelCount                            | integer |
| IsRangeAccredited                       | boolean |
| CommencedOn                             | string  |
| CommencedBy                             | string  |
| ZFactor                                 | number  |
| AirBuoyancy                             | number  |
| EvaporationRate                         | number  |
| AirHumidity                             | number  |
| Altitude                                | number  |
| AmbientTemperature                      | number  |
| BarometricPressure                      | number  |
| LightIntensity                          | number  |
| NoiseLevel                              | number  |
| PhLevel                                 | number  |
| WaterConductivity                       | number  |
| WaterTemperature                        | number  |
| SolarRadiation                          | number  |
| WindSpeed                               | number  |
| ZFactorUom                              | string  |
| AirBuoyancyUom                          | string  |
| EvaporationRateUom                      | string  |
| AirHumidityUom                          | string  |
| AltitudeUom                             | string  |
| AmbientTemperatureUom                   | string  |
| BarometricPressureUom                   | string  |
| LightIntensityUom                       | string  |
| NoiseLevelUom                           | string  |
| PhLevelUom                              | string  |
| WaterConductivityUom                    | string  |
| WaterTemperatureUom                     | string  |
| SolarRadiationUom                       | string  |
| WindSpeedUom                            | string  |
| SpecificationName                       | string  |
| ParameterName                           | string  |
| MeasurementSetDisplayOrder              | integer |
| DisplayOrder                            | integer |
| UnitOfMeasure                           | string  |
| DisplayFormat                           | string  |
| Precision                               | number  |
| Minimum                                 | number  |
| Nominal                                 | number  |
| ExpectedValue                           | number  |
| ExpectedValueRaw                        | string  |
| TestValue                               | number  |
| BaseValue                               | number  |
| UseExpectedValue                        | boolean |
| ReadingEntryLogic                       | string  |
| ReadingEntryMath                        | string  |
| DoubleSubstitutionSequence              | string  |
| ReadingEntryMathString                  | string  |
| NominalExtended                         | string  |
| ExpectedValueExtended                   | string  |
| Maximum                                 | number  |
| ToleranceMin                            | number  |
| ToleranceMax                            | number  |
| Resolution                              | number  |
| ResolutionCount                         | number  |
| MinMaxHeader                            | string  |
| AccuracyClass                           | string  |
| AccuracyClassMin                        | number  |
| AccuracyClassMax                        | number  |
| EnvironmentMask                         | string  |
| DisplayName                             | string  |
| DisplayPartNumber                       | string  |
| PartNumber                              | string  |
| VendorCompanyId                         | integer |
| ServiceOrderNumber                      | integer |
| CustomOrderNumber                       | string  |
| CompletedByName                         | string  |
| CompletedOn                             | string  |
| IsLimited                               | boolean |
| VendorTag                               | string  |
| VendorServiceNotes                      | string  |
| Room                                    | string  |
| SegmentName                             | string  |
| ScheduleName                            | string  |
| NextSegmentName                         | string  |
| CertificateNumber                       | string  |
| WorkStatus                              | integer |
| ServiceType                             | string  |
| ServiceLevel                            | string  |
| Barcode                                 | string  |
| ServiceComments                         | string  |
| OrderItemNumber                         | integer |
| AssetTag                                | string  |
| AssetUser                               | string  |
| SerialNumber                            | string  |
| EquipmentId                             | string  |
| LegacyIdentifier                        | string  |
| SiteName                                | string  |
| AssetName                               | string  |
| AssetDescription                        | string  |
| ProductName                             | string  |
| ProductDescription                      | string  |
| AssetMaker                              | string  |
| Station                                 | string  |
| AssetTagChange                          | string  |
| AssetUserChange                         | string  |
| SerialNumberChange                      | string  |
| ServiceDate                             | string  |
| NextServiceDate                         | string  |
| ServiceOrderItemId                      | integer |
| ServiceOrderId                          | integer |
| MeasurementBatchId                      | integer |
| MeasurementId                           | integer |
| StandardId                              | integer |
| ToolId                                  | integer |
| MeasurementToolId                       | integer |
| MeasurementConditionId                  | integer |
| MeasurementPointId                      | integer |
| MeasurementSetId                        | integer |
| IsHidden                                | boolean |
| Readings                                | integer |
| ToleranceType                           | string  |
| ToleranceTypeString                     | string  |
| PrecisionType                           | string  |
| SpecificationMode                       | string  |
| ToleranceMode                           | string  |
| ToleranceUnit                           | string  |
| ToleranceString                         | string  |
| PoNumber                                | string  |
| SecondaryPo                             | string  |
| ShippedDate                             | string  |
| ShipmentStatus                          | string  |
| ShippedOn                               | string  |
| DeliveredOn                             | string  |
| TrackingNumber                          | string  |
| PaymentTerms                            | integer |
| ShippingMethod                          | string  |
| Location                                | string  |
| SiteAccessNotes                         | string  |
| AbbreviatedUOM                          | string  |
| UnitScaleFactor                         | number  |
| MeasurementNotTakenResult               | string  |
| HideFromCertificate                     | boolean |
| MeasurementNotTakenReason               | string  |
| EnvironmentText1                        | string  |
| EnvironmentText2                        | string  |
| EnvironmentText3                        | string  |
| EnvironmentText4                        | string  |
| EnvironmentText5                        | string  |
| EnvironmentText6                        | string  |
| Values                                  | string  |
| Value1                                  | string  |
| Value2                                  | string  |
| Value3                                  | string  |
| Value4                                  | string  |
| Value5                                  | string  |
| Value6                                  | string  |
| Value7                                  | string  |
| Value8                                  | string  |
| Value9                                  | string  |
| Value10                                 | string  |
| Value11                                 | string  |
| Value12                                 | string  |
| Value13                                 | string  |
| Value14                                 | string  |
| Value15                                 | string  |
| Value16                                 | string  |
| Value17                                 | string  |
| Value18                                 | string  |
| Value19                                 | string  |
| Value20                                 | string  |
| Value21                                 | string  |
| Value22                                 | string  |
| Value23                                 | string  |
| Value24                                 | string  |
| Value25                                 | string  |
| Value26                                 | string  |
| Value27                                 | string  |
| Value28                                 | string  |
| Value29                                 | string  |
| Value30                                 | string  |
| Value31                                 | string  |
| Value32                                 | string  |
| Value33                                 | string  |
| Value34                                 | string  |
| Value35                                 | string  |
| Value36                                 | string  |
| Value37                                 | string  |
| Value38                                 | string  |
| Value39                                 | string  |
| Value40                                 | string  |
| RawValue1                               | string  |
| RawValue2                               | string  |
| RawValue3                               | string  |
| RawValue4                               | string  |
| RawValue5                               | string  |
| RawValue6                               | string  |
| RawValue7                               | string  |
| RawValue8                               | string  |
| RawValue9                               | string  |
| RawValue10                              | string  |
| RawValue11                              | string  |
| RawValue12                              | string  |
| RawValue13                              | string  |
| RawValue14                              | string  |
| RawValue15                              | string  |
| RawValue16                              | string  |
| RawValue17                              | string  |
| RawValue18                              | string  |
| RawValue19                              | string  |
| RawValue20                              | string  |
| RawValue21                              | string  |
| RawValue22                              | string  |
| RawValue23                              | string  |
| RawValue24                              | string  |
| RawValue25                              | string  |
| RawValue26                              | string  |
| RawValue27                              | string  |
| RawValue28                              | string  |
| RawValue29                              | string  |
| RawValue30                              | string  |
| RawValue31                              | string  |
| RawValue32                              | string  |
| RawValue33                              | string  |
| RawValue34                              | string  |
| RawValue35                              | string  |
| RawValue36                              | string  |
| RawValue37                              | string  |
| RawValue38                              | string  |
| RawValue39                              | string  |
| RawValue40                              | string  |
| SubtitlesToReadings                     | string  |
| ValueSubtitle1                          | string  |
| ValueSubtitle2                          | string  |
| ValueSubtitle3                          | string  |
| ValueSubtitle4                          | string  |
| ValueSubtitle5                          | string  |
| ValueSubtitle6                          | string  |
| ValueSubtitle7                          | string  |
| ValueSubtitle8                          | string  |
| ValueSubtitle9                          | string  |
| ValueSubtitle10                         | string  |
| ValueSubtitle11                         | string  |
| ValueSubtitle12                         | string  |
| ValueSubtitle13                         | string  |
| ValueSubtitle14                         | string  |
| ValueSubtitle15                         | string  |
| ValueSubtitle16                         | string  |
| ValueSubtitle17                         | string  |
| ValueSubtitle18                         | string  |
| ValueSubtitle19                         | string  |
| ValueSubtitle20                         | string  |
| ValueSubtitle21                         | string  |
| ValueSubtitle22                         | string  |
| ValueSubtitle23                         | string  |
| ValueSubtitle24                         | string  |
| ValueSubtitle25                         | string  |
| ValueSubtitle26                         | string  |
| ValueSubtitle27                         | string  |
| ValueSubtitle28                         | string  |
| ValueSubtitle29                         | string  |
| ValueSubtitle30                         | string  |
| ValueSubtitle31                         | string  |
| ValueSubtitle32                         | string  |
| ValueSubtitle33                         | string  |
| ValueSubtitle34                         | string  |
| ValueSubtitle35                         | string  |
| ValueSubtitle36                         | string  |
| ValueSubtitle37                         | string  |
| ValueSubtitle38                         | string  |
| ValueSubtitle39                         | string  |
| ValueSubtitle40                         | string  |
| ValuesDecimalPlaces                     | integer |
| RepeatMeasurementAndCalculateHysteresis | boolean |
| MeasurementPointOrder                   | string  |
| HysteresisPoint                         | string  |
| MaxHysteresis                           | number  |
| Run                                     | integer |
| Direction                               | integer |
| Hysteresis                              | number  |
| ColumnMean                              | string  |
| ColumnMeanResult                        | string  |
| ColumnSD                                | string  |
| ColumnSDResult                          | string  |
| ColumnCV                                | string  |
| ColumnCVResult                          | string  |
| ColumnRange                             | string  |
| ColumnRangeResult                       | string  |
| ColumnDelta                             | string  |
| ColumnDeltaResult                       | string  |
| ColumnResult                            | string  |

**Group (Tag):**
ReportDatasets

**ODC File:**
[Excel-Qualer-SDK/ReportDatasets/ReportDatasets_GetAsFoundMeasurementsByServiceOrderItemId.odc](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-odc/blob/main/Excel-Qualer-SDK/ReportDatasets/ReportDatasets_GetAsFoundMeasurementsByServiceOrderItemId.odc)

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

6. Select `ReportDatasets_GetAsFoundMeasurementsByServiceOrderItemId.odc` and click `Open`.

> ⚠️ If parameters are needed, you'll see an error now. It's ok, but you'll need to set them.

### Setting parameters
If there are any parameters listed near the top of this file, create a named range with each name listed under **Excel Named Range(s):**
> They're just named ranges, with particular names.
