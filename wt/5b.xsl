<?xml version = "1.0"?> <xsl:stylesheet version = "1.0" xmlns:xsl = 
"http://www.w3.org/1999/XSL/Transform" xmlns="http://www.w3.org/1999/xhtml">
<xsl:template match = "RU">
<html><head><title> Style sheet for 5b.xml </title>
</head><body>
<h2> Shopping </h2>
<span style = "font-style: italic; color: blue;"> Books: 
</span> <xsl:value-of select = "b" /> <br />
<span style = "font-style: italic; color: blue;"> Electronics: 
</span> <xsl:value-of select = "e" /> <br /
<span style = "font-style: italic; color: blue;"> Stationary: 
</span> <xsl:value-of select = "s" /> <br />
<span style = "font-style: italic; color: blue;"> Clothes: 
</span> <xsl:value-of select = "c" /> <br />
<span style = "font-style: italic; color: blue;"> Others: 
</span> <xsl:value-of select = "o" /> <br />
</body>
</html>
</xsl:template>
</xsl:stylesheet>