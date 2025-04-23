def render_odc_xml(name: str, mashup_formula: str) -> str:
    return f"""<html xmlns:o="urn:schemas-microsoft-com:office:office"
xmlns="http://www.w3.org/TR/REC-html40">

<head>
<meta http-equiv=Content-Type content="text/x-ms-odc; charset=utf-8">
<meta name=ProgId content=ODC.Database>
<meta name=SourceType content=OLEDB>
<title>Query - {name}</title>
<xml id=docprops><o:DocumentProperties
  xmlns:o="urn:schemas-microsoft-com:office:office"
  xmlns="http://www.w3.org/TR/REC-html40">
  <o:Description>Connection to the '{name}' query in the workbook.</o:Description>
  <o:Name>Query - {name}</o:Name>
 </o:DocumentProperties>
</xml><xml id=msodc><odc:OfficeDataConnection
  xmlns:odc="urn:schemas-microsoft-com:office:odc"
  xmlns="http://www.w3.org/TR/REC-html40">
  <odc:PowerQueryConnection odc:Type="OLEDB">
   <odc:ConnectionString>Provider=Microsoft.Mashup.OleDb.1;Data Source=$Workbook$;Location={name};Extended Properties=&quot;&quot;</odc:ConnectionString>
   <odc:CommandType>SQL</odc:CommandType>
   <odc:CommandText>SELECT * FROM [{name}]</odc:CommandText>
  </odc:PowerQueryConnection>
  <odc:PowerQueryMashupData>&lt;Mashup xmlns:xsd=&quot;http://www.w3.org/2001/XMLSchema&quot; xmlns:xsi=&quot;http://www.w3.org/2001/XMLSchema-instance&quot; xmlns=&quot;http://schemas.microsoft.com/DataMashup&quot;&gt;&lt;Client&gt;EXCEL&lt;/Client&gt;&lt;Version&gt;2.140.405.0&lt;/Version&gt;&lt;MinVersion&gt;2.21.0.0&lt;/MinVersion&gt;&lt;Culture&gt;en-US&lt;/Culture&gt;&lt;SafeCombine&gt;true&lt;/SafeCombine&gt;&lt;Items&gt;&lt;Query Name=&quot;{name}&quot;&gt;&lt;Formula&gt;&lt;![CDATA[{mashup_formula}]]&gt;&lt;/Formula&gt;&lt;IsParameterQuery xsi:nil=&quot;true&quot; /&gt;&lt;IsDirectQuery xsi:nil=&quot;true&quot; /&gt;&lt;/Query&gt;&lt;/Items&gt;&lt;/Mashup&gt;</odc:PowerQueryMashupData>
 </odc:OfficeDataConnection>
</xml>""" + """
<style>
<!--
    .ODCDataSource
    {
    behavior: url(dataconn.htc);
    }
-->
</style>"""
