let
    Status = try Excel.CurrentWorkbook(){[Name="Status"]}[Content]{0}[Column1] otherwise "",
    CompanyId = try Excel.CurrentWorkbook(){[Name="CompanyId"]}[Content]{0}[Column1] otherwise "",
    From = try Excel.CurrentWorkbook(){[Name="From"]}[Content]{0}[Column1] otherwise "",
    To = try Excel.CurrentWorkbook(){[Name="To"]}[Content]{0}[Column1] otherwise "",
    ModifiedAfter = try Excel.CurrentWorkbook(){[Name="ModifiedAfter"]}[Content]{0}[Column1] otherwise "",
    WorkOrderNumber = try Excel.CurrentWorkbook(){[Name="WorkOrderNumber"]}[Content]{0}[Column1] otherwise "",
    AssignedEmployees = try Excel.CurrentWorkbook(){[Name="AssignedEmployees"]}[Content]{0}[Column1] otherwise "",
    q1 = if Text.Length(Status) > 0 then [ status = Status ] else [],
    q2 = if Text.Length(CompanyId) > 0 then [ companyId = CompanyId ] else [],
    q3 = if Text.Length(From) > 0 then [ from = From ] else [],
    q4 = if Text.Length(To) > 0 then [ to = To ] else [],
    q5 = if Text.Length(ModifiedAfter) > 0 then [ modifiedAfter = ModifiedAfter ] else [],
    q6 = if Text.Length(WorkOrderNumber) > 0 then [ workOrderNumber = WorkOrderNumber ] else [],
    q7 = if Text.Length(AssignedEmployees) > 0 then [ assignedEmployees = AssignedEmployees ] else [],
    QueryOptions = Record.Combine({q1, q2, q3, q4, q5, q6, q7}),
    baseUrl = "https://jgiquality.qualer.com",
    relativeUrl = "api/service/workorders",
    response = Web.Contents(
        baseUrl,
        [
            RelativePath = Text.TrimStart(relativeUrl, "/"),
            Query = QueryOptions,
            Headers = [ Authorization = "Api-Token bf407589-f463-4046-ba2c-30642bd5d637" ]
        ]
    ),
    json = Json.Document(response),
    ConvertToTable = Table.FromRecords(json)
in
    ConvertToTable