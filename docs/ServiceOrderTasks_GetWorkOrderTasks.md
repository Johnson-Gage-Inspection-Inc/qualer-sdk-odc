# `ServiceOrderTasks_GetWorkOrderTasks`

**URL Template:**  
`GET /api/service/workorders/{serviceOrderId}/tasks`

**Parameters:**  
- `serviceOrderId` (path)

**Excel Named Range(s):**  
- `ServiceOrderId`

**Description:**  
TimeSpent
Integer part (before dot) is hours
Fractional part (after dot) is minutes
For example:
    if time spent is 10 minutes -&gt; 10 / 60 = 0.1666666666666667
    if time spent is 65 minutes -&gt; (65 - 60) + (5 / 60) = 1.0833333333333333

**Group (Tag):**  
ServiceOrderTasks

**ODC File:**  
`Excel-Qualer-SDK/ServiceOrderTasks/ServiceOrderTasks_GetWorkOrderTasks.odc`
