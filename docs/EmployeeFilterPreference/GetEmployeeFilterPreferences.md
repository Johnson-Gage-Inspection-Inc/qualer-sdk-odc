# `EmployeeFilterPreference_GetEmployeeFilterPreferences`
> GetEmployeeFilterPreferences

**URL Template:**
`GET /api/user/filters`

**Parameters (Named Ranges):**

> *Required parameters are bolded.*



**Description:**
No description provided.

### Response Schema

#### OK [200]

| Field        | Type    |
|:-------------|:--------|
| FilterType   | string  |
| WithinDays   | integer |
| UseDateRange | boolean |
| StartDate    | string  |
| EndDate      | string  |

**Group (Tag):**
EmployeeFilterPreference

**ODC File:**
[Excel-Qualer-SDK/EmployeeFilterPreference/EmployeeFilterPreference_GetEmployeeFilterPreferences.odc](https://github.com/Johnson-Gage-Inspection-Inc/qualer-sdk-odc/blob/main/Excel-Qualer-SDK/EmployeeFilterPreference/EmployeeFilterPreference_GetEmployeeFilterPreferences.odc)

---

To Use in Excel:
---

1. Go to the ![`Data`](https://github.com/user-attachments/assets/da437a70-57b3-4c5b-bb01-4910ece19ed1)
 tab.
3. Click ![Existing Connections](https://github.com/user-attachments/assets/a2f1ed67-b2e0-4c23-ac90-68c870e60289)
4. Click ![`Browse for More...`](https://github.com/user-attachments/assets/8e698494-6865-41e7-b6fa-043aea81809a)
5. Paste the following into the URL bar
```
\\jgiquality.sharepoint.com@SSL\sites\JGI\Shared Documents\General\Excel-Qualer-SDK\EmployeeFilterPreference\
```

![image](https://github.com/user-attachments/assets/1e1a8d87-0377-446d-aaf5-d78562991db3)

6. Select `EmployeeFilterPreference_GetEmployeeFilterPreferences.odc` and click `Open`.

> ⚠️ If parameters are needed, you'll see an error now. It's ok, but you'll need to set them.

### Setting parameters
If there are any parameters listed near the top of this file, create a named range with each name listed under **Excel Named Range(s):**
> They're just named ranges, with particular names.
