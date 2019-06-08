# import bs4
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
html_doc ='''<html xmlns="http://www.w3.org/1999/xhtml"><head>
<title>好看的美剧推荐,天天美剧在线观看,2019美剧吧,美剧排行榜天堂-五杀电影院</title>
<meta name="keywords" content="美剧天堂,天天美剧,美剧吧,人人美剧">
<meta name="description" content="最新美剧在线看_美剧天堂_人人美剧吧_美剧下载_美剧排行榜前十名_美剧推荐">
<script type="text/javascript" async="" src="https://www.google-analytics.com/analytics.js"></script><script src="https://hm.baidu.com/hm.js?e3505c2df04d4cb537a857e99eb666b5"></script><script>var SitePath='/',SiteAid='12',SiteTid='45',SiteId='';</script>
<link href="/template/5sdy/css/bootstrap.min.css" rel="stylesheet">
<link href="/template/5sdy/css/ustv.css" rel="stylesheet">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
<meta name="renderer" content="webkit">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<meta name="applicable-device" content="pc,mobile">
<meta http-equiv="Cache-Control" content="no-siteapp">
<meta http-equiv="Cache-Control" content="no-transform">
<!--[if lt IE 9]>
      <script src="/template/5sdy/js/html5shiv.min.js"></script>
      <script src="/template/5sdy/js/respond.min.js"></script>
    <![endif]-->
<script src="/template/5sdy/js/jquery.min.js" type="text/javascript"></script>
<script src="/template/5sdy/js/jquery-migrate.min.js" type="text/javascript"></script>
<script src="/template/5sdy/js/bootstrap.min.js"></script>
<script src="/js/jq/jquery.lazyload.js"></script>
<script src="/js/jq/jquery.autocomplete.js"></script>
<script src="/template/5sdy/js/home.js"></script>
</head>
<body>
<div class="container">
  <div class="row visible-md visible-lg">
    <div class="col-md-2 tb col-sm-4"> <a class="logo" href="/">五杀电影院</a> </div>
    <div class="col-md-6 visible-md visible-lg">
    </div>
    <div class="col-md-4 col-sm-8">
       <div class="ss fr">
<form id="ffsearch" name="ffsearch" method="post" action="/index.php?m=vod-search">
<input type="submit" id="searchbutton" class="search-button" value="搜索">
<input type="text" id="wd" name="wd" class="search-input ac_input" value="输入影片片名或演员名称。" onfocus="if(this.value=='输入影片片名或演员名称。'){this.value='';}" onblur="if(this.value==''){this.value='输入影片片名或演员名称。';};" autocomplete="off">
</form> 
      </div>
    </div>
  </div>
</div>
<div class="dh bottom">
  <div class="container">
    <nav class="navbar navbar-static-top">
      <div class="container-fluid padding ">
        <div class="navbar-header visible-xs ">
          <button type="button" class="navbar-toggle collapsed col-xs-1" data-toggle="collapse" data-target="#bs-example-navbar-collapse-8" aria-expanded="false"> <span class="sr-only"></span> <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span> </button>
          <a href="/index.php?m=vod-search" class="glyphicon glyphicon-search visible-lg visible-md"> </a> 
		  <a class="navbar-brand col-xs-3" href="/">五杀电影院</a>
		  	 <div class="header col-xs-7"> 
				<form id="ffsearch" name="ffsearch" method="post" action="/index.php?m=vod-search">
				<input type="submit" id="searchbutton" class="globalIcon searchIcon" value="搜">
				<input type="text" id="wd" name="wd" class="aHeaderSearch top_search_btn visible-xs visible-sm" value="输入影片片名或演员名称。" onfocus="if(this.value=='输入影片片名或演员名称。'){this.value='';}" onblur="if(this.value==''){this.value='输入影片片名或演员名称。';};">
				</form> 
			</div>
			  </div>
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-8">
         <ul class="nav navbar-nav">
			 <li><a href="/" target="_self">首页</a></li>
			 
			 <li><a href="/tv/2.html" title="电影" target="_self">电影</a></li>
			 
			 <li><a href="/tv/17.html" title="电视剧" target="_self">电视剧</a></li>
			 
			 <li><a href="/tv/45.html" class="this" title="英美剧" target="_self">英美剧</a></li>
			 
			 <li><a href="/tv/20.html" title="动漫" target="_self">动漫</a></li>
			 
			 <li><a href="/tv/40.html" title="综艺" target="_self">综艺</a></li>
			 
			 <li> <a href="/zhuanti.html" title="专题">专题</a></li>
			
		 </ul>
        </div>
      </div>
    </nav>
  </div>
</div>
<script type="text/javascript" src="/template/5sdy/ads/960-90.js" charset="utf-8"></script>
<div class="container">
<div class="color visible-lg visible-md">
<div class="row  cen home">
<div class="col-md-1 padding"><p>热门</p><p>美剧</p></div>
<div class="col-md-11 ">
	<div class="row slides list_module_img">
	<ul>
		
		<li class="col-md-2 bt15"><a class="list-img " href="/v/16140.html" title="权力的游戏第八季未删减版/冰与火之歌8"><img class="lazy" data-original="/upload/vod/2019-04/201904261556268329.jpg" src="/upload/vod/2019-04/201904261556268329.jpg" alt="权力的游戏第八季未删减版/冰与火之歌8" style="display: block;"><label class="title">已完结/共6集</label><label class="name">权力的游戏第八季未删减版/冰与火之歌8</label></a></li>
		
		<li class="col-md-2 bt15"><a class="list-img " href="/v/9508.html" title="权力的游戏第八季/冰与火之歌8"><img class="lazy" data-original="/upload/vod/2019-04/201904261556268284.jpg" src="/upload/vod/2019-04/201904261556268284.jpg" alt="权力的游戏第八季/冰与火之歌8" style="display: block;"><label class="title">已完结/共6集</label><label class="name">权力的游戏第八季/冰与火之歌8</label></a></li>
		
		<li class="col-md-2 bt15"><a class="list-img " href="/v/16291.html" title="切尔诺贝利"><img class="lazy" data-original="/upload/vod/2019-05/201905091557393298.jpg" src="/upload/vod/2019-05/201905091557393298.jpg" alt="切尔诺贝利" style="display: block;"><label class="title">更新至第03集</label><label class="name">切尔诺贝利</label></a></li>
		
		<li class="col-md-2 bt15"><a class="list-img " href="/v/1105.html" title="斯巴达克斯1 血与沙第一季 未删减"><img class="lazy" data-original="/upload/vod/2019-04/201904281556389041.jpg" src="/upload/vod/2019-04/201904281556389041.jpg" alt="斯巴达克斯1 血与沙第一季 未删减" style="display: block;"><label class="title">已完结/共13集</label><label class="name">斯巴达克斯1 血与沙第一季 未删减</label></a></li>
		
		<li class="col-md-2 bt15"><a class="list-img " href="/v/1110.html" title="冰与火之歌1/权力的游戏第一季"><img class="lazy" data-original="/upload/vod/2019-04/201904261556268723.jpg" src="/upload/vod/2019-04/201904261556268723.jpg" alt="冰与火之歌1/权力的游戏第一季" style="display: block;"><label class="title">未删减/已完结/共10集</label><label class="name">冰与火之歌1/权力的游戏第一季</label></a></li>
		
		<li class="col-md-2 bt15"><a class="list-img " href="/v/1106.html" title="斯巴达克斯2 复仇 第二季 未删减"><img class="lazy" data-original="//ww3.sinaimg.cn/bmiddle/6e991fdbjw1f2a4710eiqj20b40go0w0.jpg" src="/images/blank.png" alt="斯巴达克斯2 复仇 第二季 未删减"><label class="title">已完结/共10集</label><label class="name">斯巴达克斯2 复仇 第二季 未删减</label></a></li>
		
	</ul>
	</div>
	</div>
	</div>
 
	<div class="row com margin">
		<div class="col-md-8">
			<div class="row cenwl">
				<div class="col-md-2"><p>最新更新</p></div>
				<div class="col-md-10">
					<ul class="row caten">
									
					<li class="col-md-3"><a href="/v/16389.html" title="福尔摩斯：基本演绎法 第七季">福尔摩斯：基本演绎法 第七季</a></li>
									
					<li class="col-md-3"><a href="/v/16374.html" title="哈顿花园大劫案">哈顿花园大劫案</a></li>
									
					<li class="col-md-3"><a href="/v/15872.html" title="美少女的谎言：完美主义第一季">美少女的谎言：完美主义第一季</a></li>
									
					<li class="col-md-3"><a href="/v/16378.html" title="火箭之夏">火箭之夏</a></li>
									
					<li class="col-md-3"><a href="/v/16027.html" title="斗篷与匕首第二季">斗篷与匕首第二季</a></li>
									
					<li class="col-md-3"><a href="/v/16115.html" title="吸血鬼生活第一季">吸血鬼生活第一季</a></li>
									
					<li class="col-md-3"><a href="/v/16227.html" title="红线">红线</a></li>
									
					<li class="col-md-3"><a href="/v/14692.html" title="芝加哥烈焰第七季">芝加哥烈焰第七季</a></li>
					
					</ul>
				</div>
				</div>
						<div class="row bot">
				<div class="col-md-2"><p>美剧推荐</p></div>
				<div class="col-md-10 bat">
					<ul class="row">
										
						<li class="col-md-3"><a href="/v/7076.html" title="越狱第五季 重启剧">越狱第五季 重启剧</a></li>
										
						<li class="col-md-3"><a href="/v/9508.html" title="权力的游戏第八季/冰与火之歌8">权力的游戏第八季/冰与火之歌8</a></li>
										
						<li class="col-md-3"><a href="/v/16140.html" title="权力的游戏第八季未删减版/冰与火之歌8">权力的游戏第八季未删减版/冰与火之歌8</a></li>
										
						<li class="col-md-3"><a href="/v/16301.html" title="神盾局特工第六季">神盾局特工第六季</a></li>
										
						<li class="col-md-3"><a href="/v/7747.html" title="权力的游戏第七季/冰与火之歌7">权力的游戏第七季/冰与火之歌7</a></li>
										
					</ul>
				</div>
			</div>
		</div>
		<div class="col-md-4 lebal ">
			<div class="tt">
				<a href="/artindex.html" target="_blank" class="pull-right">更多&gt;&gt;</a> 
				<span><a href="/artindex.html" target="_blank">美剧资讯</a></span>
			</div>
			<ul>
				
				<li><a href="/xinwen/3.html" title="[慎入]黑客泄露《权力的游戏8》剧本，权力的游戏第八季什么时候上映播出？" target="_self">[慎入]黑客泄露《权力的游戏8》剧本，权…</a></li>
				
				<li><a href="/xinwen/2.html" title="《金刚狼3》删减14分钟,到底删了什么？" target="_self">《金刚狼3》删减14分钟,到底删了什么？…</a></li>
				
			</ul>
		</div>
	</div>
	</div>
	<div class="wz"><span>您所在的位置：</span><a href="/">首页</a>&nbsp;&nbsp;»&nbsp;&nbsp;<a href="/tv/45.html">英美剧</a></div>
	<div class="color">
		<div class=" row kh-h1">
			<div class="col-md-12"><h1>英美剧大全</h1></div>
			<div class="col-md-12 list-fen ">
				<div class="list-f-mod ">
					<div class="mod-fl">
						<h3>类型：</h3>
						<ul>
						<li><a href="/index.php?m=vod-list-id-45-pg-1-order--by-time-class--year--letter--area--lang-.html" class="current" target="_self">全部</a></li>
						
						<li><a href="/index.php?m=vod-list-id-46-pg-1-order--by--class--year--letter--area--lang-.html" target="_self">魔幻/科幻</a></li> 
						
						<li><a href="/index.php?m=vod-list-id-47-pg-1-order--by--class--year--letter--area--lang-.html" target="_self">灵异/惊悚</a></li> 
						
						<li><a href="/index.php?m=vod-list-id-48-pg-1-order--by--class--year--letter--area--lang-.html" target="_self">动作/犯罪</a></li> 
						
						<li><a href="/index.php?m=vod-list-id-51-pg-1-order--by--class--year--letter--area--lang-.html" target="_self">喜剧/剧情</a></li> 
						
						<li><a href="/index.php?m=vod-list-id-50-pg-1-order--by--class--year--letter--area--lang-.html" target="_self">律政/医务</a></li> 
									
						</ul>
					</div>  
					<div class="mod-fl">
					  <h3>剧情：</h3>
					  <ul>
						<li><a href="/index.php?m=vod-list-id-45-pg-1-order--by-time-class--year--letter--area--lang-.html" class="current" target="_self">全部</a></li>
					  
					</ul>
					</div>
					
					<div class="mod-fl">
						<h3>年代：</h3>
						<ul>
							<li><a href="/index.php?m=vod-list-id-45-pg-1-order--by-time-class--year--letter--area--lang-.html" class="current" target="_self">全部</a></li>
							
							<li><a href="/index.php?m=vod-list-id-45-pg-1-order--by--class--year-2019-letter--area--lang-.html" target="_self">2019</a></li>
							
							<li><a href="/index.php?m=vod-list-id-45-pg-1-order--by--class--year-2018-letter--area--lang-.html" target="_self">2018</a></li>
							
							<li><a href="/index.php?m=vod-list-id-45-pg-1-order--by--class--year-2017-letter--area--lang-.html" target="_self">2017</a></li>
							
							<li><a href="/index.php?m=vod-list-id-45-pg-1-order--by--class--year-2016-letter--area--lang-.html" target="_self">2016</a></li>
							
							<li><a href="/index.php?m=vod-list-id-45-pg-1-order--by--class--year-2015-letter--area--lang-.html" target="_self">2015</a></li>
							
							<li><a href="/index.php?m=vod-list-id-45-pg-1-order--by--class--year-2014-letter--area--lang-.html" target="_self">2014</a></li>
							
							<li><a href="/index.php?m=vod-list-id-45-pg-1-order--by--class--year-2013-letter--area--lang-.html" target="_self">2013</a></li>
							
							<li><a href="/index.php?m=vod-list-id-45-pg-1-order--by--class--year-2012-letter--area--lang-.html" target="_self">2012</a></li>
							
							<li><a href="/index.php?m=vod-list-id-45-pg-1-order--by--class--year-2011-letter--area--lang-.html" target="_self">2011</a></li>
							
							<li><a href="/index.php?m=vod-list-id-45-pg-1-order--by--class--year-2010-letter--area--lang-.html" target="_self">2010</a></li>
							
							<li><a href="/index.php?m=vod-list-id-45-pg-1-order--by--class--year-2009-letter--area--lang-.html" target="_self">2009</a></li>
							
							<li><a href="/index.php?m=vod-list-id-45-pg-1-order--by--class--year-2008-letter--area--lang-.html" target="_self">2008</a></li>
							
							<li><a href="/index.php?m=vod-list-id-45-pg-1-order--by--class--year-2007-letter--area--lang-.html" target="_self">2007</a></li>
							
							<li><a href="/index.php?m=vod-list-id-45-pg-1-order--by--class--year-2006-letter--area--lang-.html" target="_self">2006</a></li>
							
						</ul>
					</div>
				</div>
			</div> 
		</div>
		<ul class="row margin slides slides-border bt15">
			
			<li class="col-md-2 col-sm-3 col-xs-6 "><a href="/v/16389.html" title="福尔摩斯：基本演绎法 第七季" target="_blank" class="list-img"><img class="loading lazy" data-original="/upload/vod/2019-05/201905251558718456.jpg" src="/upload/vod/2019-05/201905251558718456.jpg" alt="福尔摩斯：基本演绎法 第七季" style="display: block;"><label class="title">更新至第01集</label><label class="name">福尔摩斯：基本演绎法 第七季</label></a></li>
			
			<li class="col-md-2 col-sm-3 col-xs-6 "><a href="/v/16374.html" title="哈顿花园大劫案" target="_blank" class="list-img"><img class="loading lazy" data-original="/upload/vod/2019-05/201905231558596643.jpg" src="/upload/vod/2019-05/201905231558596643.jpg" alt="哈顿花园大劫案" style="display: block;"><label class="title">更新至第03集</label><label class="name">哈顿花园大劫案</label></a></li>
			
			<li class="col-md-2 col-sm-3 col-xs-6 "><a href="/v/15872.html" title="美少女的谎言：完美主义第一季" target="_blank" class="list-img"><img class="loading lazy" data-original="/upload/vod/2019-04/201904261556266575.jpg" src="/upload/vod/2019-04/201904261556266575.jpg" alt="美少女的谎言：完美主义第一季" style="display: block;"><label class="title">更新至第10集</label><label class="name">美少女的谎言：完美主义第一季</label></a></li>
			
			<li class="col-md-2 col-sm-3 col-xs-6 "><a href="/v/16378.html" title="火箭之夏" target="_blank" class="list-img"><img class="loading lazy" data-original="/upload/vod/2019-05/201905241558691846.jpg" src="/upload/vod/2019-05/201905241558691846.jpg" alt="火箭之夏" style="display: block;"><label class="title">更新至第01集</label><label class="name">火箭之夏</label></a></li>
			
			<li class="col-md-2 col-sm-3 col-xs-6 "><a href="/v/16027.html" title="斗篷与匕首第二季" target="_blank" class="list-img"><img class="loading lazy" data-original="/upload/vod/2019-04/201904271556297438.jpg" src="/upload/vod/2019-04/201904271556297438.jpg" alt="斗篷与匕首第二季" style="display: block;"><label class="title">更新至第09集</label><label class="name">斗篷与匕首第二季</label></a></li>
			
			<li class="col-md-2 col-sm-3 col-xs-6 "><a href="/v/16115.html" title="吸血鬼生活第一季" target="_blank" class="list-img"><img class="loading lazy" data-original="/upload/vod/2019-04/201904261556265147.jpg" src="/upload/vod/2019-04/201904261556265147.jpg" alt="吸血鬼生活第一季" style="display: block;"><label class="title">更新至第09集</label><label class="name">吸血鬼生活第一季</label></a></li>
			
			<li class="col-md-2 col-sm-3 col-xs-6 "><a href="/v/16227.html" title="红线" target="_blank" class="list-img"><img class="loading lazy" data-original="/upload/vod/2019-04/201904301556630695.jpg" src="/upload/vod/2019-04/201904301556630695.jpg" alt="红线" style="display: block;"><label class="title">已完结/共8集</label><label class="name">红线</label></a></li>
			
			<li class="col-md-2 col-sm-3 col-xs-6 "><a href="/v/14692.html" title="芝加哥烈焰第七季" target="_blank" class="list-img"><img class="loading lazy" data-original="/upload/vod/2019-04/201904261556266810.jpg" src="/upload/vod/2019-04/201904261556266810.jpg" alt="芝加哥烈焰第七季" style="display: block;"><label class="title">已完结/共22集</label><label class="name">芝加哥烈焰第七季</label></a></li>
			
			<li class="col-md-2 col-sm-3 col-xs-6 "><a href="/v/14691.html" title="芝加哥医院第四季" target="_blank" class="list-img"><img class="loading lazy" data-original="/upload/vod/2019-04/201904261556265278.jpg" src="/upload/vod/2019-04/201904261556265278.jpg" alt="芝加哥医院第四季" style="display: block;"><label class="title">已完结/共22集</label><label class="name">芝加哥医院第四季</label></a></li>
			
			<li class="col-md-2 col-sm-3 col-xs-6 "><a href="/v/16000.html" title="幻想快乐第二季" target="_blank" class="list-img"><img class="loading lazy" data-original="/upload/vod/2019-04/201904261556266533.jpg" src="/upload/vod/2019-04/201904261556266533.jpg" alt="幻想快乐第二季" style="display: block;"><label class="title">更新至第09集</label><label class="name">幻想快乐第二季</label></a></li>
			
			<li class="col-md-2 col-sm-3 col-xs-6 "><a href="/v/14824.html" title="海豹突击队第二季" target="_blank" class="list-img"><img class="loading lazy" data-original="/upload/vod/2019-04/201904281556447826.jpg" src="/upload/vod/2019-04/201904281556447826.jpg" alt="海豹突击队第二季" style="display: block;"><label class="title">已完结/共22集</label><label class="name">海豹突击队第二季</label></a></li>
			
			<li class="col-md-2 col-sm-3 col-xs-6 "><a href="/v/15709.html" title="互怼特工第一季" target="_blank" class="list-img"><img class="loading lazy" data-original="/upload/vod/2019-04/201904261556266790.jpg" src="/upload/vod/2019-04/201904261556266790.jpg" alt="互怼特工第一季" style="display: block;"><label class="title">已完结/共13集</label><label class="name">互怼特工第一季</label></a></li>
			
			<li class="col-md-2 col-sm-3 col-xs-6 "><a href="/v/15161.html" title="新圣女魔咒第一季" target="_blank" class="list-img"><img class="loading lazy" data-original="/upload/vod/2019-05/201905241558631744.jpg" src="/upload/vod/2019-05/201905241558631744.jpg" alt="新圣女魔咒第一季" style="display: block;"><label class="title">更新至第19集</label><label class="name">新圣女魔咒第一季</label></a></li>
			
			<li class="col-md-2 col-sm-3 col-xs-6 "><a href="/v/16100.html" title="新阴阳魔界第一季" target="_blank" class="list-img"><img class="loading lazy" data-original="/upload/vod/2019-04/201904261556266769.jpg" src="/upload/vod/2019-04/201904261556266769.jpg" alt="新阴阳魔界第一季" style="display: block;"><label class="title">更新至第09集</label><label class="name">新阴阳魔界第一季</label></a></li>
			
			<li class="col-md-2 col-sm-3 col-xs-6 "><a href="/v/16373.html" title="血宝藏第一季" target="_blank" class="list-img"><img class="loading lazy" data-original="/upload/vod/2019-05/201905231558596494.jpg" src="/upload/vod/2019-05/201905231558596494.jpg" alt="血宝藏第一季" style="display: block;"><label class="title">更新至第02集</label><label class="name">血宝藏第一季</label></a></li>
			
			<li class="col-md-2 col-sm-3 col-xs-6 "><a href="/v/15701.html" title="宵禁第一季" target="_blank" class="list-img"><img class="loading lazy" data-original="/upload/vod/2019-05/201905231558597687.jpg" src="/upload/vod/2019-05/201905231558597687.jpg" alt="宵禁第一季" style="display: block;"><label class="title">更新至第05集</label><label class="name">宵禁第一季</label></a></li>
			
			<li class="col-md-2 col-sm-3 col-xs-6 "><a href="/v/14695.html" title="美式主妇第三季" target="_blank" class="list-img"><img class="loading lazy" data-original="/upload/vod/2019-04/201904281556448217.jpg" src="/upload/vod/2019-04/201904281556448217.jpg" alt="美式主妇第三季" style="display: block;"><label class="title">更新至第23集</label><label class="name">美式主妇第三季</label></a></li>
			
			<li class="col-md-2 col-sm-3 col-xs-6 "><a href="/v/15877.html" title="大城小村第一季" target="_blank" class="list-img"><img class="loading lazy" data-original="/upload/vod/2019-04/201904281556448418.jpg" src="/upload/vod/2019-04/201904281556448418.jpg" alt="大城小村第一季" style="display: block;"><label class="title">已完结/共10集</label><label class="name">大城小村第一季</label></a></li>
			
			<li class="col-md-2 col-sm-3 col-xs-6 "><a href="/v/15476.html" title="神烦警探第六季" target="_blank" class="list-img"><img class="loading lazy" data-original="/upload/vod/2019-05/201905071557163146.jpg" src="/upload/vod/2019-05/201905071557163146.jpg" alt="神烦警探第六季" style="display: block;"><label class="title">已完结/共18集</label><label class="name">神烦警探第六季</label></a></li>
			
			<li class="col-md-2 col-sm-3 col-xs-6 "><a href="/v/16231.html" title="地球百子第六季" target="_blank" class="list-img"><img class="loading lazy" data-original="/upload/vod/2019-05/201905021556788940.jpg" src="/upload/vod/2019-05/201905021556788940.jpg" alt="地球百子第六季" style="display: block;"><label class="title">更新至第04集</label><label class="name">地球百子第六季</label></a></li>
			
			<li class="col-md-2 col-sm-3 col-xs-6 "><a href="/v/15913.html" title="弥补第一季" target="_blank" class="list-img"><img class="loading lazy" data-original="/upload/vod/2019-04/201904281556449462.jpg" src="/upload/vod/2019-04/201904281556449462.jpg" alt="弥补第一季" style="display: block;"><label class="title">已完结/共10集</label><label class="name">弥补第一季</label></a></li>
			
			<li class="col-md-2 col-sm-3 col-xs-6 "><a href="/v/15721.html" title="与敌共谋第一季" target="_blank" class="list-img"><img class="loading lazy" data-original="/upload/vod/2019-04/201904281556448402.jpg" src="/upload/vod/2019-04/201904281556448402.jpg" alt="与敌共谋第一季" style="display: block;"><label class="title">已完结/共13集</label><label class="name">与敌共谋第一季</label></a></li>
			
			<li class="col-md-2 col-sm-3 col-xs-6 "><a href="/v/16084.html" title="军事法典/军法第一季" target="_blank" class="list-img"><img class="loading lazy" data-original="/upload/vod/2019-04/201904281556448431.jpg" src="/upload/vod/2019-04/201904281556448431.jpg" alt="军事法典/军法第一季" style="display: block;"><label class="title">更新至第07集</label><label class="name">军事法典/军法第一季</label></a></li>
			
			<li class="col-md-2 col-sm-3 col-xs-6 "><a href="/v/16149.html" title="鬼屋欢乐送第一季" target="_blank" class="list-img"><img class="loading lazy" data-original="/upload/vod/2019-04/201904281556449282.jpg" src="/upload/vod/2019-04/201904281556449282.jpg" alt="鬼屋欢乐送第一季" style="display: block;"><label class="title">更新至第06集</label><label class="name">鬼屋欢乐送第一季</label></a></li>
				
			<div class="clearfix"></div>
		</ul>
		<div class="pager">共947条数据&nbsp;当前:1/40页&nbsp;<em>首页</em>&nbsp;<em>上一页</em>&nbsp;<span class="pagenow">1</span>&nbsp;<a target="_self" class="pagelink_b" href="/tv/45-2.html">2</a>&nbsp;<a target="_self" class="pagelink_b" href="/tv/45-3.html">3</a>&nbsp;<a target="_self" class="pagelink_b" href="/tv/45-4.html">4</a>&nbsp;<a target="_self" class="pagelink_b" href="/tv/45-5.html">5</a>&nbsp;<a target="_self" class="pagelink_b" href="/tv/45-6.html">6</a>&nbsp;<a target="_self" href="/tv/45-2.html" class="pagelink_a">下一页</a>&nbsp;<a target="_self" href="/tv/45-40.html" class="pagelink_a">尾页</a>&nbsp;<input type="input" name="page" id="page" size="4" class="pagego"><input type="button" value="跳 转" onclick="pagego('/tv/45-{pg}.html',40)" class="pagebtn"></div>
	</div>
</div>	
﻿<!--底部开始--> 
<div class="footer ">
<script src="/template/5sdy/ads/tiao.js"></script>
	<div class="fBox container">
		
		<div class="clearfix"></div>
		﻿<div class="footer_nav" style="display:none;"><script src="/js/tj.js"></script><!--— Global site tag (gtag.js) - Google Analytics —-->
<script async="" src="https://www.googletagmanager.com/gtag/js?id=UA-111341196-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-111341196-1');
</script>
<script>var _hmt=_hmt||[];(function(){var hm=document.createElement('script');hm.src='https://hm.baidu.com/hm.js?e3505c2df04d4cb537a857e99eb666b5';var s=document.getElementsByTagName('script')[0];s.parentNode.insertBefore(hm,s)})();</script>
</div>
		本网站提供新影视资源均系收集各大网站，本网站只提供web页面浏览服务，并不提供影片资源存储，也不参与任何视频录制、上传<br>若本站收集的节目无意侵犯了贵司版权，邮箱地址来信，我们将在第一时间删<br>Copyright © 2015-2018 <a href="http://www.lol5s.com/"><font face="Verdana, Arial, Helvetica, sans-serif"><b><font color="#F60">www.lol5s.com</font></b></font></a>.All Rights Reserved .
	</div>
</div>
<!--底部结束-->



</body></html>
'''
soup = BeautifulSoup(html_doc,'html.parser')
#获取所有链接
links = soup.find_all('a')
base = 'http://www.lol5s.com/ www.lol5s.com'
for link in links:
    c = urljoin(base,link['href'])
    print(link.name,link['href'],link.get_text(),c)

