########################################################################################################
# 設定用ファイルです。
# このファイルさえ設定してしまえば、他のファイルの設定を変更する必要は特にありません。
# 各ファイル一行目のパールパスの設定のみで済みます。
# このファイル(setting.pl)の名称を変更しますと動かなくなるので名称を変更しないでください。
########################################################################################################

############
# 基本設定 #
############

#メールサーバーのパス設定
$mailprog = '/usr/lib/sendmail';

#あなたのメールアドレス
$sendAddress = 'あなたのメールアドレス';

#CGIの文字コード設定
$mcode = 'utf-8';

#スクリプトの名称。うまく動かない場合はhttpから始まる絶対パスで入力
$script = 'pc_mail.cgi';

#送信フォームの名称。相対パスの場合はこのスクリプトからのパス
$form = 'pc_mail.html';

#メールを送信し終わった後に表示するリンク先URL。相対パスの場合はこのスクリプトからのパス
$jump = '../../';

#メールを送信し終わった後に表示するリンク先の名称
$jumpname = 'トップページ';

#メールを送信し終わった後に表示するメッセージ
$msg = '送信しました。ご協力ありがとうございました。';

#控えのメールに添付するメッセージ(メッセージ等)
$msg2 = 'テストメッセージ1';

#控えのメールに添付するメッセージ2(URL等)
$msg3 = 'テストメッセージ2';

#背景色
$collar1 = 'white';

#文字色
$collar2 = '';
	
#リンクの文字色
$collar3 = '';

#見出しの文字色
$collar4 = 'blue';

#テーブルのボーダー色
$collar5 = 'black';

#見出しの文字色
$collar6 = 'red';

#テーブルの見出し色
$collar7 = '#FFCC00';

#テーブルの背景色
$collar8 = 'white';

#背景に画像を使用する場合は画像までのパスを入力。画像等を使用しない場合は空白に。
$backimage = '';

#普通の文字の大きさ
$size1 = '85%';

#小さい文字の大きさ
$size2 = '75%';

#見出し文字の大きさ
$size3 = '200%';

#見出しの文字の大きさ2
$size4 = '150%';

#########################
#    メール関連 項目    #
#########################

#項目1（送信項目の名称）
$list1 = "[お名前]";
	
#項目2（送信項目の名称）
$list2 = "[メールアドレス]";

#項目3（送信項目の名称）
$list3 = "[ご住所]";

#項目4（送信項目の名称）
$list4 = "[お電話番号]";

#項目5（送信項目の名称）
$list5 = "[お問い合せ内容]";

#項目6（送信項目の名称）
$list6 = "[ご希望の連絡方法]";

###################
# スパム禁止用設定
###################

#スパム禁止管理画面のパスワード設定
$adminpass = 'admin0123';

#スパム禁止機能を使用する場合は1をそうでない場合は0を入力
$ng = '0';

#英字のみのメールを禁止する機能を使用する場合は1をそうでない場合は0を入力
$alphabetng = '0';

#連続利用禁止期間を秒数で入力。連続利用を禁止しない場合は0を入力。
$ngrk = '0';

#最小入力文字数
$saisyou = '0';

#最大入力文字数
$saidai = '100000';

#日時記録ファイル。
$ngtime = 'ng/ngtime.cgi';

#連続利用禁止記録ファイル。
$ngrenzoku = 'ng/ngrenzoku.cgi';

#日時記録ファイル。
$ngtime = 'ng/ngtime.cgi';

#禁止IPリストの名称。
$ngip = 'ng/ngip.cgi';

#禁止サーバリスト完全一致。
$nghost = 'ng/nghost.cgi';

#禁止サーバリスト部分一致。
$nghost2 = 'ng/nghost2.cgi';

#禁止メールアドレスの名称。
$ngmail = 'ng/ngmail.cgi';

#禁止ブラウザの名称。
$ngbrowser = 'ng/ngbrowser.cgi';

#禁止ワードリストの名称。
$ngword = 'ng/ngword.cgi';

1;
