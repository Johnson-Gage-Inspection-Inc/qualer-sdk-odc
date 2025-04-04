let
    EmployeeId = try Excel.CurrentWorkbook(){[Name="EmployeeId"]}[Content]{0} otherwise "",
    IsInternal = try Excel.CurrentWorkbook(){[Name="IsInternal"]}[Content]{0} otherwise "",
    q1 = if Text.Length(IsInternal) > 0 then [ "isInternal" = IsInternal ] else [],
    QueryOptions = Record.Combine({q1}),
    baseUrl = "https://jgiquality.qualer.com",
    relativeUrl = "api/employee/" & Text.From(EmployeeId) & "/workorders",
    response = Web.Contents(
        baseUrl,
        [
            RelativePath = Text.TrimStart(relativeUrl, "/"),
            Query = QueryOptions,
            Headers = [ Authorization = "Api-Token bf407589-f463-4046-ba2c-30642bd5d637" ]
        ]
    ),
    json = Json.Document(response),
    ConvertToTable = Table.FromList(json, Splitter.SplitByNothing(), null, null, ExtraValues.Error)
in ConvertToTable
