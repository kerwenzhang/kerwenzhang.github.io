---
layout: postlayout
title: "[转]LOGFont, HFont和CFont"
date:   2015-05-31 00:18:23 
thumbimg: 1346208288725.jpg
categories: [MFC]
tags: [MFC, Font]
---

<div id="cnblogs_post_body"><p><strong>实际上就是逻辑字体和物理字体的区别</strong></p>
<p>LOGFONT:&nbsp;一个结构，用来逻辑上表达一个字体，比如LOGFONT.lfFaceName是字体的名字&nbsp;<br />HFONT:&nbsp;一个句柄，相当于表示内存中的一个字体对象，它可以马上拿来用&nbsp;<br />CFont:&nbsp;是mfc对于HFONT的一种封装&nbsp;<br /><br />可以说LOGFONT是一种墨水的名字，比如英雄牌，比较抽象&nbsp;<br />而HFONT表示实实在在的一瓶墨水，打开瓶盖就可以用&nbsp;<br />CFont只是把一瓶墨水外面包了一层纸，其实它还是一瓶墨水</p>
<div><br />**************************************</div>
<div>当你需要简单的使用字体就是用CFont&nbsp;<br />如果需要定义字体的各个小的细节等复杂的字体就用LOGFONT&nbsp;<br />HFONT可以是他们两个相互之间发生联系<br /><br />**************************************<br />CFont -&gt; LogFont:</div>
<div>&nbsp;</div>
<div>CFont&nbsp;*pFont&nbsp;=&nbsp;new&nbsp;CFont;&nbsp;<br />pFont-&gt;CreateFont(....&nbsp;//填的参数很多:(&nbsp;<br />LOGFONT&nbsp;logFont;&nbsp;<br />pFont-&gt;GetLogFont(&amp;logFont)//得到刚刚在Create里填的东东&nbsp;</div>
<div>&nbsp;</div>
<div>LogFont -&gt; CFont:</div>
<div><br />LOGFONT&nbsp;logfont;&nbsp;<br />lstrcpy((LPSTR)logfont.lfFaceName,(LPSTR)"楷体_GB2312");&nbsp;<br />logfont.lfWeight=700;&nbsp;<br />logfont.lfWidth=20;&nbsp;<br />logfont.lfHeight=50;&nbsp;<br />logfont.lfEscapement=0;&nbsp;<br />logfont.lfUnderline=FALSE;&nbsp;<br />logfont.lfItalic=FALSE;&nbsp;<br />logfont.lfStrikeOut=FALSE;&nbsp;<br />logfont.lfCharSet=GB2312_CHARSET;&nbsp;//以上参数好像一个都不能少&nbsp;<br /><br />pFont-&gt;CreateFontIndirect(&amp;logfont);&nbsp;<br />//行了，这下就有内容了。可以拿来用了。<br />可以用CWnd::GetFont得到当前窗口的font。</div>
<div>&nbsp;</div>
<div>////////////////////////////////////////////////////////////////////////////</div>
<div>LOGFONT结构体原型：</div>
<div>
<div class="para">typedef struct tagLOGFONT</div>
<div class="para">{</div>
<div class="para">LONG lfHeight;</div>
<div class="para">LONG lfWidth;</div>
<div class="para">LONG lfEscapement;</div>
<div class="para">LONG lfOrientation;</div>
<div class="para">LONG lfWeight;</div>
<div class="para">BYTE lfItalic;</div>
<div class="para">BYTE lfUnderline;</div>
<div class="para">BYTE lfStrikeOut;</div>
<div class="para">BYTE lfCharSet;</div>
<div class="para">BYTE lfOutPrecision;</div>
<div class="para">BYTE lfClipPrecision;</div>
<div class="para">BYTE lfQuality;</div>
<div class="para">BYTE lfPitchAndFamily;</div>
<div class="para">TCHAR lfFaceName[LF_FACESIZE];</div>
<p class="para">} LOGFONT;</p>
<div class="para">
<p class="headline-2"><span class="headline-content"><strong>lfHeight</strong>：</span></p>
<p class="para">以逻辑单位指定字体字符元(character cell)或字符的高度。字符高度值为字符元高度值减去内部行距(internal-leading)值。当lfHeight大于0时，字体映射程序将该值转换为设备单位，并将它与可用字体的字符元高度进行匹配；当该参数为0时，字体映射程度将使用一个匹配的默认高度值；如果参数的值小于0，则将其转换为设备单位，并将其绝对值与可用字体的字符高度进行匹配。对于任何一种情况，字体映射程度最终得到的字体高度值不会超过所指定的值。以MM_TEXT映射模式下，字体高度值和磅值有如下的换算公式：lfHeight=-MulDiv(PointSize, GetDeviceCaps(hDC, LOGPIXELSY), 72);</p>
<p class="headline-2"><span class="headline-content"><strong>lfWidth</strong>：</span></p>
<p class="para">以逻辑单位指定字体字符的平均宽度。如果lfWidth的值为0，则根据设备的纵横比从可用字体的数字转换纵横中选取最接近的匹配值，该值通过比较两者之间的差异的绝对值得出。</p>
<p class="headline-2"><span class="headline-content"><strong>lfEscapement</strong>：</span></p>
<p class="para">以十分之一度为单位指定每一行文本输出时相对于页面底端的角度。</p>
<p class="headline-2"><span class="headline-content"><strong>lfOrientation</strong>：</span></p>
<p class="para">以十分之一度为单位指定字符基线相对于页面底端的角度。</p>
<p class="headline-2"><span class="headline-content"><strong>lfWeight</strong>：</span></p>
<p class="para">指定字体重量。在Windows中，字体重量这个术语用来指代字体的粗细程度。lfWeight的范围为0到1000，正常情况下的字体重量为400，粗体为700。如果lfWeight为0，则使用默认的字体重量。</p>
<p class="headline-2"><span class="headline-content"><strong>lfItalic</strong>：</span></p>
<p class="para">当lfItalic为TRUE时使用斜体</p>
<p class="headline-2"><span class="headline-content"><strong>lfUnderline</strong>：</span></p>
<p class="para">当lfUnderline为TRUE时给字体添加下划线</p>
<p class="headline-2"><span class="headline-content"><strong>lfStrikeOut</strong>：</span></p>
<p class="para">当lfStrikeOut为TRUE时给字体添加删除线</p>
<p class="headline-2"><span class="headline-content"><strong>lfCharSet</strong>：</span></p>
<p class="para">指定字符集。可以使用以下预定义的值：ANSI_CHARSET、BALTIC_CHARSET、CHINESEBIG5_CHARSET、DEFAULT_CHARSET、EASTEUROPE_CHARSET、GB2312_CHARSET、GREEK_CHARSET、HANGUL_CHARSET、MAC_CHARSET、OEM_CHARSET、RUSSIAN_CHARSET、SHIFTJIS_CHARSET、SYMBOL_CHARSET、TURKISH_CHARSET。</p>
<p class="para">其中，OEM_CHARSET 表示字符集依赖本地操作系统。</p>
<p class="para">DEFAULT_CHARSET 表示字符集基于本地操作系统。例如，系统位置是 English (United States),字符集将设置为 ANSI_CHARSET。</p>
<p class="headline-2"><span class="headline-content"><strong>lfOutPrecision</strong>：</span></p>
<p class="para">指定输出精度。输出精度定义了输出与所要求的字体高度、宽度、字符方向等的接近程度。它可以为下面的值之一：OUT_CHARACTER_PRECIS、OUT_DEFAULT_PRECIS、OUT_STRING_PRECIS、OUT_STROKE_PRECIS。</p>
<p class="headline-2"><span class="headline-content"><strong>lfClipPrecision</strong>：</span></p>
<p class="para">指定剪辑精度。剪辑精度定义了当字符的一部分超过剪辑区域时对字符的剪辑方式，它可以为下列值之一：CLIP_CHARACTER_PRECIS、CLIP_DEFAULT_PRECIS、CLIP_STROKE_PRECIS。</p>
<p class="headline-2"><span class="headline-content"><strong>lfQuality</strong>：</span></p>
<p class="para">定义输出质量。输出质量定义了图形设备接口在匹配逻辑字体属性到实际的物理字体的所使用的方式，它可以为下列值之一：DEFAULT_QUALITY (默认质量)、DRAFT_QUALITY (草稿质量)、PROOF_QUALITY (正稿质量)。</p>
<p class="headline-2"><span class="headline-content"><strong>lfPitchAndFamily</strong>：</span></p>
<p class="para">指定字体的字符间距和族。最低两位指定字体的字符间距为以下值之一：DEFAULT_PITCH、FIXED_PITCH、VARIABLE_PITCH第4到7位指定字体族为以下值之一：FF_DECORATIVE、FF_DONTCARE、FF_MODERN、FF_ROMAN、FF_SCRIPT、FF_SWISS这些值的具体含义可以参考Visual C++中关于结构LOGFONT的文档。字符间距和字体族可以使用逻辑或(OR)运算符来进行组合。</p>
<p class="headline-2"><span class="headline-content"><strong>lfFaceName</strong>：</span></p>
<p class="para">一个指定以NULL结尾的字符串，它指定的所用的字体名。该字符串的长度不得超过32个字符，如果lfFaceName为NULL，图形设备接口将使用默认的字体名。</p>
<p class="para">&nbsp;</p>
<p class="para">////////////////////////////////////////////////////////////////////////////</p>
<p class="para">CFont:</p>
<div class="para">BOOL CreateFont(</div>
<div class="para">int nHeight,</div>
<div class="para">int nWidth,</div>
<div class="para">int nEscapement,</div>
<div class="para">int nOrientation,</div>
<div class="para">int nWeight,</div>
<div class="para">BYTE bItalic,</div>
<div class="para">BYTE bUnderline,</div>
<div class="para">BYTE cStrikeOut,</div>
<div class="para">BYTE nCharSet,</div>
<div class="para">BYTE nOutPrecision,</div>
<div class="para">BYTE nClipPrecision,</div>
<div class="para">BYTE nQuality,</div>
<div class="para">BYTE nPitchAndFamily,</div>
<div class="para">LPCTSTR lpszFacename</div>
<div class="para">);</div>
<div class="para">参数：</div>
<div class="para">
<div class="para"><strong>nHeight</strong>：</div>
<div class="para">指定字体高度（逻辑单位）。有三种取值：&gt;0，字体映射器将高度值转换为设备单位，并与可用字体的字符元高度进行匹配；=0，字体映射器使用默认的高度值；&lt;0，字体映射器将高度值转换为设备单位，用其绝对值与可用字体的字符高度进行匹配。nHeight转换后的绝对值不应超过16384个设备单位。</div>
<div class="para"><strong>nWidth</strong>：</div>
<div class="para">指定字体中字符的平均宽度（逻辑单位）。</div>
<div class="para"><strong>nEscapement</strong>：</div>
<div class="para">指定偏离垂线和显示界面X轴之间的角度，以十分之一度为单位。偏离垂线是穿过一行文本中第一个字符和最后一个字符的直线。</div>
<div class="para"><strong>nOrientation</strong>：</div>
<div class="para">指定每个字符的基线和设备X轴之间的角度，以十分之一度为单位。</div>
<div class="para"><strong>nWeight</strong>：</div>
<div class="para">指定字体磅数（每1000点中墨点像素数）。可取0到1000之间的任意整数值。</div>
<div class="para"><strong>bItalic</strong>：</div>
<div class="para">指定字体是否为斜体。</div>
<div class="para"><strong>bUnderline</strong>：</div>
<div class="para">指定字体是否带有下划线。</div>
<div class="para"><strong>bStrikeOut</strong>：</div>
<div class="para">指定字体是否带有删除线。</div>
<div class="para"><strong>nCharSet</strong>：</div>
<div class="para">指定字体的字符集。预定义的字符集：</div>
<div class="para">ANSI_CHARSET;BALTIC_CHARSET;CHINESEBIG5_CHARSET;DEFAULT_CHARSET;EASTEUROPE_CHARSET; GB2312_CHARSET; GREEK_CHARSET;HANGUL_CHARSET; MAC_CHARSET; OEM_CHARSET; RUSSIAN_CHARSET; SHIFTJIS_CHARSET;SYMBOL_CHARSET; TURKISH_CHARSET。韩国Windows：JOHAB_CHARSET；中东地区Windows：HEBREW_CHARSSET，ARABIC_CHARSET；泰国Windows：THAI_CHARSET。</div>
<div class="para">应用程序可以使用DEFAULT_CHARSET以允许字体名和大小完全指定逻辑字体，如果指定的字体名不存在则可能会用任意字符集的字体来代替，所以为避免不可预料的结果，应谨慎使用DEFAULT_CHARSET。</div>
<div class="para"><strong>nOutPrecision</strong>：</div>
<div class="para">指定输出精度。输出精度定义了输出与要求的字体高度、宽度、字符方向、移位和间距等的接近程度。它的取值及含义如下（只能取其一）：</div>
<div class="para">OUT_CHARACTER_PRECIS；未用。</div>
<div class="para">OUT_DEFAULT_PRECIS：指定缺省的字体映射器状态。</div>
<div class="para">OUT_DEVICE_PRECIS：在当系统里有多种字体使用同一个名字时指示字体映射器选择一种设备字体。</div>
<div class="para">OUT_OUTLINE_PRCIS：在Windows NT中此值指示字体映射器从TrueType和其他基于边框的字体中选择。</div>
<div class="para">OUT_RASTER_PRECIS：在当系统里有多种字体使用同一个名字时指示字体映射器选择一种光栅字体。</div>
<div class="para">OUT_STRING_PRECIS：此值没有被字体映射器使用，但是当列举光栅字体时它会被返回。</div>
<div class="para">OUT_STROKE_PRECIS：没有被字体映射器使用，但是当列举TrueType字体、其他基于边框的字体和向量字体时它会被返回。</div>
<div class="para">OUT_TT_ONLY_PRECIS：指示字体映射器仅从TrueType字体中选择，如果系统中没有安装TrueType字体，则字体映射返回缺省状态。</div>
<div class="para">OUT_TT_PRECIS：在当系统里有多种同名的字体时指示字体映射器选择一种TrueType字体。当操作系统含有多种与指定名字同名的字体时，应用程序可以使用OUT_DEVICE_PRECIS，OUT_RASTER_PRECIS和OUT_TT_PRECIS值来控制字体映射器如何选择一种字体，例如，如果操作系统含有名字Symbol的光栅和TrueType两种字体，指定OUT_TT_PRECIS使字体映射器选择TrueType方式（指定OUT_TT_ONLY_PRECIS强制字体映射器选择一种TrueType字体，尽管这会给TrueType字体换一个名字）。</div>
<div class="para"><strong>nClipPrecision</strong>：</div>
<div class="para">指定裁剪精度。裁剪精度定义了怎样裁剪部分超出裁剪区域的字符。它的取值及含义如下（可取一个或多个值）：</div>
<div class="para">CLIP_DEFAULT_PRECIS：指定缺省裁剪状态。</div>
<div class="para">CLIP_CHARACTER_PRECIS：未用。</div>
<div class="para">CLIP_STROKE_PRECIS：未被字体映射器使用，但是当列举光栅字体、向量字体或TrueType字体时它会被返回。在Windows环境下，为保证兼容性，当列举字体时这个值总被返回。</div>
<div class="para">CLIP_MASK：未用。</div>
<div class="para">CLIP_EMBEDDED：要使用嵌入式只读字体必须使用此标志。</div>
<div class="para">CLIP_LH_ANGLES：当此值被使用时，所有字体的旋转依赖于坐标系统的定位是朝左的还是朝右的。如果未使用此值，设备字体总是逆时针方向旋转，但其他字体的旋转依赖于坐标系统的定向。</div>
<div class="para">CLIP_TT_ALWAYS：未用。</div>
<div class="para"><strong>nQuality</strong>：</div>
<div class="para">指定字体的输出质量。输出质量定义了GDI将逻辑字体属性匹配到实际物理字体的细致程度。它的各个取值及含义如下（取其一）：</div>
<div class="para">DEFAULT_QUALITY：字体的外观不重要。</div>
<div class="para">DRAFT_QUALITY：字体外观的重要性次于使用PROOF_QUALITY时，对GDI光栅字体，缩放比例是活动的，这意味着多种字体大小可供选择，但质量可能不高，如果有必要，粗体、斜体、下划线、strikeout字体可被综合起来使用。</div>
<div class="para">PROOF_QUALITY：字符质量比精确匹配逻辑字体字体属性更重要。对GDI扫描字体，缩放比例是活动的，并选择最接近的大小。尽管当使用PROOF_QUALITY时，选择字体大小并不完全匹配，但字体的质量很高，并没有外观上的变形。如果有必要，粗体、斜体、下划线、strikeout字体可被综合起来使用。</div>
<div class="para"><strong>nPitchAndFamily</strong>：</div>
<div class="para">指定字体间距和字体族。低2位用来指定字体的间距，可取下列值中的一个：DEFAULT_PITCH，FIXED_PITCH，VARIABLE_PITCH。高4位指定字体族，取值及含义如下（取其一）：</div>
<div class="para">FF_DECORATIVE：新奇的字体，如老式英语（Old English）。</div>
<div class="para">FF_DONTCARE：不关心或不知道。</div>
<div class="para">FF_MDERN：笔划宽度固定的字体，有或者无衬线。如Pica、Elite和Courier New。</div>
<div class="para">FF_ROMAN：笔划宽度变动的字体，有衬线。如MS Serif。</div>
<div class="para">FF_SCRIPT：设计成看上去象手写体的字体。如Script和Cursive。</div>
<div class="para">FF_SWISS：笔划宽度变动的字体，无斜线。如MS Sans Serif。</div>
<div class="para">应用程序可以用运算符OR将字符间距和字体族组合起来给nPitchAndFamily赋值。</div>
<div class="para">字体族描述一种字体的普通外观，当所有的精确字样都不能使用时，可用它们来指定字体。</div>
<div class="para"><strong>lpszFacename</strong>：</div>
<div class="para">指定字体的字样名的字符串。此字符串的长度不应超过30个字符。Windows函数EnumFontFamilies可以枚举出当前所有可用字体的字样名。如果lpszFacename为NULL，则GDI使用一种与设备无关的字体。</div>
<div class="para">返回值：此函数成功则返回TRUE，否则返回FALSE。</div>

<p>Post Date: {{ page.date | date_to_string }}</p>