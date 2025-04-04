let
    Model_accountNumberText = try Excel.CurrentWorkbook(){[Name="Model.accountNumberText"]}[Content]{0}[Column1] otherwise "",
    Model_companyName = try Excel.CurrentWorkbook(){[Name="Model.companyName"]}[Content]{0}[Column1] otherwise "",
    Model_take = try Excel.CurrentWorkbook(){[Name="Model.take"]}[Content]{0}[Column1] otherwise "",
    Model_modifiedAfter = try Excel.CurrentWorkbook(){[Name="Model.modifiedAfter"]}[Content]{0}[Column1] otherwise "",
    q1 = if Text.Length(Model_accountNumberText) > 0 then [ model.accountNumberText = Model_accountNumberText ] else [],
    q2 = if Text.Length(Model_companyName) > 0 then [ model.companyName = Model_companyName ] else [],
    q3 = if Text.Length(Model_take) > 0 then [ model.take = Model_take ] else [],
    q4 = if Text.Length(Model_modifiedAfter) > 0 then [ model.modifiedAfter = Model_modifiedAfter ] else [],
    QueryOptions = Record.Combine({q1, q2, q3, q4}),
    baseUrl = "https://jgiquality.qualer.com",
    relativeUrl = "api/service/vendors",
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
in
    ConvertToTable