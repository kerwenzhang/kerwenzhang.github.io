---                
layout: post                
title: "C# XML序列化" 
date:   2020-01-03 16:40:00                 
categories: "C#"                
catalog: true                
tags:                 
    - C#                
---      

    
1. Open xml to copy xml content
2. Create a new class in VS
3. Edit -> Paste Special -> Paste XML as Classes

        [System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
        [System.Xml.Serialization.XmlRootAttribute(Namespace = "", IsNullable = false)]
        public partial class Server
        {

            private string uriField;

            /// <remarks/>
            public string uri
            {
                get
                {
                    return this.uriField;
                }
                set
                {
                    this.uriField = value;
                }
            }
        }

4. Read xml data

        private Server GetServerListFromXML()
        {
            XmlDocument xmlDoc = new XmlDocument();
            string strXML = GetConfigXmlPath();
            if (!File.Exists(strXML))
            {
                Logger.Instance().LogError("XML File: " + strXML + " is NOT existed.");
                return null;
            }
            try
            {
                xmlDoc.Load(strXML);
            }
            catch (Exception e)
            {
                Logger.Instance().LogError("Cannot load " + strXML + ". Error message: " + e.Message);
            }
            Server serversList = ParseXML.DeserializeXML<Server>(xmlDoc.OuterXml);
            return serversList;
        }

5. Save data to xml

        private bool SaveServiceAddress(Server info)
        {
            StreamWriter sw = null;    
            try
            {
                string xml = ParseXML.Serializer(typeof(Server), info);
                string strXML = GetConfigXmlPath();
                FileStream fs = new FileStream(strXML, FileMode.OpenOrCreate);
                sw = new StreamWriter(fs);
                sw.Write(xml);
                sw.Close();
            }
            catch (Exception e)
            {
                if (sw != null)
                {
                    sw.Close();
                }
                return false;
            }
            return true;
        }
