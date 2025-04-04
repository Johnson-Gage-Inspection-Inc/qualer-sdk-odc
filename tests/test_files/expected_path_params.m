let
    VendorCompanyId = try Excel.CurrentWorkbook(){[Name="VendorCompanyId"]}[Content]{0} otherwise "",
    QueryOptions = [],
    baseUrl = "https://jgiquality.qualer.com",
    relativeUrl = "api/service/vendors/" & Text.From(VendorCompanyId),
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
