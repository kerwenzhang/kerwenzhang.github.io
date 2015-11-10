---
layout: postlayout
title: "[转] MFC中ListControl控件的使用"
date:   2015-05-31 00:18:23 
categories: [MFC]
tags: [MFC, ListControl]
---

以下未经说明，listctrl默认view 风格为report

##1. CListCtrl 风格
	LVS_ICON: 为每个item显示大图标  
	LVS_SMALLICON: 为每个item显示小图标  
	LVS_LIST: 显示一列带有小图标的item  
	LVS_REPORT: 显示item详细资料
直观的理解：windows资源管理器，&ldquo;查看&rdquo;标签下的&ldquo;大图标，小图标，列表，详细资料&rdquo;
 

##2. 设置listctrl 风格及扩展风格
	LONG lStyle;  
	lStyle = GetWindowLong(m_list.m_hWnd, GWL_STYLE);//获取当前窗口style  
	lStyle &amp;= ~LVS_TYPEMASK; //清除显示方式位  
	lStyle |= LVS_REPORT; //设置style  
	SetWindowLong(m_list.m_hWnd, GWL_STYLE, lStyle);//设置style  
   
	DWORD dwStyle = m_list.GetExtendedStyle();  
	dwStyle |= LVS_EX_FULLROWSELECT;//选中某行使整行高亮（只适用与report风格的listctrl）  
	dwStyle |= LVS_EX_GRIDLINES;//网格线（只适用与report风格的listctrl）  
	dwStyle |= LVS_EX_CHECKBOXES;//item前生成checkbox控件  
	m_list.SetExtendedStyle(dwStyle); //设置扩展风格  
    
注：listview的style请查阅msdn  
<a href="http://msdn.microsoft.com/library/default.asp?url=/library/en-us/wceshellui5/html/wce50lrflistviewstyles.asp">http://msdn.microsoft.com/library/default.asp?url=/library/en-us/wceshellui5/html/wce50lrflistviewstyles.asp

##3. 插入数据
	m_list.InsertColumn( 0, "ID", LVCFMT_LEFT, 40 );//插入列  
	m_list.InsertColumn( 1, "NAME", LVCFMT_LEFT, 50 );  
	int nRow = m_list.InsertItem(0, &ldquo;11&rdquo;);//插入行  
	m_list.SetItemText(nRow, 1, &ldquo;jacky&rdquo;);//设置数据

##4. 一直选中item

    选中style中的Show selection always，或者在上面第2点中设置LVS_SHOWSELALWAYS  
  
  
	

##5. 选中和取消选中一行
	int nIndex = 0;  
	//选中  
	m_list.SetItemState(nIndex, LVIS_SELECTED|LVIS_FOCUSED, LVIS_SELECTED|LVIS_FOCUSED);  
	//取消选中  
	m_list.SetItemState(nIndex, 0, LVIS_SELECTED|LVIS_FOCUSED);

##6. 得到listctrl中所有行的checkbox的状态
	m_list.SetExtendedStyle(LVS_EX_CHECKBOXES);  
	CString str;  
	for(int i=0; i&lt;m_list.GetItemCount(); i++)  
	{  
		if( m_list.GetItemState(i, LVIS_SELECTED) == LVIS_SELECTED || m_list.GetCheck(i))  
		{  
			str.Format(_T("第%d行的checkbox为选中状态"), i);  
			AfxMessageBox(str);  
		}  
	}
 

##7. 得到listctrl中所有选中行的序号  

方法一：      
	CString str;  
	for(int i=0; i&lt;m_list.GetItemCount(); i++)  
	{  
		if( m_list.GetItemState(i, LVIS_SELECTED) == LVIS_SELECTED )    
		{  
			str.Format(_T("选中了第%d行"), i);  
			AfxMessageBox(str);  
		}  
	}
方法二：  
	POSITION pos = m_list.GetFirstSelectedItemPosition();  
	if (pos == NULL)  
		TRACE0("No items were selected!/n");  
	else  
	{  
		while (pos)  
		{  
			int nItem = m_list.GetNextSelectedItem(pos);  
			TRACE1("Item %d was selected!/n", nItem);  
			// you could do your own processing on nItem here  
		}  
	}
 
##8. 得到item的信息  
	TCHAR szBuf[1024];  
	LVITEM lvi;  
	lvi.iItem = nItemIndex;  
	lvi.iSubItem = 0;  
	lvi.mask = LVIF_TEXT;  
	lvi.pszText = szBuf;  
	lvi.cchTextMax = 1024;  
	m_list.GetItem(&amp;lvi);  
关于得到设置item的状态，还可以参考msdn文章  
Q173242: Use Masks to Set/Get Item States in CListCtrl  
<a href="http://support.microsoft.com/kb/173242/en-us">http://support.microsoft.com/kb/173242/en-us
 

##9. 得到listctrl的所有列的header字符串内容
	LVCOLUMN lvcol;  
	char  str[256];  
	int   nColNum;  
	CString  strColumnName[4];//假如有4列
	nColNum = 0;  
	lvcol.mask = LVCF_TEXT;  
	lvcol.pszText = str;  
	lvcol.cchTextMax = 256;  
	while(m_list.GetColumn(nColNum, &amp;lvcol))  
	{   
		strColumnName[nColNum] = lvcol.pszText;  
		nColNum++;  
	}
 

##10. 使listctrl中一项可见，即滚动滚动条

	m_list.EnsureVisible(i, FALSE);  
  


##11. 得到listctrl列数

	int nHeadNum = m_list.GetHeaderCtrl()-&gt;GetItemCount();  
  


##12. 删除所有列
方法一：  
	while ( m_list.DeleteColumn (0))  
	因为你删除了第一列后，后面的列会依次向上移动。
方法二：  
	int nColumns = 4;  
		for (int i=nColumns-1; i&gt;=0; i--)  
		m_list.DeleteColumn (i);
 

##13. 得到单击的listctrl的行列号
添加listctrl控件的NM_CLICK消息相应函数  
	void CTest6Dlg::OnClickList1(NMHDR* pNMHDR, LRESULT* pResult)  
	{  
		// 方法一：  
		/*  
		DWORD dwPos = GetMessagePos();  
		CPoint point( LOWORD(dwPos), HIWORD(dwPos) );  
     
		m_list.ScreenToClient(&amp;point);  
     
		LVHITTESTINFO lvinfo;  
		lvinfo.pt = point;  
		lvinfo.flags = LVHT_ABOVE;  
       
		int nItem = m_list.SubItemHitTest(&amp;lvinfo);  
		if(nItem != -1)  
		{  
			CString strtemp;  
			strtemp.Format("单击的是第%d行第%d列", lvinfo.iItem, lvinfo.iSubItem);  
			AfxMessageBox(strtemp);  
		}  
          */  
     
		// 方法二:  
		/*  
		NM_LISTVIEW* pNMListView = (NM_LISTVIEW*)pNMHDR;  
		if(pNMListView-&gt;iItem != -1)  
		{  
			CString strtemp;  
			strtemp.Format("单击的是第%d行第%d列",  
				pNMListView-&gt;iItem, pNMListView-&gt;iSubItem);  
			AfxMessageBox(strtemp);  
		}  
		*/  
		*pResult = 0;  
	}

##14. 判断是否点击在listctrl的checkbox上
添加listctrl控件的NM_CLICK消息相应函数  
	void CTest6Dlg::OnClickList1(NMHDR* pNMHDR, LRESULT* pResult)  
	{  
		DWORD dwPos = GetMessagePos();  
		CPoint point( LOWORD(dwPos), HIWORD(dwPos) );  
     
		m_list.ScreenToClient(&amp;point);  
     
		LVHITTESTINFO lvinfo;  
		lvinfo.pt = point;  
		lvinfo.flags = LVHT_ABOVE;  
       
		UINT nFlag;  
		int nItem = m_list.HitTest(point, &amp;nFlag);  
		//判断是否点在checkbox上  
		if(nFlag == LVHT_ONITEMSTATEICON)  
		{  
			AfxMessageBox("点在listctrl的checkbox上");  
		}   
		*pResult = 0;  
	}
 

##15. 右键点击listctrl的item弹出菜单
	添加listctrl控件的NM_RCLICK消息相应函数  
	void CTest6Dlg::OnRclickList1(NMHDR* pNMHDR, LRESULT* pResult)  
	{  
		NM_LISTVIEW* pNMListView = (NM_LISTVIEW*)pNMHDR;  
		if(pNMListView-&gt;iItem != -1)  
		{  
			DWORD dwPos = GetMessagePos();  
			CPoint point( LOWORD(dwPos), HIWORD(dwPos) );  
      
			CMenu menu;  
			VERIFY( menu.LoadMenu( IDR_MENU1 ) );  
			CMenu* popup = menu.GetSubMenu(0);  
			ASSERT( popup != NULL );  
			popup-&gt;TrackPopupMenu(TPM_LEFTALIGN | TPM_RIGHTBUTTON, point.x, point.y, this );  
		}   
		*pResult = 0;  
	} 

 
 
修改某一行的某一项
m_listRecvDetail.SetItem(m_listItemCount-2,3,LVIF_TEXT,"不应答",0,0,0,NULL);
Post Date: {{ page.date | date_to_string }}