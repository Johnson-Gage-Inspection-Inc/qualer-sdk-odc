# `MaintenancePlans_GetMaintenancePlans`
> 
    
**URL Template:**
`GET /api/plans`

**Parameters (Named Ranges):**

> *Required parameters are bolded.*



**Description:**
No description provided.

### Response Schema

#### OK [200]

| Field                                       | Type    |
|:--------------------------------------------|:--------|
| MaintenancePlanId                           | integer |
| MaintenancePlanName                         | string  |
| IsTemplate                                  | boolean |
| CompanyName                                 | string  |
| MaintenanceTasks.SegmentName                | string  |
| MaintenanceTasks.ServiceLevelId             | integer |
| MaintenanceTasks.DisplayOrder               | integer |
| MaintenanceTasks.ServiceNotes               | string  |
| MaintenanceTasks.IntervalCycle              | string  |
| MaintenanceTasks.IntervalLength             | integer |
| MaintenanceTasks.OnDay                      | string  |
| MaintenanceTasks.OnMonth                    | string  |
| MaintenanceTasks.OnWeekDays                 | string  |
| MaintenanceTasks.WeekdayOfMonth             | string  |
| MaintenanceTasks.ColorCode                  | integer |
| MaintenanceTasks.ServiceInterval            | string  |
| MaintenanceTasks.OnSegmentId                | integer |
| MaintenanceTasks.DocumentNumber             | string  |
| MaintenanceTasks.DocumentSection            | string  |
| MaintenanceTasks.AsFoundStandardGroupId     | integer |
| MaintenanceTasks.AsLeftStandardGroupId      | integer |
| MaintenanceTasks.TaskNotes                  | string  |
| MaintenanceTasks.AdvanceRecallPeriod        | string  |
| MaintenanceTasks.DaysBeforeDue              | integer |
| MaintenanceTasks.PastDueGracePeriod         | string  |
| MaintenanceTasks.DaysAfterDue               | integer |
| MaintenanceTasks.UsePeriodInReports         | string  |
| MaintenanceTasks.GenerateOrderAutomatically | boolean |
| MaintenanceTasks.ApproveUponGeneration      | boolean |
| MaintenanceTasks.GenerateSeparate           | boolean |

**Group (Tag):**
MaintenancePlans

**ODC File:**
[Excel-Qualer-SDK/MaintenancePlans/MaintenancePlans_GetMaintenancePlans.odc](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-odc/blob/main/Excel-Qualer-SDK/MaintenancePlans/MaintenancePlans_GetMaintenancePlans.odc)

---

To Use in Excel:
---

1. Go to the ![`Data`](https://github.com/user-attachments/assets/da437a70-57b3-4c5b-bb01-4910ece19ed1)
 tab.
3. Click ![Existing Connections](https://github.com/user-attachments/assets/a2f1ed67-b2e0-4c23-ac90-68c870e60289)
4. Click ![`Browse for More...`](https://github.com/user-attachments/assets/8e698494-6865-41e7-b6fa-043aea81809a)
5. Paste the following into the URL bar
```
\\jgiquality.sharepoint.com@SSL\sites\JGI\Shared Documents\General\Excel-Qualer-SDK\MaintenancePlans\
```

![image](https://github.com/user-attachments/assets/1e1a8d87-0377-446d-aaf5-d78562991db3)

6. Select `MaintenancePlans_GetMaintenancePlans.odc` and click `Open`.

> ⚠️ If parameters are needed, you'll see an error now. It's ok, but you'll need to set them.

### Setting parameters
If there are any parameters listed near the top of this file, create a named range with each name listed under **Excel Named Range(s):**
> They're just named ranges, with particular names.
