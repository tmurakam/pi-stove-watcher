# ガスコンロ監視アプリケーション

Raspberry Pi + サーマルセンサ(AMG88xx) を使用したガスコンロ監視アプリです。

温度が上がった状態が一定時間継続するたびに、アラーム (サウンド) が鳴ります。
                                      
以下を参考にしています。

* https://www.youtube.com/watch?v=q2a0arclhbU
* https://github.com/kotamorishi/pi-thermal-camera

# 必要環境

* Raspberry Pi
* OS: Raspberry Pi OS: bookworm
* AGM88xx
* (Alexa) => 不要

# 使用方法

Raspberry Pi に本アプリを展開します。
以下を実行し、必要な python ライブラリをインストールします。

    $ pip install -r requirements.txt

Alexa に音声をしゃべらせる場合、`secret.sh` を以下の内容で作成しておく必要があります。

    EMAIL='Amazonアカウント}'
    PASSWORD='{Amazonパスワード}'

注: Alexa 連携は現在うまく動作しないため、無効化しています。

サーマルセンサをガスコンロ側に向けてください。1m くらいまでは認識します。

`main.py` を実行すると監視を開始します。

温度が High threshold 以上になると High 状態に、Low threashold 以下になると Low 状態に遷移します。
High 状態で5分経過することに、スピーカーおよび Alexa から警告を再生します。

# カスタマイズ

AMG8833 のアドレスは 0x69 にしてあります。変更したいときは main.py の以下の行を変更してください。

    sensor = Adafruit_AMG88xx(address=0x68)

温度スレッショルドは、`stove_watcher.py` の THR_H および THR_L で指定します。

警告音インターバルは `stove_watcher.py` の ALARM_INTERVAL で指定します。

Alexa デバイスの識別子は、`alerter_sound.py` の DEVICE で指定します。
また喋らせるテキストも本ファイルで定義します。

# 自動起動

Rasberry Pi 起動時に自動起動するためには、~/.config/autostart/stove-watcher.desktop ファイルを以下の内容で作成してください。

```
[Desktop Entry]
Exec=lxterminal -e /[path_to_thi_app]/startup.sh
Type=Application
Name=stove-watcher
Terminal=use
```
