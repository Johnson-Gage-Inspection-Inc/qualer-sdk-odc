# `ClientAssets_GetAssetManagerList`

**URL Template:**  
`GET /api/service/clients/{clientCompanyId}/assets/byfilter`

**Parameters:**  
- `clientCompanyId` (path)

**Excel Named Range(s):**  
- `ClientCompanyId`

**Description:**  
assetFilterType: ClientUnset, ClientAssetsCollected, ClientPastDue, ClientDueForService, ClientOutOfService, ClientWithoutSchedule
            
ClientDueForService - depends on Employee Filter Preference
POST api/user/filters

**Group (Tag):**  
ClientAssets

**ODC File:**  
`[Excel-Qualer-SDK/ClientAssets/ClientAssets_GetAssetManagerList.odc](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-odc/blob/main/Excel-Qualer-SDK/ClientAssets/ClientAssets_GetAssetManagerList.odc)`
