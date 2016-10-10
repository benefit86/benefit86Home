#!/usr/bin/perl
#↑パールパス設定。サーバに合わせて必要であれば変更してください。
########################################################################################################
# 著作権の表示
# パソコン用メール送信フォーム(2009.10)
# 作者 中野智丹
########################################################################################################
#設定ファイル
require './setting.pl';
require './inquiry.pl';

#日本語変換ライブラリの設定
require './mimew.pl';
#日時の取得
$nowtime = time;

#■デコード
if ($ENV{'REQUEST_METHOD'} eq "POST") { read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'}); }
else { $buffer = $ENV{'QUERY_STRING'}; }

if ($buffer eq "") { &err1('エラーです。'); }

@pairs = split(/&/,$buffer);
foreach $pair (@pairs) {
 
 ($name,$value) = split(/=/, $pair);
 $name2 = $name;
 $value2 = $value;
 $FORM2{$name} = $value;
 
 $value =~ tr/+/ /;
 $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
 $value =~ s/</&lt;/g;
 $value =~ s/>/&gt;/g;
 $value =~ s/\n/<br>/g; 
 $value =~ s/\r//g;
 $value =~ s/\t//g;
 $value =~ s/"/'/g;
 #フォーム変数へ
 $FORM{$name} = $value;
}

$name1 = $FORM{'name1'};
$kana = $FORM{'kana'};
$company = $FORM{'company'};
$mail = $FORM{'mail'};
$situmon = $FORM{'situmon'};

$hensin = $FORM{'hensin'};
$kakunin = $FORM{'kakunin'};

#日時取得
sub time1{
 $ENV{'TZ'} = "JST-9";
 $time = time;
 local($sec,$min,$hour,$mday,$mon,$year) = localtime($time);

 # 日時のフォーマット
 $data_now1 = sprintf("%04d %02d/%02d %02d:%02d",
   $year+1900,$mon+1,$mday,$hour,$min);

}

#日時取得4
sub time4{
 $ENV{'TZ'} = "JST-9";
 $time = time;
 local($sec,$min,$hour,$mday,$mon,$year) = localtime($time);

 # 日時のフォーマット
 $data_now4 = sprintf("%04d%02d%02d",
   $year+1900,$mon+1,$mday);
}

#送信完了画面の出力
if($kakunin eq "1"){
 &kakunin();
}else{
 &kanryou();
} 

#確認画面のレイアウトを改造するには↓を変更します。
sub kakunin{

print <<"OUT_HTML";
Content-type: text/html

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>お問い合わせ｜ビジネス・企業 #4</title>
<meta name="keywords" content="キーワード" />
<meta name="description" content="サイトの説明" />
<link href="../css/import.css" rel="stylesheet" type="text/css">
<script type="text/javascript" src="../js/import.js"></script>
</head>
<body>
<!--ヘッダー-->
<div id="header" class="clearfix">
  <h1><a href="./">SAMPLE TEMPLATE</a></h1>
</div>
<!--ヘッダー終了-->
<!--グローバルナビゲーション-->
<div id="globalNavi">
  <ul class="clearfix">
    <li><a href="./">トップページ<br>
      <span>TOP</span></a></li>
    <li><a href="../service.html">事業情報<br>
      <span>SERVICE</span></a></li>
    <li><a href="../company.html">会社概要<br>
      <span>COMPANY</span></a></li>
    <li><a href="../recruit.html">採用情報<br>
      <span>RECRUIT</span></a></li>
    <li><a href="../contact.html">お問い合わせ<br>
      <span>CONTACT</span></a></li>
  </ul>
</div>
<!--グローバルナビゲーション終了-->
<!--ビジュアル-->
<div id="ttl_catch">
  <h2>お問い合わせ</h2>
</div>
<!--ビジュアル終了-->
<!--コンテンツ-->
<div id="contents" class="clearfix">
  <!--メイン-->
  <div id="main">
    <div class="section">
      <h3>お問い合わせ</h3>
      <form action="inquiry.cgi" method="post">
      <input type="hidden" name="name1" value="$name1" />
      <input type="hidden" name="kana" value="$kana" />
      <input type="hidden" name="company" value="$company" />
      <input type="hidden" name="mail" value="$mail" />
      <input type="hidden" name="situmon" value="$situmon" />
      <input name="hensin" type="hidden" value="1">
        <table width="100%" border="0" cellspacing="0" cellpadding="0" class="table_01">
          <colgroup>
          <col width="25%">
          <col width="75%">
          </colgroup>
          <tr>
            <th>
              <label for="name1">お名前</label>
              ※ </th>
            <td>$name1</td>
          </tr>
          <tr>
            <th>
              <label for="kana">ふりがな</label>
              ※ </th>
            <td>$kana</td>
          </tr>
          <tr>
            <th>
              <label for="company">会社名</label>
            </th>
            <td>$company</td>
          </tr>
          <tr>
            <th>
              <label for="mail">メールアドレス</label>
              ※ </th>
            <td>$mail</td>
          </tr>
          <tr>
            <th>
              <label for="situmon">お問い合わせ内容</label>
            ※</th>
            <td>$situmon</td>
          </tr>
        </table>
        <p class="align_center">
          <input name="" type="submit" value="上記内容で送信する">
        </p>
      </form>
    </div>
  </div>
  <!--メイン終了-->
  <!--サブ-->
  <div id="sub">
    <div class="btn_contact"><a href="../contact.html">お問い合わせ</a></div>
    <ul class="bnr">
      <li><img src="../images/common/bnr_twitter.gif" alt="Twitterアカウント"></li>
      <li><img src="../images/common/bnr_facebook.gif" alt="facebookページ"></li>
    </ul>
  </div>
  <!--サブ終了-->
</div>
<!--コンテンツ終了-->
<!--フッター-->
<div id="footer">
  <div class="inr_group">
    <div class="group_link clearfix">
      <p class="policy"><a href="../privacy.html">プライバシーポリシー</a></p>
      <p class="copy">COPYRIGHT &copy; 2013 SAMPLE ALL RIGHTS RESERVED.</p>
    </div>
  </div>
</div>
<!--フッター終了-->
</body>
</html>

OUT_HTML
exit;
}


#送信完了画面のレイアウトを改造するには↓を変更します。
sub kanryou{

&time1;
&time4;

#IPアドレス
$ip = $ENV{'REMOTE_ADDR'};
#ユーザーホスト
$user = gethostbyaddr(pack("C4" ,split(/\./, $ip)), 2);
#ブラウザ
$browser = $ENV{'HTTP_USER_AGENT'};


if($ng eq "1" )
{

open(BROWSERFILE, "<$ngbrowser") or &err1('このブラウザでの閲覧は禁止されております。');
flock(BROWSERFILE, 2);
@NGBROWSER = <BROWSERFILE>;
flock(BROWSERFILE, 8);
close(BROWSERFILE);

foreach $ngbrowser9 (@NGBROWSER)
{
($ngbrowser99) = split(/<>/,$ngbrowser9);
if($browser eq $ngbrowser99)
{
  &err1('このブラウザでの閲覧は禁止されております。');
}
}

open(IPFILE, "<$ngip") or &err1('恐れ入りますが現在送信不可となっております。');
flock(IPFILE, 2);
@NGIP = <IPFILE>;
flock(IPFILE, 8);
close(IPFILE);

foreach $ngip9 (@NGIP)
{
($ngip99) = split(/<>/,$ngip9);
if($ip eq $ngip99)
{
  &err1('恐れ入りますが現在送信不可となっております。');
}
}
open(HOSTFILE, "<$nghost") or &err1('ご利用サーバーからの投函は禁止されております');
flock(HOSTFILE, 2);
@NGHOST = <HOSTFILE>;
flock(HOSTFILE, 8);
close(HOSTFILE);

foreach $nghost9 (@NGHOST)
{
($nghost99) = split(/<>/,$nghost9);
if($user eq $nghost99)
{
  &err1('ご利用サーバーからの投函は禁止されております');
}
}

open(NGMAIL, "<$ngmail") or &err1('このメールアドレスでのお問い合わせは受付しておりません。');
flock(NGMAIL, 2);
@NGMAIL = <NGMAIL>;
flock(NGMAIL, 8);
close(NGMAIL);

foreach $ngmail9 (@NGMAIL)
{
($ngmail99) = split(/<>/,$ngmail9);
if($mail eq $ngmail99)
{
  &err1('このメールアドレスでのお問い合わせは受付しておりません。');
}
}

open(HOSTFILE2, "<$nghost2") or &err1('このサーバーで一部送信が禁止されている可能性があります。');
flock(HOSTFILE2, 2);
@NGHOST2 = <HOSTFILE2>;
flock(HOSTFILE2, 8);
close(HOSTFILE2);

foreach $nghost92 (@NGHOST2)
{
($nghost992) = split(/<>/,$nghost92);
if($user =~ $nghost992)
{
  &err1('このサーバーで一部送信が禁止されている可能性があります。');
}
}

open(NGWORD, "<$ngword") or &err1('受付されていない文字を含んでいる可能性があります。');
flock(NGWORD, 2);
@NGWORD = <NGWORD>;
flock(NGWORD, 8);
close(NGWORD);

foreach $ngword9 (@NGWORD)
{
($ngword99) = split(/<>/,$ngword9);
if($situmon =~ $ngword99)
{
  &err1('受付されていない文字を含んでいる可能性があります。');
}
}

}

#日時の処理
open(NGTIME, "<$ngtime");
flock(NGTIME, 2);
$NGTIMENOW = <NGTIME>;
flock(NGTIME, 8);
close (NGTIME);

if($NGTIMENOW < $data_now4){
unlink  "$ngtime";
unlink  "$ngrenzoku";

chmod 0606, $ngtime;
chmod 0606, $ngrenzoku;

open(NGTIME, "+<$ngtime");
flock(NGTIME, 2);
seek (NGTIME, 0, 0);
print NGTIME "$data_now4\n";
flock(NGTIME, 8);
close (NGTIME);
}

#連続投稿のチェック

foreach $tdata (@RENZOKU)
{
 ($A1,$B1,$C1,$D1,$E1) = split (/<>/,$tdata);
 $A1 += $ngrk;
 if($ip eq $D1){
 if($A1 > $nowtime){
  &err1('すでにお問い合わせをされています。');
}
}
}

print <<"OUT_HTML";
Content-type: text/html

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>お問い合わせ｜ビジネス・企業 #4</title>
<meta name="keywords" content="キーワード" />
<meta name="description" content="サイトの説明" />
<link href="../css/import.css" rel="stylesheet" type="text/css">
<script type="text/javascript" src="../js/import.js"></script>
</head>
<body>
<!--ヘッダー-->
<div id="header" class="clearfix">
  <h1><a href="./">SAMPLE TEMPLATE</a></h1>
</div>
<!--ヘッダー終了-->
<!--グローバルナビゲーション-->
<div id="globalNavi">
  <ul class="clearfix">
    <li><a href="./">トップページ<br>
      <span>TOP</span></a></li>
    <li><a href="../service.html">事業情報<br>
      <span>SERVICE</span></a></li>
    <li><a href="../company.html">会社概要<br>
      <span>COMPANY</span></a></li>
    <li><a href="../recruit.html">採用情報<br>
      <span>RECRUIT</span></a></li>
    <li><a href="../contact.html">お問い合わせ<br>
      <span>CONTACT</span></a></li>
  </ul>
</div>
<!--グローバルナビゲーション終了-->
<!--ビジュアル-->
<div id="ttl_catch">
  <h2>お問い合わせ</h2>
</div>
<!--ビジュアル終了-->
<!--コンテンツ-->
<div id="contents" class="clearfix">
  <!--メイン-->
  <div id="main">
    <div class="section">
      <h3>送信完了しました</h3>
<p>この度は、お問い合わせ頂き、誠にありがとうございます。<br><br>
  ご記入いただきましたメールアドレスの方へ、ご入力内容の確認メールを送信させていただきましたので、<br>
  そちらも合わせてご確認下さい。折り返し、担当者よりご連絡をさせていただきます。<br><br>何卒よろしくお願い致します。</p>
    </div>
  </div>
  <!--メイン終了-->
  <!--サブ-->
  <div id="sub">
    <div class="btn_contact"><a href="../contact.html">お問い合わせ</a></div>
    <ul class="bnr">
      <li><img src="../images/common/bnr_twitter.gif" alt="Twitterアカウント"></li>
      <li><img src="../images/common/bnr_facebook.gif" alt="facebookページ"></li>
    </ul>
  </div>
  <!--サブ終了-->
</div>
<!--コンテンツ終了-->
<!--フッター-->
<div id="footer">
  <div class="inr_group">
    <div class="group_link clearfix">
      <p class="policy"><a href="../privacy.html">プライバシーポリシー</a></p>
      <p class="copy">COPYRIGHT &copy; 2013 SAMPLE ALL RIGHTS RESERVED.</p>
    </div>
  </div>
</div>
<!--フッター終了-->
</body>
</html>

OUT_HTML

  $subject = &mimeencode($kenmei);
  $subject2 = &mimeencode($kenmei2);
  $mail = &mimeencode($mail);
  $sendAddress = &mimeencode($sendAddress);

$DATA = "送信日時";
$USER = "ホスト";
$IP = "IPアドレス";
$BROWSER = "ブラウザ";

#改行
$biko =~ s/&lt;br&gt;/\n/g;

#自分に送信されるメールです。改造するには↓を変更します。

  open (MAIL, "|$mailprog $sendAddress") || die "Can't open $mailprog!\n";
  print MAIL "From: $mail\n";
  print MAIL "Subject: $subject\n";
  print MAIL "MIME-Version: 1.0\n";
  print MAIL "Content-type: text/plain; charset=utf-8\n";
  print MAIL "\n";
  print MAIL "【 お問い合わせがありました。 】\n\n";
  print MAIL "[氏名]\n";
  print MAIL "$name1\n\n";
  print MAIL "[ふりがな]\n";
  print MAIL "$name1\n\n";
  print MAIL "[会社名]\n";
  print MAIL "$company\n\n";
  print MAIL "[メールアドレス]\n";
  print MAIL "$mail\n\n";
  print MAIL "[お問い合わせ内容]\n";
  print MAIL "$situmon\n\n";
  print MAIL "■■■■■■■■\n";
  print MAIL "[$DATA]\n";
  print MAIL "$data_now1\n";
  print MAIL "[$USER]\n";
  print MAIL "$user\n";
  print MAIL "[$IP]\n";
  print MAIL "$ip\n";
  print MAIL "[$BROWSER]\n";
  print MAIL "$browser\n";
  print MAIL "■■■■■■■■\n";
  close (MAIL);

if($FORM{'hensin'} eq "1" ){
#閲覧者に送信される控えメールです。
  open (MAIL, "|$mailprog $mail") || die "Can't open $mailprog!\n";
  print MAIL "From: $sendAddress\n";
  print MAIL "To: $mail\n";
  print MAIL "Subject: $subject2\n";
  print MAIL "MIME-Version: 1.0\n";
  print MAIL "Content-type: text/plain; charset=utf-8\n";
  print MAIL "\n";
  print MAIL "$name1 様\n\n";
  print MAIL "この度は、お問い合わせ頂き、誠にありがとうございます。\n\n";
  print MAIL "--------------------------------------------\n\n";
  print MAIL "【 お客様情報 】\n\n";
  print MAIL "お客様が送信されました情報は以下の通りになります。\n\n";
  print MAIL "[氏名]\n";
  print MAIL "$name1\n\n";
  print MAIL "[ふりがな]\n";
  print MAIL "$name1\n\n";
  print MAIL "[会社名]\n";
  print MAIL "$company\n\n";
  print MAIL "[メールアドレス]\n";
  print MAIL "$mail\n\n";
  print MAIL "[お問い合わせ内容]\n";
  print MAIL "$situmon\n\n";
  print MAIL "-----------------------------------------------\n";
  print MAIL "後程上記内容を確認し、24時間以内に担当者よりご連絡させていただきます。\n";
  print MAIL "いま暫くお待ちいただきます様、宜しくお願い致します。\n\n";
  print MAIL "◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇\n";
  print MAIL "サンプル株式会社\n";
  print MAIL "大阪府大阪市\n";
  print MAIL "営業時間00：00～00：00（土日休日）\n";
  print MAIL "TEL.0000-000-000\n";
  print MAIL "◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇\n";
  close (MAIL);
} 
exit;  
}

